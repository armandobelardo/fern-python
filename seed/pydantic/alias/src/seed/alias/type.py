# This file was auto-generated by Fern from our API Definition.

import typing

from .type_id import TypeId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Type(pydantic.BaseModel):
    """
    A simple type with just a name.
    ---
    from seed.alias import Type

    Type(
        id="type-df89sdg1",
        name="foo",
    )
    """

    id: TypeId
    name: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
