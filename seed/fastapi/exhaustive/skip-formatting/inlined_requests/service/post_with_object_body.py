# This file was auto-generated by Fern from our API Definition.

from ...types.object.types.object_with_optional_field import ObjectWithOptionalField
import typing

try:
    import pydantic.v1 as pydantic # type: ignore
except ImportError:
    import pydantic # type: ignore
            
class PostWithObjectBody(pydantic.BaseModel):
    string: str
    integer: int
    nested_object: ObjectWithOptionalField = pydantic.Field(alias="NestedObject")
    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().json(**kwargs_with_defaults)
    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().dict(**kwargs_with_defaults)