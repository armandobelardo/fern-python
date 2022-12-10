# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class StdoutResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    stdout: str

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        stdout: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StdoutResponse.Validators.root()
            def validate(values: StdoutResponse.Partial) -> StdoutResponse.Partial:
                ...

            @StdoutResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: StdoutResponse.Partial) -> SubmissionId:
                ...

            @StdoutResponse.Validators.field("stdout")
            def validate_stdout(stdout: str, values: StdoutResponse.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StdoutResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StdoutResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[StdoutResponse.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[StdoutResponse.Validators.SubmissionIdValidator]
        ] = []
        _stdout_pre_validators: typing.ClassVar[typing.List[StdoutResponse.Validators.PreStdoutValidator]] = []
        _stdout_post_validators: typing.ClassVar[typing.List[StdoutResponse.Validators.StdoutValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[StdoutResponse.Validators._RootValidator], StdoutResponse.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StdoutResponse.Validators._PreRootValidator], StdoutResponse.Validators._PreRootValidator
        ]:
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StdoutResponse.Validators.PreSubmissionIdValidator], StdoutResponse.Validators.PreSubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [StdoutResponse.Validators.SubmissionIdValidator], StdoutResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StdoutResponse.Validators.PreStdoutValidator], StdoutResponse.Validators.PreStdoutValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[StdoutResponse.Validators.StdoutValidator], StdoutResponse.Validators.StdoutValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "stdout":
                    if pre:
                        cls._stdout_pre_validators.append(validator)
                    else:
                        cls._stdout_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StdoutResponse.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: StdoutResponse.Partial) -> SubmissionId:
                ...

        class PreStdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StdoutResponse.Partial) -> typing.Any:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: StdoutResponse.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StdoutResponse.Partial) -> StdoutResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: StdoutResponse.Partial) -> StdoutResponse.Partial:
        for validator in StdoutResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: StdoutResponse.Partial) -> StdoutResponse.Partial:
        for validator in StdoutResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: StdoutResponse.Partial) -> SubmissionId:
        for validator in StdoutResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: StdoutResponse.Partial) -> SubmissionId:
        for validator in StdoutResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=True)
    def _pre_validate_stdout(cls, v: str, values: StdoutResponse.Partial) -> str:
        for validator in StdoutResponse.Validators._stdout_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=False)
    def _post_validate_stdout(cls, v: str, values: StdoutResponse.Partial) -> str:
        for validator in StdoutResponse.Validators._stdout_post_validators:
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
        allow_population_by_field_name = True
