from abc import ABC, abstractmethod

import fern.resources.ir as ir_types
from fern.generator_exec.sdk.resources import GeneratorConfig

from fern_python.codegen import AST, Filepath
from fern_python.generators.pydantic_model import PydanticGeneratorContextImpl

from ..core_utilities import CoreUtilities
from ..declaration_referencers import TypeDeclarationReferencer
from ..fastapi_filepath_creator import FastApiFilepathCreator


class FastApiGeneratorContext(ABC):
    def __init__(
        self,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
    ):
        self.ir = ir
        self.generator_config = generator_config
        self.filepath_creator = FastApiFilepathCreator(ir=ir, generator_config=generator_config)
        self.pydantic_generator_context = PydanticGeneratorContextImpl(
            ir=ir,
            type_declaration_referencer=TypeDeclarationReferencer(filepath_creator=self.filepath_creator),
            generator_config=generator_config,
            filepath_creator=self.filepath_creator,
        )
        self.core_utilities = CoreUtilities(filepath_creator=self.filepath_creator)

    @abstractmethod
    def get_filepath_for_service(self, service_name: ir_types.DeclaredServiceName) -> Filepath:
        ...

    @abstractmethod
    def get_class_name_for_service(self, service_name: ir_types.DeclaredServiceName) -> str:
        ...

    @abstractmethod
    def get_reference_to_service(self, service_name: ir_types.DeclaredServiceName) -> AST.ClassReference:
        ...

    @abstractmethod
    def get_filepath_for_inlined_request(
        self, service_name: ir_types.DeclaredServiceName, request: ir_types.InlinedRequestBody
    ) -> Filepath:
        ...

    @abstractmethod
    def get_class_name_for_inlined_request(
        self, service_name: ir_types.DeclaredServiceName, request: ir_types.InlinedRequestBody
    ) -> str:
        ...

    @abstractmethod
    def get_reference_to_inlined_request(
        self, service_name: ir_types.DeclaredServiceName, request: ir_types.InlinedRequestBody
    ) -> AST.ClassReference:
        ...

    @abstractmethod
    def get_filepath_for_error(self, error_name: ir_types.DeclaredErrorName) -> Filepath:
        ...

    @abstractmethod
    def get_class_name_for_error(self, error_name: ir_types.DeclaredErrorName) -> str:
        ...

    @abstractmethod
    def get_reference_to_error(self, error_name: ir_types.DeclaredErrorName) -> AST.ClassReference:
        ...
