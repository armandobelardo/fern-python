# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .metadata import Metadata as commons_types_types_metadata_Metadata
from .tag import Tag as commons_types_types_tag_Tag

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def metadata(self, value: commons_types_types_metadata_Metadata) -> EventInfo:
        return EventInfo(__root__=_EventInfo.Metadata(**value.dict(exclude_unset=True), type="metadata"))

    def tag(self, value: commons_types_types_tag_Tag) -> EventInfo:
        return EventInfo(__root__=_EventInfo.Tag(type="tag", value=value))


class EventInfo(pydantic.BaseModel):
    """
    from seed.examples.commons import EventInfo_Metadata

    EventInfo_Metadata(
        type="metadata",
        id="metadata-alskjfg8",
        data={"one": "two"},
        json_string='{"one": "two"}',
    )
    """

    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_EventInfo.Metadata, _EventInfo.Tag]:
        return self.__root__

    def visit(
        self,
        metadata: typing.Callable[[commons_types_types_metadata_Metadata], T_Result],
        tag: typing.Callable[[commons_types_types_tag_Tag], T_Result],
    ) -> T_Result:
        if self.__root__.type == "metadata":
            return metadata(
                commons_types_types_metadata_Metadata(**self.__root__.dict(exclude_unset=True, exclude={"type"}))
            )
        if self.__root__.type == "tag":
            return tag(self.__root__.value)

    __root__: typing_extensions.Annotated[
        typing.Union[_EventInfo.Metadata, _EventInfo.Tag], pydantic.Field(discriminator="type")
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _EventInfo:
    class Metadata(commons_types_types_metadata_Metadata):
        type: typing_extensions.Literal["metadata"]

        class Config:
            allow_population_by_field_name = True

    class Tag(pydantic.BaseModel):
        type: typing_extensions.Literal["tag"]
        value: commons_types_types_tag_Tag


EventInfo.update_forward_refs()
