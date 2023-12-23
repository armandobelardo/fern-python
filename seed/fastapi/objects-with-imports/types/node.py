# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..commons.metadata.types.metadata import Metadata
from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Node(pydantic.BaseModel):
    """
    from seed.objects_with_imports import Node
    from seed.objects_with_imports.commons import Metadata

    Node(
        id="node-8dvgfja2",
        label="left",
        metadata=Metadata(
            id="metadata-kjasf923",
            data={"foo": "bar", "baz": "qux"},
        ),
    )
    """

    id: str
    label: typing.Optional[str]
    metadata: typing.Optional[Metadata]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
