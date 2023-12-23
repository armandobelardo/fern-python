# This file was auto-generated by Fern from our API Definition.

from ...core.api_error import ApiError
from .object_with_required_field import ObjectWithRequiredField


class ObjectWithRequiredFieldError(ApiError):
    def __init__(self, body: ObjectWithRequiredField):
        super().__init__(status_code=400, body=body)
