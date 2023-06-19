# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class GetTraceResponsesPageRequest(pydantic.BaseModel):
    offset: typing.Optional[int]

    class Partial(typing_extensions.TypedDict):
        offset: typing_extensions.NotRequired[typing.Optional[int]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetTraceResponsesPageRequest.Validators.root()
            def validate(values: GetTraceResponsesPageRequest.Partial) -> GetTraceResponsesPageRequest.Partial:
                ...

            @GetTraceResponsesPageRequest.Validators.field("offset")
            def validate_offset(offset: typing.Optional[int], values: GetTraceResponsesPageRequest.Partial) -> typing.Optional[int]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GetTraceResponsesPageRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GetTraceResponsesPageRequest.Validators._RootValidator]] = []
        _offset_pre_validators: typing.ClassVar[
            typing.List[GetTraceResponsesPageRequest.Validators.PreOffsetValidator]
        ] = []
        _offset_post_validators: typing.ClassVar[
            typing.List[GetTraceResponsesPageRequest.Validators.OffsetValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetTraceResponsesPageRequest.Validators._RootValidator],
            GetTraceResponsesPageRequest.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetTraceResponsesPageRequest.Validators._PreRootValidator],
            GetTraceResponsesPageRequest.Validators._PreRootValidator,
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetTraceResponsesPageRequest.Validators.PreOffsetValidator],
            GetTraceResponsesPageRequest.Validators.PreOffsetValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetTraceResponsesPageRequest.Validators.OffsetValidator],
            GetTraceResponsesPageRequest.Validators.OffsetValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "offset":
                    if pre:
                        cls._offset_pre_validators.append(validator)
                    else:
                        cls._offset_post_validators.append(validator)
                return validator

            return decorator

        class PreOffsetValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetTraceResponsesPageRequest.Partial) -> typing.Any:
                ...

        class OffsetValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[int], __values: GetTraceResponsesPageRequest.Partial
            ) -> typing.Optional[int]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GetTraceResponsesPageRequest.Partial) -> GetTraceResponsesPageRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_get_trace_responses_page_request_validate(
        cls, values: GetTraceResponsesPageRequest.Partial
    ) -> GetTraceResponsesPageRequest.Partial:
        for validator in GetTraceResponsesPageRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_get_trace_responses_page_request_validate(
        cls, values: GetTraceResponsesPageRequest.Partial
    ) -> GetTraceResponsesPageRequest.Partial:
        for validator in GetTraceResponsesPageRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("offset", pre=True)
    def _pre_validate_offset(
        cls, v: typing.Optional[int], values: GetTraceResponsesPageRequest.Partial
    ) -> typing.Optional[int]:
        for validator in GetTraceResponsesPageRequest.Validators._offset_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("offset", pre=False)
    def _post_validate_offset(
        cls, v: typing.Optional[int], values: GetTraceResponsesPageRequest.Partial
    ) -> typing.Optional[int]:
        for validator in GetTraceResponsesPageRequest.Validators._offset_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        json_encoders = {dt.datetime: serialize_datetime}
