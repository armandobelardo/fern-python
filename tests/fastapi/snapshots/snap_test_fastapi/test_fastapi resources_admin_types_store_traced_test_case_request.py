# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...submission.types.test_case_result_with_stdout import TestCaseResultWithStdout
from ...submission.types.trace_response import TraceResponse


class StoreTracedTestCaseRequest(pydantic.BaseModel):
    result: TestCaseResultWithStdout
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StoreTracedTestCaseRequest.Validators.root
            def validate(values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
                ...

            @StoreTracedTestCaseRequest.Validators.field("result")
            def validate_result(v: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial) -> TestCaseResultWithStdout:
                ...

            @StoreTracedTestCaseRequest.Validators.field("trace_responses")
            def validate_trace_responses(v: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial) -> typing.List[TraceResponse]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[StoreTracedTestCaseRequest.Partial], StoreTracedTestCaseRequest.Partial]]
        ] = []
        _result_validators: typing.ClassVar[typing.List[StoreTracedTestCaseRequest.Validators.ResultValidator]] = []
        _trace_responses_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.TraceResponsesValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[StoreTracedTestCaseRequest.Partial], StoreTracedTestCaseRequest.Partial]
        ) -> typing.Callable[[StoreTracedTestCaseRequest.Partial], StoreTracedTestCaseRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["result"]
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.ResultValidator],
            StoreTracedTestCaseRequest.Validators.ResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"]
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.TraceResponsesValidator],
            StoreTracedTestCaseRequest.Validators.TraceResponsesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "result":
                    cls._result_validators.append(validator)
                if field_name == "trace_responses":
                    cls._trace_responses_validators.append(validator)
                return validator

            return decorator

        class ResultValidator(typing_extensions.Protocol):
            def __call__(
                self, v: TestCaseResultWithStdout, *, values: StoreTracedTestCaseRequest.Partial
            ) -> TestCaseResultWithStdout:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TraceResponse], *, values: StoreTracedTestCaseRequest.Partial
            ) -> typing.List[TraceResponse]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
        for validator in StoreTracedTestCaseRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("result")
    def _validate_result(
        cls, v: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial
    ) -> TestCaseResultWithStdout:
        for validator in StoreTracedTestCaseRequest.Validators._result_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("trace_responses")
    def _validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedTestCaseRequest.Validators._trace_responses_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
