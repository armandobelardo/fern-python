# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .error_info import ErrorInfo
from .running_submission_state import RunningSubmissionState
from .workspace_run_details import WorkspaceRunDetails

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class WorkspaceSubmissionStatus_Stopped(pydantic.BaseModel):
    type: typing_extensions.Literal["stopped"]


class WorkspaceSubmissionStatus_Errored(pydantic.BaseModel):
    type: typing_extensions.Literal["errored"]
    value: ErrorInfo


class WorkspaceSubmissionStatus_Running(pydantic.BaseModel):
    type: typing_extensions.Literal["running"]
    value: RunningSubmissionState


class WorkspaceSubmissionStatus_Ran(WorkspaceRunDetails):
    type: typing_extensions.Literal["ran"]

    class Config:
        allow_population_by_field_name = True


class WorkspaceSubmissionStatus_Traced(WorkspaceRunDetails):
    type: typing_extensions.Literal["traced"]

    class Config:
        allow_population_by_field_name = True


WorkspaceSubmissionStatus = typing.Union[
    WorkspaceSubmissionStatus_Stopped,
    WorkspaceSubmissionStatus_Errored,
    WorkspaceSubmissionStatus_Running,
    WorkspaceSubmissionStatus_Ran,
    WorkspaceSubmissionStatus_Traced,
]
