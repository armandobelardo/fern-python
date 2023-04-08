# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class ExceptionInfo(pydantic.BaseModel):
    exception_type: str = pydantic.Field(alias="exceptionType")
    exception_message: str = pydantic.Field(alias="exceptionMessage")
    exception_stacktrace: str = pydantic.Field(alias="exceptionStacktrace")

    class Partial(typing_extensions.TypedDict):
        exception_type: typing_extensions.NotRequired[str]
        exception_message: typing_extensions.NotRequired[str]
        exception_stacktrace: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ExceptionInfo.Validators.root()
            def validate(values: ExceptionInfo.Partial) -> ExceptionInfo.Partial:
                ...

            @ExceptionInfo.Validators.field("exception_type")
            def validate_exception_type(exception_type: str, values: ExceptionInfo.Partial) -> str:
                ...

            @ExceptionInfo.Validators.field("exception_message")
            def validate_exception_message(exception_message: str, values: ExceptionInfo.Partial) -> str:
                ...

            @ExceptionInfo.Validators.field("exception_stacktrace")
            def validate_exception_stacktrace(exception_stacktrace: str, values: ExceptionInfo.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ExceptionInfo.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ExceptionInfo.Validators._RootValidator]] = []
        _exception_type_pre_validators: typing.ClassVar[
            typing.List[ExceptionInfo.Validators.PreExceptionTypeValidator]
        ] = []
        _exception_type_post_validators: typing.ClassVar[
            typing.List[ExceptionInfo.Validators.ExceptionTypeValidator]
        ] = []
        _exception_message_pre_validators: typing.ClassVar[
            typing.List[ExceptionInfo.Validators.PreExceptionMessageValidator]
        ] = []
        _exception_message_post_validators: typing.ClassVar[
            typing.List[ExceptionInfo.Validators.ExceptionMessageValidator]
        ] = []
        _exception_stacktrace_pre_validators: typing.ClassVar[
            typing.List[ExceptionInfo.Validators.PreExceptionStacktraceValidator]
        ] = []
        _exception_stacktrace_post_validators: typing.ClassVar[
            typing.List[ExceptionInfo.Validators.ExceptionStacktraceValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ExceptionInfo.Validators._RootValidator], ExceptionInfo.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ExceptionInfo.Validators._PreRootValidator], ExceptionInfo.Validators._PreRootValidator]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExceptionInfo.Validators.PreExceptionTypeValidator], ExceptionInfo.Validators.PreExceptionTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["exception_type"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ExceptionInfo.Validators.ExceptionTypeValidator], ExceptionInfo.Validators.ExceptionTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception_message"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExceptionInfo.Validators.PreExceptionMessageValidator],
            ExceptionInfo.Validators.PreExceptionMessageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["exception_message"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ExceptionInfo.Validators.ExceptionMessageValidator], ExceptionInfo.Validators.ExceptionMessageValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception_stacktrace"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExceptionInfo.Validators.PreExceptionStacktraceValidator],
            ExceptionInfo.Validators.PreExceptionStacktraceValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["exception_stacktrace"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ExceptionInfo.Validators.ExceptionStacktraceValidator],
            ExceptionInfo.Validators.ExceptionStacktraceValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "exception_type":
                    if pre:
                        cls._exception_type_pre_validators.append(validator)
                    else:
                        cls._exception_type_post_validators.append(validator)
                if field_name == "exception_message":
                    if pre:
                        cls._exception_message_pre_validators.append(validator)
                    else:
                        cls._exception_message_post_validators.append(validator)
                if field_name == "exception_stacktrace":
                    if pre:
                        cls._exception_stacktrace_pre_validators.append(validator)
                    else:
                        cls._exception_stacktrace_post_validators.append(validator)
                return validator

            return decorator

        class PreExceptionTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExceptionInfo.Partial) -> typing.Any:
                ...

        class ExceptionTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: ExceptionInfo.Partial) -> str:
                ...

        class PreExceptionMessageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExceptionInfo.Partial) -> typing.Any:
                ...

        class ExceptionMessageValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: ExceptionInfo.Partial) -> str:
                ...

        class PreExceptionStacktraceValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExceptionInfo.Partial) -> typing.Any:
                ...

        class ExceptionStacktraceValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: ExceptionInfo.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ExceptionInfo.Partial) -> ExceptionInfo.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: ExceptionInfo.Partial) -> ExceptionInfo.Partial:
        for validator in ExceptionInfo.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: ExceptionInfo.Partial) -> ExceptionInfo.Partial:
        for validator in ExceptionInfo.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("exception_type", pre=True)
    def _pre_validate_exception_type(cls, v: str, values: ExceptionInfo.Partial) -> str:
        for validator in ExceptionInfo.Validators._exception_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception_type", pre=False)
    def _post_validate_exception_type(cls, v: str, values: ExceptionInfo.Partial) -> str:
        for validator in ExceptionInfo.Validators._exception_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception_message", pre=True)
    def _pre_validate_exception_message(cls, v: str, values: ExceptionInfo.Partial) -> str:
        for validator in ExceptionInfo.Validators._exception_message_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception_message", pre=False)
    def _post_validate_exception_message(cls, v: str, values: ExceptionInfo.Partial) -> str:
        for validator in ExceptionInfo.Validators._exception_message_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception_stacktrace", pre=True)
    def _pre_validate_exception_stacktrace(cls, v: str, values: ExceptionInfo.Partial) -> str:
        for validator in ExceptionInfo.Validators._exception_stacktrace_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception_stacktrace", pre=False)
    def _post_validate_exception_stacktrace(cls, v: str, values: ExceptionInfo.Partial) -> str:
        for validator in ExceptionInfo.Validators._exception_stacktrace_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
