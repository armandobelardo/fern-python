# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.problem_id import ProblemId
from .submission_id import SubmissionId


class CustomTestCasesUnsupported(pydantic.BaseModel):
    problem_id: ProblemId
    submission_id: SubmissionId

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        submission_id: typing_extensions.NotRequired[SubmissionId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CustomTestCasesUnsupported.Validators.root
            def validate(values: CustomTestCasesUnsupported.Partial) -> CustomTestCasesUnsupported.Partial:
                ...

            @CustomTestCasesUnsupported.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: CustomTestCasesUnsupported.Partial) -> ProblemId:
                ...

            @CustomTestCasesUnsupported.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: CustomTestCasesUnsupported.Partial) -> SubmissionId:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[CustomTestCasesUnsupported.Partial], CustomTestCasesUnsupported.Partial]]
        ] = []
        _problem_id_validators: typing.ClassVar[
            typing.List[CustomTestCasesUnsupported.Validators.ProblemIdValidator]
        ] = []
        _submission_id_validators: typing.ClassVar[
            typing.List[CustomTestCasesUnsupported.Validators.SubmissionIdValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[CustomTestCasesUnsupported.Partial], CustomTestCasesUnsupported.Partial]
        ) -> typing.Callable[[CustomTestCasesUnsupported.Partial], CustomTestCasesUnsupported.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[
            [CustomTestCasesUnsupported.Validators.ProblemIdValidator],
            CustomTestCasesUnsupported.Validators.ProblemIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [CustomTestCasesUnsupported.Validators.SubmissionIdValidator],
            CustomTestCasesUnsupported.Validators.SubmissionIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: CustomTestCasesUnsupported.Partial) -> ProblemId:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: CustomTestCasesUnsupported.Partial) -> SubmissionId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: CustomTestCasesUnsupported.Partial) -> CustomTestCasesUnsupported.Partial:
        for validator in CustomTestCasesUnsupported.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, v: ProblemId, values: CustomTestCasesUnsupported.Partial) -> ProblemId:
        for validator in CustomTestCasesUnsupported.Validators._problem_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: CustomTestCasesUnsupported.Partial) -> SubmissionId:
        for validator in CustomTestCasesUnsupported.Validators._submission_id_validators:
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
