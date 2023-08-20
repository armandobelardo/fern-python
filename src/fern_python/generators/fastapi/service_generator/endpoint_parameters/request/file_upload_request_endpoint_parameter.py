from typing import override

import fern.ir.resources as ir_types

from ....context import FastApiGeneratorContext
from .inlined_request_endpoint_parameter import InlinedRequestEndpointParameter
from .request_endpoint_parameter import RequestEndpointParameter


class FileUploadRequestEndpointParameter(RequestEndpointParameter):
    def __init__(self, context: FastApiGeneratorContext, property: ir_types.FileProperty):
        super().__init__(context=context)
        self._property = property

    @override
    def get_name(self) -> str:
        return self._property.key

    @override
    def _get_unsafe_name(self) -> str:
        return self._property.key

    def get_type(self) -> list[RequestEndpointParameter]:
        return self._context.pydantic_generator_context.get_type_hint_for_file_upload()


def get_file_upload_request_parameters(
    context: FastApiGeneratorContext, request: ir_types.FileUploadRequest
) -> list[RequestEndpointParameter]:
    return map(
        lambda property: property.visit(
            file=lambda prop: FileUploadRequestEndpointParameter(context=context, property=prop),
            body_property=lambda prop: InlinedRequestEndpointParameter(
                context=context, service_name=prop, request=request
            ),
        ),
        request.properties,
    )
