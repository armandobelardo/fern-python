# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .trace_response_v_2 import TraceResponseV2


class TraceResponsesPageV2(pydantic.BaseModel):
    offset: typing.Optional[int]
    trace_responses: typing.List[TraceResponseV2] = pydantic.Field(alias="traceResponses")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TraceResponsesPageV2.Validators.root
            def validate(values: TraceResponsesPageV2.Partial) -> TraceResponsesPageV2.Partial:
                ...

            @TraceResponsesPageV2.Validators.field("offset")
            def validate_offset(v: typing.Optional[int], values: TraceResponsesPageV2.Partial) -> typing.Optional[int]:
                ...

            @TraceResponsesPageV2.Validators.field("trace_responses")
            def validate_trace_responses(v: typing.List[TraceResponseV2], values: TraceResponsesPageV2.Partial) -> typing.List[TraceResponseV2]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TraceResponsesPageV2.Partial], TraceResponsesPageV2.Partial]]
        ] = []
        _offset_validators: typing.ClassVar[typing.List[TraceResponsesPageV2.Validators.OffsetValidator]] = []
        _trace_responses_validators: typing.ClassVar[
            typing.List[TraceResponsesPageV2.Validators.TraceResponsesValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TraceResponsesPageV2.Partial], TraceResponsesPageV2.Partial]
        ) -> typing.Callable[[TraceResponsesPageV2.Partial], TraceResponsesPageV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"]
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators.OffsetValidator], TraceResponsesPageV2.Validators.OffsetValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"]
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators.TraceResponsesValidator],
            TraceResponsesPageV2.Validators.TraceResponsesValidator,
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
                self, v: typing.Optional[int], *, values: TraceResponsesPageV2.Partial
            ) -> typing.Optional[int]:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TraceResponseV2], *, values: TraceResponsesPageV2.Partial
            ) -> typing.List[TraceResponseV2]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        for validator in TraceResponsesPageV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("offset")
    def _validate_offset(cls, v: typing.Optional[int], values: TraceResponsesPageV2.Partial) -> typing.Optional[int]:
        for validator in TraceResponsesPageV2.Validators._offset_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("trace_responses")
    def _validate_trace_responses(
        cls, v: typing.List[TraceResponseV2], values: TraceResponsesPageV2.Partial
    ) -> typing.List[TraceResponseV2]:
        for validator in TraceResponsesPageV2.Validators._trace_responses_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        offset: typing_extensions.NotRequired[typing.Optional[int]]
        trace_responses: typing_extensions.NotRequired[typing.List[TraceResponseV2]]

    class Config:
        frozen = True
        allow_population_by_field_name = True
