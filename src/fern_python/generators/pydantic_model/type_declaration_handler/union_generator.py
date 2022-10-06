from typing import List

from typing_extensions import Never

from fern_python.codegen import AST, LocalClassReference
from fern_python.declaration_handler import DeclarationHandlerContext
from fern_python.generated import ir_types
from fern_python.pydantic_codegen import (
    PYDANTIC_FIELD_REFERENCE,
    PydanticField,
    PydanticModel,
)

from ..fern_aware_pydantic_model import FernAwarePydanticModel
from .abstract_type_generator import AbstractTypeGenerator
from .get_visit_method import VisitableItem, VisitorArgument, get_visit_method

VISITOR_RETURN_TYPE = AST.GenericTypeVar(name="T_Result")
BUILDER_ARGUMENT_NAME = "value"


class UnionGenerator(AbstractTypeGenerator):
    def __init__(
        self,
        name: ir_types.DeclaredTypeName,
        union: ir_types.UnionTypeDeclaration,
        context: DeclarationHandlerContext,
    ):
        super().__init__(name=name, context=context)
        self._union = union

    def generate(self) -> None:
        factory_declaration = AST.ClassDeclaration(name="_Factory")
        factory = self._context.source_file.add_class_declaration(factory_declaration)

        with FernAwarePydanticModel(type_name=self._name, context=self._context) as external_pydantic_model:
            external_pydantic_model.add_class_var_unsafe(
                name="factory",
                type_hint=AST.TypeHint(type=factory),
                initializer=AST.Expression(AST.ClassInstantiation(class_=factory)),
            )

            internal_single_union_types: List[LocalClassReference] = []

            internal_union = self._context.source_file.add_class_declaration(
                declaration=AST.ClassDeclaration(name="_" + external_pydantic_model.get_class_name()),
            )

            for single_union_type in self._union.types:
                shape = single_union_type.shape.get_as_union()
                if shape.properties_type == "samePropertiesAsObject":
                    external_pydantic_model.add_ghost_reference(shape)
                elif shape.properties_type == "singleProperty":
                    if shape.type.__root__.type == "named":
                        external_pydantic_model.add_ghost_reference(shape.type.__root__)
                elif shape.properties_type == "noProperties":
                    pass
                else:
                    assert_never(shape.properties_type)

                with PydanticModel(
                    name=single_union_type.discriminant_value.pascal_case,
                    source_file=self._context.source_file,
                    base_models=single_union_type.shape.visit(
                        same_properties_as_object=lambda type_name: [
                            self._context.get_class_reference_for_type_name(type_name)
                        ],
                        single_property=lambda property_: None,
                        no_properties=lambda: None,
                    ),
                    parent=internal_union,
                ) as internal_pydantic_model_for_single_union_type:

                    internal_single_union_type = internal_pydantic_model_for_single_union_type.to_reference()
                    internal_single_union_types.append(internal_single_union_type)

                    discriminant_field = self._get_discriminant_field_for_single_union_type(
                        single_union_type=single_union_type
                    )

                    internal_pydantic_model_for_single_union_type.add_field(discriminant_field)

                    if shape.properties_type == "singleProperty":
                        internal_pydantic_model_for_single_union_type.add_field(
                            PydanticField(
                                name=shape.name.snake_case,
                                json_field_name=shape.name.wire_value,
                                type_hint=self._context.get_type_hint_for_type_reference(type_reference=shape.type),
                            )
                        )

                    factory_declaration.add_method(
                        AST.FunctionDeclaration(
                            name=single_union_type.discriminant_value.snake_case,
                            parameters=single_union_type.shape.visit(
                                same_properties_as_object=lambda type_name: [
                                    AST.FunctionParameter(
                                        name=BUILDER_ARGUMENT_NAME,
                                        type_hint=self._context.get_type_hint_for_type_reference(
                                            ir_types.TypeReference.factory.named(type_name)
                                        ),
                                    )
                                ],
                                single_property=lambda property: [
                                    AST.FunctionParameter(
                                        name=BUILDER_ARGUMENT_NAME,
                                        type_hint=self._context.get_type_hint_for_type_reference(property.type),
                                    )
                                ],
                                no_properties=lambda: [],
                            ),
                            return_type=self._context.get_type_hint_for_type_reference(
                                ir_types.TypeReference.factory.named(self._name)
                            ),
                            body=AST.CodeWriter(
                                self._create_body_writer(
                                    single_union_type=single_union_type,
                                    internal_single_union_type=internal_single_union_type,
                                    external_union=external_pydantic_model.to_reference(),
                                    discriminant_attr_name=discriminant_field.name,
                                )
                            ),
                        ),
                    )

            root_type = AST.TypeHint.union(
                *(
                    AST.TypeHint(type=internal_single_union_type)
                    for internal_single_union_type in internal_single_union_types
                ),
            )

            external_pydantic_model.add_method_unsafe(
                AST.FunctionDeclaration(
                    name="get_as_union",
                    parameters=[],
                    return_type=root_type,
                    body=AST.CodeWriter("return self.__root__"),
                )
            )

            external_pydantic_model.add_method_unsafe(
                get_visit_method(
                    items=[
                        VisitableItem(
                            parameter_name=single_union_type.discriminant_value.snake_case,
                            expected_value=single_union_type.discriminant_value.wire_value,
                            visitor_argument=single_union_type.shape.visit(
                                same_properties_as_object=lambda type_name: VisitorArgument(
                                    expression=AST.Expression("self.__root__"),
                                    type=external_pydantic_model.get_type_hint_for_type_reference(
                                        ir_types.TypeReference.factory.named(type_name)
                                    ),
                                ),
                                single_property=lambda property: VisitorArgument(
                                    expression=AST.Expression(
                                        f"self.__root__.{single_union_type.discriminant_value.snake_case}"
                                    ),
                                    type=external_pydantic_model.get_type_hint_for_type_reference(property.type),
                                ),
                                no_properties=lambda: None,
                            ),
                        )
                        for single_union_type in self._union.types
                    ],
                    reference_to_current_value=f"self.__root__.{self._get_discriminant_attr_name()}",
                    are_checks_exhaustive=True,
                )
            )

            external_pydantic_model.set_root_type_unsafe(
                is_forward_ref=True,
                root_type=AST.TypeHint.annotated(
                    type=root_type,
                    annotation=AST.Expression(
                        AST.FunctionInvocation(
                            function_definition=PYDANTIC_FIELD_REFERENCE,
                            kwargs=[
                                (
                                    "discriminator",
                                    AST.Expression(
                                        f'"{self._get_discriminant_attr_name()}"',
                                    ),
                                )
                            ],
                        )
                    ),
                ),
            )

    def _create_body_writer(
        self,
        single_union_type: ir_types.SingleUnionType,
        internal_single_union_type: AST.ClassReference,
        external_union: AST.ClassReference,
        discriminant_attr_name: str,
    ) -> AST.ReferencingCodeWriter:
        def write(writer: AST.NodeWriter, reference_resolver: AST.ReferenceResolver) -> None:
            # explicit typing needed to help mypy
            no_expressions: List[AST.Expression] = []

            internal_single_union_type_instantiation = AST.ClassInstantiation(
                class_=internal_single_union_type,
                args=single_union_type.shape.visit(
                    same_properties_as_object=lambda type_name: [
                        AST.Expression(
                            AST.FunctionInvocation(
                                function_definition=AST.Reference(qualified_name_excluding_import=("dict",)),
                                args=[AST.Expression(BUILDER_ARGUMENT_NAME)],
                            ),
                            spread=AST.ExpressionSpread.TWO_ASTERISKS,
                        )
                    ],
                    single_property=lambda property: no_expressions,
                    no_properties=lambda: no_expressions,
                ),
                kwargs=[(discriminant_attr_name, self._get_discriminant_value_for_single_union_type(single_union_type))]
                + single_union_type.shape.visit(
                    same_properties_as_object=lambda type_name: [],
                    single_property=lambda property: [
                        (property.name.snake_case, AST.Expression(BUILDER_ARGUMENT_NAME))
                    ],
                    no_properties=lambda: [],
                ),
            )

            sub_union_instantiation = AST.ClassInstantiation(
                class_=external_union,
                kwargs=[("__root__", AST.Expression(internal_single_union_type_instantiation))],
            )

            writer.write("return ")
            writer.write_node(sub_union_instantiation)

        return write

    def _get_discriminant_field_for_single_union_type(
        self, single_union_type: ir_types.SingleUnionType
    ) -> PydanticField:
        return PydanticField(
            name=self._get_discriminant_attr_name(),
            type_hint=AST.TypeHint.literal(self._get_discriminant_value_for_single_union_type(single_union_type)),
            json_field_name=self._union.discriminant_v_2.wire_value,
        )

    def _get_discriminant_attr_name(self) -> str:
        return self._union.discriminant_v_2.snake_case

    def _get_discriminant_value_for_single_union_type(
        self,
        single_union_type: ir_types.SingleUnionType,
    ) -> AST.Expression:
        return AST.Expression(f'"{single_union_type.discriminant_value.wire_value}"')


def assert_never(arg: Never) -> Never:
    raise AssertionError("Expected code to be unreachable")