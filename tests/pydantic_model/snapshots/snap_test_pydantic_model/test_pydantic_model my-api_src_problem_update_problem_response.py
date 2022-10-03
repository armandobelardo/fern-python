import typing

import pydantic


class UpdateProblemResponse(pydantic.BaseModel):
    problem_version: int = pydantic.Field(alias="problemVersion")

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
