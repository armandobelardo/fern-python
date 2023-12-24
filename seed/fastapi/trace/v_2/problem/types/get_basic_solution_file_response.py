# This file was auto-generated by Fern from our API Definition.

import typing

from ....commons.types.language import Language
from .file_info_v_2 import FileInfoV2

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GetBasicSolutionFileResponse(pydantic.BaseModel):
    solution_file_by_language: typing.Dict[Language, FileInfoV2] = pydantic.Field(alias="solutionFileByLanguage")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
