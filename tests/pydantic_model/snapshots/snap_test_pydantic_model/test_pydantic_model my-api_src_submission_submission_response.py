from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.problem_id import ProblemId
from .code_execution_update import CodeExecutionUpdate
from .exception_info import ExceptionInfo
from .terminated_response import TerminatedResponse

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def server_initialized(self) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.ServerInitialized(type="serverInitialized"))

    def problem_initialized(self, value: ProblemId) -> SubmissionResponse:
        return SubmissionResponse(
            __root__=_SubmissionResponse.ProblemInitialized(type="problemInitialized", problem_initialized=value)
        )

    def workspace_initialized(self) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.WorkspaceInitialized(type="workspaceInitialized"))

    def server_errored(self, value: ExceptionInfo) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.ServerErrored(**dict(value), type="serverErrored"))

    def code_execution_update(self, value: CodeExecutionUpdate) -> SubmissionResponse:
        return SubmissionResponse(
            __root__=_SubmissionResponse.CodeExecutionUpdate(type="codeExecutionUpdate", code_execution_update=value)
        )

    def terminated(self, value: TerminatedResponse) -> SubmissionResponse:
        return SubmissionResponse(__root__=_SubmissionResponse.Terminated(**dict(value), type="terminated"))


class SubmissionResponse(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get(
        self,
    ) -> typing.Union[
        _SubmissionResponse.ServerInitialized,
        _SubmissionResponse.ProblemInitialized,
        _SubmissionResponse.WorkspaceInitialized,
        _SubmissionResponse.ServerErrored,
        _SubmissionResponse.CodeExecutionUpdate,
        _SubmissionResponse.Terminated,
    ]:
        return self.__root__

    def visit(
        self,
        server_initialized: typing.Callable[[], T_Result],
        problem_initialized: typing.Callable[[ProblemId], T_Result],
        workspace_initialized: typing.Callable[[], T_Result],
        server_errored: typing.Callable[[ExceptionInfo], T_Result],
        code_execution_update: typing.Callable[[CodeExecutionUpdate], T_Result],
        terminated: typing.Callable[[TerminatedResponse], T_Result],
    ) -> T_Result:
        if self.__root__.type == "serverInitialized":
            return server_initialized()
        if self.__root__.type == "problemInitialized":
            return problem_initialized(self.__root__.problem_initialized)
        if self.__root__.type == "workspaceInitialized":
            return workspace_initialized()
        if self.__root__.type == "serverErrored":
            return server_errored(self.__root__)
        if self.__root__.type == "codeExecutionUpdate":
            return code_execution_update(self.__root__.code_execution_update)
        if self.__root__.type == "terminated":
            return terminated(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _SubmissionResponse.ServerInitialized,
            _SubmissionResponse.ProblemInitialized,
            _SubmissionResponse.WorkspaceInitialized,
            _SubmissionResponse.ServerErrored,
            _SubmissionResponse.CodeExecutionUpdate,
            _SubmissionResponse.Terminated,
        ],
        pydantic.Field(discriminator="type"),
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)


class _SubmissionResponse:
    class ServerInitialized(pydantic.BaseModel):
        type: typing_extensions.Literal["serverInitialized"]

    class ProblemInitialized(pydantic.BaseModel):
        type: typing_extensions.Literal["problemInitialized"]
        problem_initialized: ProblemId = pydantic.Field(alias="problemInitialized")

        class Config:
            allow_population_by_field_name = True

    class WorkspaceInitialized(pydantic.BaseModel):
        type: typing_extensions.Literal["workspaceInitialized"]

    class ServerErrored(ExceptionInfo):
        type: typing_extensions.Literal["serverErrored"]

    class CodeExecutionUpdate(pydantic.BaseModel):
        type: typing_extensions.Literal["codeExecutionUpdate"]
        code_execution_update: CodeExecutionUpdate = pydantic.Field(alias="codeExecutionUpdate")

        class Config:
            allow_population_by_field_name = True

    class Terminated(TerminatedResponse):
        type: typing_extensions.Literal["terminated"]


SubmissionResponse.update_forward_refs()
