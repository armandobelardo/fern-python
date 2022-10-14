# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class ExistingSubmissionExecuting(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ExistingSubmissionExecuting.Validators.root
            def validate(values: ExistingSubmissionExecuting.Partial) -> ExistingSubmissionExecuting.Partial:
                ...

            @ExistingSubmissionExecuting.Validators.field("submission_id")
            def validate_submission_id(v: SubmissionId, values: ExistingSubmissionExecuting.Partial) -> SubmissionId:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[ExistingSubmissionExecuting.Partial], ExistingSubmissionExecuting.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[
            typing.List[ExistingSubmissionExecuting.Validators.SubmissionIdValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[ExistingSubmissionExecuting.Partial], ExistingSubmissionExecuting.Partial]
        ) -> typing.Callable[[ExistingSubmissionExecuting.Partial], ExistingSubmissionExecuting.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [ExistingSubmissionExecuting.Validators.SubmissionIdValidator],
            ExistingSubmissionExecuting.Validators.SubmissionIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: SubmissionId, *, values: ExistingSubmissionExecuting.Partial) -> SubmissionId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: ExistingSubmissionExecuting.Partial) -> ExistingSubmissionExecuting.Partial:
        for validator in ExistingSubmissionExecuting.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: ExistingSubmissionExecuting.Partial) -> SubmissionId:
        for validator in ExistingSubmissionExecuting.Validators._submission_id_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]

    class Config:
        frozen = True
        allow_population_by_field_name = True
