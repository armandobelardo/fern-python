from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_submission_state import TestSubmissionState
from .workspace_submission_state import WorkspaceSubmissionState

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def test(self, value: TestSubmissionState) -> SubmissionTypeState:
        return SubmissionTypeState(__root__=_SubmissionTypeState.Test(**dict(value), type="test"))

    def workspace(self, value: WorkspaceSubmissionState) -> SubmissionTypeState:
        return SubmissionTypeState(__root__=_SubmissionTypeState.Workspace(**dict(value), type="workspace"))


class SubmissionTypeState(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]:
        return self.__root__

    def visit(
        self,
        test: typing.Callable[[TestSubmissionState], T_Result],
        workspace: typing.Callable[[WorkspaceSubmissionState], T_Result],
    ) -> T_Result:
        if self.__root__.type == "test":
            return test(self.__root__)
        if self.__root__.type == "workspace":
            return workspace(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace], pydantic.Field(discriminator="type")
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace], values.get("__root__")
        )
        for validator in SubmissionTypeState.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]],
                    typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]],
                typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace],
            ],
        ) -> None:
            cls._validators.append(validator)

    class Config:
        frozen = True


class _SubmissionTypeState:
    class Test(TestSubmissionState):
        type: typing_extensions.Literal["test"]

        class Config:
            frozen = True

    class Workspace(WorkspaceSubmissionState):
        type: typing_extensions.Literal["workspace"]

        class Config:
            frozen = True


SubmissionTypeState.update_forward_refs()
