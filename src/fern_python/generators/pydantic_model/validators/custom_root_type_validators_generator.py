from typing import Sequence

from fern_python.codegen import AST
from fern_python.pydantic_codegen import PydanticModel

from .validator_generators import CustomRootTypeValidatorGenerator, ValidatorGenerator
from .validators_generator import ValidatorsGenerator


class CustomRootTypeValidatorsGenerator(ValidatorsGenerator):
    def __init__(self, root_type: AST.TypeHint, model: PydanticModel):
        super().__init__(model=model)
        self._root_type = root_type
        self._root_type_generator = CustomRootTypeValidatorGenerator(
            root_type=root_type,
            model=model,
            reference_to_validators_class=self._get_reference_to_validators_class(),
        )

    def _populate_validators_class(self, validators_class: AST.ClassDeclaration) -> None:
        self._root_type_generator.add_to_validators_class(validators_class)

    def _get_validator_generators(self) -> Sequence[ValidatorGenerator]:
        return [self._root_type_generator]
