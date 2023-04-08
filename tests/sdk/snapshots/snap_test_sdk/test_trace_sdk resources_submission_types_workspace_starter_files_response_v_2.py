# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.language import Language
from ...v_2.resources.problem.types.files import Files


class WorkspaceStarterFilesResponseV2(pydantic.BaseModel):
    files_by_language: typing.Dict[Language, Files] = pydantic.Field(alias="filesByLanguage")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
