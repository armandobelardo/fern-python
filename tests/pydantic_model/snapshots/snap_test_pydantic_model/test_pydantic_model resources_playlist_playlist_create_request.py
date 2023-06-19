# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from ..commons.problem_id import ProblemId


class PlaylistCreateRequest(pydantic.BaseModel):
    name: str
    problems: typing.List[ProblemId]

    class Partial(typing_extensions.TypedDict):
        name: typing_extensions.NotRequired[str]
        problems: typing_extensions.NotRequired[typing.List[ProblemId]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @PlaylistCreateRequest.Validators.root()
            def validate(values: PlaylistCreateRequest.Partial) -> PlaylistCreateRequest.Partial:
                ...

            @PlaylistCreateRequest.Validators.field("name")
            def validate_name(name: str, values: PlaylistCreateRequest.Partial) -> str:
                ...

            @PlaylistCreateRequest.Validators.field("problems")
            def validate_problems(problems: typing.List[ProblemId], values: PlaylistCreateRequest.Partial) -> typing.List[ProblemId]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[PlaylistCreateRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[PlaylistCreateRequest.Validators._RootValidator]] = []
        _name_pre_validators: typing.ClassVar[typing.List[PlaylistCreateRequest.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[PlaylistCreateRequest.Validators.NameValidator]] = []
        _problems_pre_validators: typing.ClassVar[
            typing.List[PlaylistCreateRequest.Validators.PreProblemsValidator]
        ] = []
        _problems_post_validators: typing.ClassVar[typing.List[PlaylistCreateRequest.Validators.ProblemsValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators._RootValidator], PlaylistCreateRequest.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators._PreRootValidator], PlaylistCreateRequest.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators.PreNameValidator], PlaylistCreateRequest.Validators.PreNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators.NameValidator], PlaylistCreateRequest.Validators.NameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problems"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators.PreProblemsValidator],
            PlaylistCreateRequest.Validators.PreProblemsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problems"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators.ProblemsValidator], PlaylistCreateRequest.Validators.ProblemsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                if field_name == "problems":
                    if pre:
                        cls._problems_pre_validators.append(validator)
                    else:
                        cls._problems_post_validators.append(validator)
                return validator

            return decorator

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: PlaylistCreateRequest.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: PlaylistCreateRequest.Partial) -> str:
                ...

        class PreProblemsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: PlaylistCreateRequest.Partial) -> typing.Any:
                ...

        class ProblemsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[ProblemId], __values: PlaylistCreateRequest.Partial
            ) -> typing.List[ProblemId]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: PlaylistCreateRequest.Partial) -> PlaylistCreateRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_playlist_create_request_validate(
        cls, values: PlaylistCreateRequest.Partial
    ) -> PlaylistCreateRequest.Partial:
        for validator in PlaylistCreateRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_playlist_create_request_validate(
        cls, values: PlaylistCreateRequest.Partial
    ) -> PlaylistCreateRequest.Partial:
        for validator in PlaylistCreateRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: PlaylistCreateRequest.Partial) -> str:
        for validator in PlaylistCreateRequest.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: PlaylistCreateRequest.Partial) -> str:
        for validator in PlaylistCreateRequest.Validators._name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problems", pre=True)
    def _pre_validate_problems(
        cls, v: typing.List[ProblemId], values: PlaylistCreateRequest.Partial
    ) -> typing.List[ProblemId]:
        for validator in PlaylistCreateRequest.Validators._problems_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problems", pre=False)
    def _post_validate_problems(
        cls, v: typing.List[ProblemId], values: PlaylistCreateRequest.Partial
    ) -> typing.List[ProblemId]:
        for validator in PlaylistCreateRequest.Validators._problems_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        json_encoders = {dt.datetime: serialize_datetime}
