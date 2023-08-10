import fern.ir.resources as ir_types

from fern_python.codegen import AST

from ....context import FastApiGeneratorContext
from .request_endpoint_parameter import RequestEndpointParameter


class FileUploadRequestEndpointParameter(RequestEndpointParameter):
    def __init__(self, context: FastApiGeneratorContext):
        super().__init__(context=context)

    def get_type(self) -> AST.TypeHint:
        return self._context.pydantic_generator_context.get_type_hint_for_file_upload()
