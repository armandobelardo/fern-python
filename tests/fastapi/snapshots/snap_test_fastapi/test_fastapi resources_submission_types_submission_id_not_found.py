# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class SubmissionIdNotFound(pydantic.BaseModel):
    missing_submission_id: SubmissionId = pydantic.Field(alias="missingSubmissionId")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionIdNotFound.Validators.root
            def validate(values: SubmissionIdNotFound.Partial) -> SubmissionIdNotFound.Partial:
                ...

            @SubmissionIdNotFound.Validators.field("missing_submission_id")
            def validate_missing_submission_id(v: SubmissionId, values: SubmissionIdNotFound.Partial) -> SubmissionId:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[SubmissionIdNotFound.Partial], SubmissionIdNotFound.Partial]]
        ] = []
        _missing_submission_id_validators: typing.ClassVar[
            typing.List[SubmissionIdNotFound.Validators.MissingSubmissionIdValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[SubmissionIdNotFound.Partial], SubmissionIdNotFound.Partial]
        ) -> typing.Callable[[SubmissionIdNotFound.Partial], SubmissionIdNotFound.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["missing_submission_id"]
        ) -> typing.Callable[
            [SubmissionIdNotFound.Validators.MissingSubmissionIdValidator],
            SubmissionIdNotFound.Validators.MissingSubmissionIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "missing_submission_id":
                    cls._missing_submission_id_validators.append(validator)
                return validator

            return decorator

        class MissingSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: SubmissionId, *, values: SubmissionIdNotFound.Partial) -> SubmissionId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: SubmissionIdNotFound.Partial) -> SubmissionIdNotFound.Partial:
        for validator in SubmissionIdNotFound.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("missing_submission_id")
    def _validate_missing_submission_id(cls, v: SubmissionId, values: SubmissionIdNotFound.Partial) -> SubmissionId:
        for validator in SubmissionIdNotFound.Validators._missing_submission_id_validators:
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
