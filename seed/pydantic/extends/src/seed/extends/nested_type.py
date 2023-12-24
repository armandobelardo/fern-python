# This file was auto-generated by Fern from our API Definition.

import typing

from .json import Json


class NestedType(Json):
    """
    from seed.extends import NestedType

    NestedType(
        docs="This is an example nested type.",
        name="NestedExample",
        raw='{"nested": "example"}',
    )
    """

    name: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
