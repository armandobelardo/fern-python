# This file was auto-generated by Fern from our API Definition.

import typing

from ...submission.types.trace_response import TraceResponse
from ...submission.types.workspace_run_details import WorkspaceRunDetails

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class StoreTracedWorkspaceRequest(pydantic.BaseModel):
    workspace_run_details: WorkspaceRunDetails = pydantic.Field(alias="workspaceRunDetails")
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
