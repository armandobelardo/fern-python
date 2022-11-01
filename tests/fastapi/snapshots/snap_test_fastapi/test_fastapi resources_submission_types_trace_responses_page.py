# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .trace_response import TraceResponse


class TraceResponsesPage(pydantic.BaseModel):
    offset: typing.Optional[int]
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    class Partial(typing_extensions.TypedDict):
        offset: typing_extensions.NotRequired[typing.Optional[int]]
        trace_responses: typing_extensions.NotRequired[typing.List[TraceResponse]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TraceResponsesPage.Validators.root
            def validate(values: TraceResponsesPage.Partial) -> TraceResponsesPage.Partial:
                ...

            @TraceResponsesPage.Validators.field("offset")
            def validate_offset(offset: typing.Optional[int], values: TraceResponsesPage.Partial) -> typing.Optional[int]:
                ...

            @TraceResponsesPage.Validators.field("trace_responses")
            def validate_trace_responses(trace_responses: typing.List[TraceResponse], values: TraceResponsesPage.Partial) -> typing.List[TraceResponse]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TraceResponsesPage.Partial], TraceResponsesPage.Partial]]
        ] = []
        _offset_validators: typing.ClassVar[typing.List[TraceResponsesPage.Validators.OffsetValidator]] = []
        _trace_responses_validators: typing.ClassVar[
            typing.List[TraceResponsesPage.Validators.TraceResponsesValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TraceResponsesPage.Partial], TraceResponsesPage.Partial]
        ) -> typing.Callable[[TraceResponsesPage.Partial], TraceResponsesPage.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"]
        ) -> typing.Callable[
            [TraceResponsesPage.Validators.OffsetValidator], TraceResponsesPage.Validators.OffsetValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"]
        ) -> typing.Callable[
            [TraceResponsesPage.Validators.TraceResponsesValidator],
            TraceResponsesPage.Validators.TraceResponsesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "offset":
                    cls._offset_validators.append(validator)
                if field_name == "trace_responses":
                    cls._trace_responses_validators.append(validator)
                return validator

            return decorator

        class OffsetValidator(typing_extensions.Protocol):
            def __call__(
                self, *, offset: typing.Optional[int], values: TraceResponsesPage.Partial
            ) -> typing.Optional[int]:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, *, trace_responses: typing.List[TraceResponse], values: TraceResponsesPage.Partial
            ) -> typing.List[TraceResponse]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TraceResponsesPage.Partial) -> TraceResponsesPage.Partial:
        for validator in TraceResponsesPage.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("offset")
    def _validate_offset(cls, offset: typing.Optional[int], values: TraceResponsesPage.Partial) -> typing.Optional[int]:
        for validator in TraceResponsesPage.Validators._offset_validators:
            offset = validator(offset, values=values)
        return offset

    @pydantic.validator("trace_responses")
    def _validate_trace_responses(
        cls, trace_responses: typing.List[TraceResponse], values: TraceResponsesPage.Partial
    ) -> typing.List[TraceResponse]:
        for validator in TraceResponsesPage.Validators._trace_responses_validators:
            trace_responses = validator(trace_responses, values=values)
        return trace_responses

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
