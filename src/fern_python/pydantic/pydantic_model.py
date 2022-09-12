from typing import Union

from ..codegen import AST


def get_reference_to_pydantic_export(export: str) -> AST.ClassReference:
    return AST.ClassReference(
        module=("pydantic",),
        name_inside_import=(export,),
        from_module=AST.Dependency(name="pydantic", version="^1.9.2"),
    )


PYDANTIC_BASE_MODEL_REFERENCE = get_reference_to_pydantic_export("BaseModel")
PYDANTIC_FIELD_REFERENCE = get_reference_to_pydantic_export("Field")


class PydanticModel:
    _class_declaration: AST.ClassDeclaration
    _has_aliases: bool = False

    def __init__(self, name: str):
        self._class_declaration = AST.ClassDeclaration(
            name=name,
            extends=[PYDANTIC_BASE_MODEL_REFERENCE],
        )

    def add_field(self, name: str, type_hint: AST.TypeHint, json_field_name: str = None) -> None:
        initializer = (
            get_initializer(json_field_name=json_field_name)
            if json_field_name is not None and json_field_name != name
            else None
        )

        if initializer is not None:
            self._has_aliases = True

        self._class_declaration.add_attribute(
            AST.VariableDeclaration(name=name, type_hint=type_hint, initializer=initializer)
        )

    def finish(self) -> AST.ClassDeclaration:
        if self._has_aliases:
            config = AST.ClassDeclaration(name="Config")
            config.add_attribute(
                AST.VariableDeclaration(
                    name="allow_population_by_field_name",
                    initializer=AST.CodeWriter("True"),
                )
            )
            self._class_declaration.add_class(declaration=config)
        return self._class_declaration


def get_initializer(json_field_name: str) -> Union[AST.CodeWriter, None]:
    class Initializer(AST.ReferencingCodeWriter):
        def write(self, reference_resolver: AST.ReferenceResolver) -> str:
            return f'{reference_resolver.resolve_reference(PYDANTIC_FIELD_REFERENCE)}(alias="{json_field_name}")'

    return AST.CodeWriter(Initializer())
