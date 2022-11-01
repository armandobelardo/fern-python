# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .workspace_submission_status import WorkspaceSubmissionStatus


class WorkspaceSubmissionState(pydantic.BaseModel):
    status: WorkspaceSubmissionStatus

    class Partial(typing_extensions.TypedDict):
        status: typing_extensions.NotRequired[WorkspaceSubmissionStatus]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceSubmissionState.Validators.root
            def validate(values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionState.Partial:
                ...

            @WorkspaceSubmissionState.Validators.field("status")
            def validate_status(status: WorkspaceSubmissionStatus, values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionStatus:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[WorkspaceSubmissionState.Partial], WorkspaceSubmissionState.Partial]]
        ] = []
        _status_validators: typing.ClassVar[typing.List[WorkspaceSubmissionState.Validators.StatusValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[WorkspaceSubmissionState.Partial], WorkspaceSubmissionState.Partial]
        ) -> typing.Callable[[WorkspaceSubmissionState.Partial], WorkspaceSubmissionState.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"]
        ) -> typing.Callable[
            [WorkspaceSubmissionState.Validators.StatusValidator], WorkspaceSubmissionState.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "status":
                    cls._status_validators.append(validator)
                return validator

            return decorator

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, *, status: WorkspaceSubmissionStatus, values: WorkspaceSubmissionState.Partial
            ) -> WorkspaceSubmissionStatus:
                ...

    @pydantic.root_validator
    def _validate(cls, values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionState.Partial:
        for validator in WorkspaceSubmissionState.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("status")
    def _validate_status(
        cls, status: WorkspaceSubmissionStatus, values: WorkspaceSubmissionState.Partial
    ) -> WorkspaceSubmissionStatus:
        for validator in WorkspaceSubmissionState.Validators._status_validators:
            status = validator(status, values=values)
        return status

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
