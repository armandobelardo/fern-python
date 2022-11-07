# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class StdoutResponse(pydantic.BaseModel):
    submission_id: SubmissionId
    stdout: str

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        stdout: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StdoutResponse.Validators.root
            def validate(values: StdoutResponse.Partial) -> StdoutResponse.Partial:
                ...

            @StdoutResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: StdoutResponse.Partial) -> SubmissionId:
                ...

            @StdoutResponse.Validators.field("stdout")
            def validate_stdout(stdout: str, values: StdoutResponse.Partial) -> str:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[StdoutResponse.Partial], StdoutResponse.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[typing.List[StdoutResponse.Validators.SubmissionIdValidator]] = []
        _stdout_validators: typing.ClassVar[typing.List[StdoutResponse.Validators.StdoutValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[StdoutResponse.Partial], StdoutResponse.Partial]
        ) -> typing.Callable[[StdoutResponse.Partial], StdoutResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [StdoutResponse.Validators.SubmissionIdValidator], StdoutResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"]
        ) -> typing.Callable[[StdoutResponse.Validators.StdoutValidator], StdoutResponse.Validators.StdoutValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "stdout":
                    cls._stdout_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: StdoutResponse.Partial) -> SubmissionId:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: StdoutResponse.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: StdoutResponse.Partial) -> StdoutResponse.Partial:
        for validator in StdoutResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: StdoutResponse.Partial) -> SubmissionId:
        for validator in StdoutResponse.Validators._submission_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout")
    def _validate_stdout(cls, v: str, values: StdoutResponse.Partial) -> str:
        for validator in StdoutResponse.Validators._stdout_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
