# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from ..commons.problem_id import ProblemId


class InitializeProblemRequest(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_version: typing.Optional[int] = pydantic.Field(alias="problemVersion", default=None)

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_version: typing_extensions.NotRequired[typing.Optional[int]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @InitializeProblemRequest.Validators.root()
            def validate(values: InitializeProblemRequest.Partial) -> InitializeProblemRequest.Partial:
                ...

            @InitializeProblemRequest.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: InitializeProblemRequest.Partial) -> ProblemId:
                ...

            @InitializeProblemRequest.Validators.field("problem_version")
            def validate_problem_version(problem_version: typing.Optional[int], values: InitializeProblemRequest.Partial) -> typing.Optional[int]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[InitializeProblemRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[InitializeProblemRequest.Validators._RootValidator]] = []
        _problem_id_pre_validators: typing.ClassVar[
            typing.List[InitializeProblemRequest.Validators.PreProblemIdValidator]
        ] = []
        _problem_id_post_validators: typing.ClassVar[
            typing.List[InitializeProblemRequest.Validators.ProblemIdValidator]
        ] = []
        _problem_version_pre_validators: typing.ClassVar[
            typing.List[InitializeProblemRequest.Validators.PreProblemVersionValidator]
        ] = []
        _problem_version_post_validators: typing.ClassVar[
            typing.List[InitializeProblemRequest.Validators.ProblemVersionValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators._RootValidator], InitializeProblemRequest.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators._PreRootValidator],
            InitializeProblemRequest.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators.PreProblemIdValidator],
            InitializeProblemRequest.Validators.PreProblemIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators.ProblemIdValidator],
            InitializeProblemRequest.Validators.ProblemIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators.PreProblemVersionValidator],
            InitializeProblemRequest.Validators.PreProblemVersionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["problem_version"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators.ProblemVersionValidator],
            InitializeProblemRequest.Validators.ProblemVersionValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    if pre:
                        cls._problem_id_pre_validators.append(validator)
                    else:
                        cls._problem_id_post_validators.append(validator)
                if field_name == "problem_version":
                    if pre:
                        cls._problem_version_pre_validators.append(validator)
                    else:
                        cls._problem_version_post_validators.append(validator)
                return validator

            return decorator

        class PreProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: InitializeProblemRequest.Partial) -> typing.Any:
                ...

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: InitializeProblemRequest.Partial) -> ProblemId:
                ...

        class PreProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: InitializeProblemRequest.Partial) -> typing.Any:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[int], __values: InitializeProblemRequest.Partial
            ) -> typing.Optional[int]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: InitializeProblemRequest.Partial) -> InitializeProblemRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_initialize_problem_request(
        cls, values: InitializeProblemRequest.Partial
    ) -> InitializeProblemRequest.Partial:
        for validator in InitializeProblemRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_initialize_problem_request(
        cls, values: InitializeProblemRequest.Partial
    ) -> InitializeProblemRequest.Partial:
        for validator in InitializeProblemRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_id", pre=True)
    def _pre_validate_problem_id(cls, v: ProblemId, values: InitializeProblemRequest.Partial) -> ProblemId:
        for validator in InitializeProblemRequest.Validators._problem_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=False)
    def _post_validate_problem_id(cls, v: ProblemId, values: InitializeProblemRequest.Partial) -> ProblemId:
        for validator in InitializeProblemRequest.Validators._problem_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=True)
    def _pre_validate_problem_version(
        cls, v: typing.Optional[int], values: InitializeProblemRequest.Partial
    ) -> typing.Optional[int]:
        for validator in InitializeProblemRequest.Validators._problem_version_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=False)
    def _post_validate_problem_version(
        cls, v: typing.Optional[int], values: InitializeProblemRequest.Partial
    ) -> typing.Optional[int]:
        for validator in InitializeProblemRequest.Validators._problem_version_post_validators:
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