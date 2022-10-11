from abc import ABC, abstractmethod

from fern_python.codegen import AST
from fern_python.pydantic_codegen import PydanticModel


class ValidatorGenerator(ABC):
    def __init__(self, model: PydanticModel, reference_to_validators_class: AST.ClassReference):
        self._model = model
        self._reference_to_validators_class = reference_to_validators_class

    @abstractmethod
    def add_validator_to_model(self) -> None:
        ...
