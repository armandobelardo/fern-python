# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.language import Language
from .execution_session_status import ExecutionSessionStatus


class ExecutionSessionState(pydantic.BaseModel):
    last_time_contacted: typing.Optional[str] = pydantic.Field(alias="lastTimeContacted")
    session_id: str = pydantic.Field(alias="sessionId")
    is_warm_instance: bool = pydantic.Field(alias="isWarmInstance")
    aws_task_id: typing.Optional[str] = pydantic.Field(alias="awsTaskId")
    language: Language
    status: ExecutionSessionStatus

    class Partial(typing_extensions.TypedDict):
        last_time_contacted: typing_extensions.NotRequired[typing.Optional[str]]
        session_id: typing_extensions.NotRequired[str]
        is_warm_instance: typing_extensions.NotRequired[bool]
        aws_task_id: typing_extensions.NotRequired[typing.Optional[str]]
        language: typing_extensions.NotRequired[Language]
        status: typing_extensions.NotRequired[ExecutionSessionStatus]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ExecutionSessionState.Validators.root
            def validate(values: ExecutionSessionState.Partial) -> ExecutionSessionState.Partial:
                ...

            @ExecutionSessionState.Validators.field("last_time_contacted")
            def validate_last_time_contacted(v: typing.Optional[str], values: ExecutionSessionState.Partial) -> typing.Optional[str]:
                ...

            @ExecutionSessionState.Validators.field("session_id")
            def validate_session_id(v: str, values: ExecutionSessionState.Partial) -> str:
                ...

            @ExecutionSessionState.Validators.field("is_warm_instance")
            def validate_is_warm_instance(v: bool, values: ExecutionSessionState.Partial) -> bool:
                ...

            @ExecutionSessionState.Validators.field("aws_task_id")
            def validate_aws_task_id(v: typing.Optional[str], values: ExecutionSessionState.Partial) -> typing.Optional[str]:
                ...

            @ExecutionSessionState.Validators.field("language")
            def validate_language(v: Language, values: ExecutionSessionState.Partial) -> Language:
                ...

            @ExecutionSessionState.Validators.field("status")
            def validate_status(v: ExecutionSessionStatus, values: ExecutionSessionState.Partial) -> ExecutionSessionStatus:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[ExecutionSessionState.Partial], ExecutionSessionState.Partial]]
        ] = []
        _last_time_contacted_validators: typing.ClassVar[
            typing.List[ExecutionSessionState.Validators.LastTimeContactedValidator]
        ] = []
        _session_id_validators: typing.ClassVar[typing.List[ExecutionSessionState.Validators.SessionIdValidator]] = []
        _is_warm_instance_validators: typing.ClassVar[
            typing.List[ExecutionSessionState.Validators.IsWarmInstanceValidator]
        ] = []
        _aws_task_id_validators: typing.ClassVar[typing.List[ExecutionSessionState.Validators.AwsTaskIdValidator]] = []
        _language_validators: typing.ClassVar[typing.List[ExecutionSessionState.Validators.LanguageValidator]] = []
        _status_validators: typing.ClassVar[typing.List[ExecutionSessionState.Validators.StatusValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[ExecutionSessionState.Partial], ExecutionSessionState.Partial]
        ) -> typing.Callable[[ExecutionSessionState.Partial], ExecutionSessionState.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["last_time_contacted"]
        ) -> typing.Callable[
            [ExecutionSessionState.Validators.LastTimeContactedValidator],
            ExecutionSessionState.Validators.LastTimeContactedValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["session_id"]
        ) -> typing.Callable[
            [ExecutionSessionState.Validators.SessionIdValidator], ExecutionSessionState.Validators.SessionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_warm_instance"]
        ) -> typing.Callable[
            [ExecutionSessionState.Validators.IsWarmInstanceValidator],
            ExecutionSessionState.Validators.IsWarmInstanceValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["aws_task_id"]
        ) -> typing.Callable[
            [ExecutionSessionState.Validators.AwsTaskIdValidator], ExecutionSessionState.Validators.AwsTaskIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"]
        ) -> typing.Callable[
            [ExecutionSessionState.Validators.LanguageValidator], ExecutionSessionState.Validators.LanguageValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"]
        ) -> typing.Callable[
            [ExecutionSessionState.Validators.StatusValidator], ExecutionSessionState.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "last_time_contacted":
                    cls._last_time_contacted_validators.append(validator)
                if field_name == "session_id":
                    cls._session_id_validators.append(validator)
                if field_name == "is_warm_instance":
                    cls._is_warm_instance_validators.append(validator)
                if field_name == "aws_task_id":
                    cls._aws_task_id_validators.append(validator)
                if field_name == "language":
                    cls._language_validators.append(validator)
                if field_name == "status":
                    cls._status_validators.append(validator)
                return validator

            return decorator

        class LastTimeContactedValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[str], *, values: ExecutionSessionState.Partial
            ) -> typing.Optional[str]:
                ...

        class SessionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: ExecutionSessionState.Partial) -> str:
                ...

        class IsWarmInstanceValidator(typing_extensions.Protocol):
            def __call__(self, v: bool, *, values: ExecutionSessionState.Partial) -> bool:
                ...

        class AwsTaskIdValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[str], *, values: ExecutionSessionState.Partial
            ) -> typing.Optional[str]:
                ...

        class LanguageValidator(typing_extensions.Protocol):
            def __call__(self, v: Language, *, values: ExecutionSessionState.Partial) -> Language:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, v: ExecutionSessionStatus, *, values: ExecutionSessionState.Partial
            ) -> ExecutionSessionStatus:
                ...

    @pydantic.root_validator
    def _validate(cls, values: ExecutionSessionState.Partial) -> ExecutionSessionState.Partial:
        for validator in ExecutionSessionState.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("last_time_contacted")
    def _validate_last_time_contacted(
        cls, v: typing.Optional[str], values: ExecutionSessionState.Partial
    ) -> typing.Optional[str]:
        for validator in ExecutionSessionState.Validators._last_time_contacted_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("session_id")
    def _validate_session_id(cls, v: str, values: ExecutionSessionState.Partial) -> str:
        for validator in ExecutionSessionState.Validators._session_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("is_warm_instance")
    def _validate_is_warm_instance(cls, v: bool, values: ExecutionSessionState.Partial) -> bool:
        for validator in ExecutionSessionState.Validators._is_warm_instance_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("aws_task_id")
    def _validate_aws_task_id(
        cls, v: typing.Optional[str], values: ExecutionSessionState.Partial
    ) -> typing.Optional[str]:
        for validator in ExecutionSessionState.Validators._aws_task_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("language")
    def _validate_language(cls, v: Language, values: ExecutionSessionState.Partial) -> Language:
        for validator in ExecutionSessionState.Validators._language_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("status")
    def _validate_status(
        cls, v: ExecutionSessionStatus, values: ExecutionSessionState.Partial
    ) -> ExecutionSessionStatus:
        for validator in ExecutionSessionState.Validators._status_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
