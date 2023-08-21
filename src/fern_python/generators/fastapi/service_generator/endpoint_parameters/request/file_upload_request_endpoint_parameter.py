import fern.ir.resources as ir_types
from fern_python.codegen import AST
from ....context import FastApiGeneratorContext
from .referenced_request_endpoint_parameter import ReferencedRequestEndpointParameter
from .request_endpoint_parameter import RequestEndpointParameter


class FileUploadRequestEndpointParameter(RequestEndpointParameter):
    def __init__(self, context: FastApiGeneratorContext, property: ir_types.FileProperty):
        super().__init__(context=context)
        self._property = property

    def get_name(self) -> str:
        return self._property.key.name.original_name

    def _get_unsafe_name(self) -> str:
        return self._property.key.name.original_name

    def get_type(self) -> AST.TypeHint:
        return self._context.pydantic_generator_context.get_type_hint_for_file_upload()


def get_file_upload_request_parameters(
    context: FastApiGeneratorContext, request: ir_types.FileUploadRequest
) -> list[RequestEndpointParameter]:
    return list(
        map(
            lambda property: property.visit(
                file=lambda prop: FileUploadRequestEndpointParameter(context=context, property=prop),
                body_property=lambda prop: ReferencedRequestEndpointParameter(
                    context=context, request_type=prop.value_type
                ),
            ),
            request.properties,
        )
    )
