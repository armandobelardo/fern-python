from __future__ import annotations

import typing

import pydantic


class MapType(pydantic.BaseModel):
    key_type: TypeReference = pydantic.Field(alias="keyType")
    value_type: TypeReference = pydantic.Field(alias="valueType")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True


from .type_reference import TypeReference  # noqa: E402

MapType.update_forward_refs()
