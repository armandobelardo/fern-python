import typing

import pydantic
import typing_extensions

from ..commons.problem_id import ProblemId


class PlaylistCreateRequest(pydantic.BaseModel):
    name: str
    problems: typing.List[ProblemId]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("name")
    def _validate_name(cls, name: str) -> str:
        for validator in PlaylistCreateRequest.Validators._name_validators:
            name = validator(name)
        return name

    @pydantic.validator("problems")
    def _validate_problems(cls, problems: typing.List[ProblemId]) -> typing.List[ProblemId]:
        for validator in PlaylistCreateRequest.Validators._problems_validators:
            problems = validator(problems)
        return problems

    class Validators:
        _name_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _problems_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[ProblemId]], typing.List[ProblemId]]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problems"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[ProblemId]], typing.List[ProblemId]]],
            typing.Callable[[typing.List[ProblemId]], typing.List[ProblemId]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "name":
                    cls._name_validators.append(validator)
                elif field_name == "problems":
                    cls._problems_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on PlaylistCreateRequest: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
