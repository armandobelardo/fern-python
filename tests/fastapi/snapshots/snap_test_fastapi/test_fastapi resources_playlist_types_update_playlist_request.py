# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.problem_id import ProblemId


class UpdatePlaylistRequest(pydantic.BaseModel):
    name: str
    problems: typing.List[ProblemId] = pydantic.Field(description=("The problems that make up the playlist.\n"))

    class Partial(typing_extensions.TypedDict):
        name: typing_extensions.NotRequired[str]
        problems: typing_extensions.NotRequired[typing.List[ProblemId]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @UpdatePlaylistRequest.Validators.root
            def validate(values: UpdatePlaylistRequest.Partial) -> UpdatePlaylistRequest.Partial:
                ...

            @UpdatePlaylistRequest.Validators.field("name")
            def validate_name(name: str, values: UpdatePlaylistRequest.Partial) -> str:
                ...

            @UpdatePlaylistRequest.Validators.field("problems")
            def validate_problems(problems: typing.List[ProblemId], values: UpdatePlaylistRequest.Partial) -> typing.List[ProblemId]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[UpdatePlaylistRequest.Partial], UpdatePlaylistRequest.Partial]]
        ] = []
        _name_validators: typing.ClassVar[typing.List[UpdatePlaylistRequest.Validators.NameValidator]] = []
        _problems_validators: typing.ClassVar[typing.List[UpdatePlaylistRequest.Validators.ProblemsValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[UpdatePlaylistRequest.Partial], UpdatePlaylistRequest.Partial]
        ) -> typing.Callable[[UpdatePlaylistRequest.Partial], UpdatePlaylistRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[
            [UpdatePlaylistRequest.Validators.NameValidator], UpdatePlaylistRequest.Validators.NameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problems"]
        ) -> typing.Callable[
            [UpdatePlaylistRequest.Validators.ProblemsValidator], UpdatePlaylistRequest.Validators.ProblemsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "name":
                    cls._name_validators.append(validator)
                if field_name == "problems":
                    cls._problems_validators.append(validator)
                return validator

            return decorator

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: UpdatePlaylistRequest.Partial) -> str:
                ...

        class ProblemsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[ProblemId], __values: UpdatePlaylistRequest.Partial
            ) -> typing.List[ProblemId]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: UpdatePlaylistRequest.Partial) -> UpdatePlaylistRequest.Partial:
        for validator in UpdatePlaylistRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("name")
    def _validate_name(cls, v: str, values: UpdatePlaylistRequest.Partial) -> str:
        for validator in UpdatePlaylistRequest.Validators._name_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problems")
    def _validate_problems(
        cls, v: typing.List[ProblemId], values: UpdatePlaylistRequest.Partial
    ) -> typing.List[ProblemId]:
        for validator in UpdatePlaylistRequest.Validators._problems_validators:
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
