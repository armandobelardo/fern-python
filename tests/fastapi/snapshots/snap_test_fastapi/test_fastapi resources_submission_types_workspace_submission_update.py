# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .workspace_submission_update_info import WorkspaceSubmissionUpdateInfo


class WorkspaceSubmissionUpdate(pydantic.BaseModel):
    update_time: str = pydantic.Field(alias="updateTime")
    update_info: WorkspaceSubmissionUpdateInfo = pydantic.Field(alias="updateInfo")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceSubmissionUpdate.Validators.root
            def validate(values: WorkspaceSubmissionUpdate.Partial) -> WorkspaceSubmissionUpdate.Partial:
                ...

            @WorkspaceSubmissionUpdate.Validators.field("update_time")
            def validate_update_time(v: str, values: WorkspaceSubmissionUpdate.Partial) -> str:
                ...

            @WorkspaceSubmissionUpdate.Validators.field("update_info")
            def validate_update_info(v: WorkspaceSubmissionUpdateInfo, values: WorkspaceSubmissionUpdate.Partial) -> WorkspaceSubmissionUpdateInfo:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[WorkspaceSubmissionUpdate.Partial], WorkspaceSubmissionUpdate.Partial]]
        ] = []
        _update_time_validators: typing.ClassVar[
            typing.List[WorkspaceSubmissionUpdate.Validators.UpdateTimeValidator]
        ] = []
        _update_info_validators: typing.ClassVar[
            typing.List[WorkspaceSubmissionUpdate.Validators.UpdateInfoValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[WorkspaceSubmissionUpdate.Partial], WorkspaceSubmissionUpdate.Partial]
        ) -> typing.Callable[[WorkspaceSubmissionUpdate.Partial], WorkspaceSubmissionUpdate.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["update_time"]
        ) -> typing.Callable[
            [WorkspaceSubmissionUpdate.Validators.UpdateTimeValidator],
            WorkspaceSubmissionUpdate.Validators.UpdateTimeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["update_info"]
        ) -> typing.Callable[
            [WorkspaceSubmissionUpdate.Validators.UpdateInfoValidator],
            WorkspaceSubmissionUpdate.Validators.UpdateInfoValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "update_time":
                    cls._update_time_validators.append(validator)
                if field_name == "update_info":
                    cls._update_info_validators.append(validator)
                return validator

            return decorator

        class UpdateTimeValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: WorkspaceSubmissionUpdate.Partial) -> str:
                ...

        class UpdateInfoValidator(typing_extensions.Protocol):
            def __call__(
                self, v: WorkspaceSubmissionUpdateInfo, *, values: WorkspaceSubmissionUpdate.Partial
            ) -> WorkspaceSubmissionUpdateInfo:
                ...

    @pydantic.root_validator
    def _validate(cls, values: WorkspaceSubmissionUpdate.Partial) -> WorkspaceSubmissionUpdate.Partial:
        for validator in WorkspaceSubmissionUpdate.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("update_time")
    def _validate_update_time(cls, v: str, values: WorkspaceSubmissionUpdate.Partial) -> str:
        for validator in WorkspaceSubmissionUpdate.Validators._update_time_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("update_info")
    def _validate_update_info(
        cls, v: WorkspaceSubmissionUpdateInfo, values: WorkspaceSubmissionUpdate.Partial
    ) -> WorkspaceSubmissionUpdateInfo:
        for validator in WorkspaceSubmissionUpdate.Validators._update_info_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        update_time: typing_extensions.NotRequired[str]
        update_info: typing_extensions.NotRequired[WorkspaceSubmissionUpdateInfo]

    class Config:
        frozen = True
        allow_population_by_field_name = True
