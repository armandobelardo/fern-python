# This file was auto-generated by Fern from our API Definition.

from ..core.api_error import ApiError
from .unauthorized_request_error_body import UnauthorizedRequestErrorBody


class UnauthorizedRequest(ApiError):
    def __init__(self, body: UnauthorizedRequestErrorBody):
        super().__init__(status_code=401, body=body)
