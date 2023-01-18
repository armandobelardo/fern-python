# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...submission.types.test_case_result_with_stdout import TestCaseResultWithStdout
from ...submission.types.trace_response import TraceResponse


class StoreTracedTestCaseRequest(pydantic.BaseModel):
    result: TestCaseResultWithStdout
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    class Partial(typing_extensions.TypedDict):
        result: typing_extensions.NotRequired[TestCaseResultWithStdout]
        trace_responses: typing_extensions.NotRequired[typing.List[TraceResponse]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StoreTracedTestCaseRequest.Validators.root()
            def validate(values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
                ...

            @StoreTracedTestCaseRequest.Validators.field("result")
            def validate_result(result: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial) -> TestCaseResultWithStdout:
                ...

            @StoreTracedTestCaseRequest.Validators.field("trace_responses")
            def validate_trace_responses(trace_responses: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial) -> typing.List[TraceResponse]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StoreTracedTestCaseRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StoreTracedTestCaseRequest.Validators._RootValidator]] = []
        _result_pre_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.PreResultValidator]
        ] = []
        _result_post_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.ResultValidator]
        ] = []
        _trace_responses_pre_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.PreTraceResponsesValidator]
        ] = []
        _trace_responses_post_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.TraceResponsesValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators._RootValidator], StoreTracedTestCaseRequest.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators._PreRootValidator],
            StoreTracedTestCaseRequest.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["result"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.PreResultValidator],
            StoreTracedTestCaseRequest.Validators.PreResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["result"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.ResultValidator],
            StoreTracedTestCaseRequest.Validators.ResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.PreTraceResponsesValidator],
            StoreTracedTestCaseRequest.Validators.PreTraceResponsesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["trace_responses"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.TraceResponsesValidator],
            StoreTracedTestCaseRequest.Validators.TraceResponsesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "result":
                    if pre:
                        cls._result_pre_validators.append(validator)
                    else:
                        cls._result_post_validators.append(validator)
                if field_name == "trace_responses":
                    if pre:
                        cls._trace_responses_pre_validators.append(validator)
                    else:
                        cls._trace_responses_post_validators.append(validator)
                return validator

            return decorator

        class PreResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StoreTracedTestCaseRequest.Partial) -> typing.Any:
                ...

        class ResultValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseResultWithStdout, __values: StoreTracedTestCaseRequest.Partial
            ) -> TestCaseResultWithStdout:
                ...

        class PreTraceResponsesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StoreTracedTestCaseRequest.Partial) -> typing.Any:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TraceResponse], __values: StoreTracedTestCaseRequest.Partial
            ) -> typing.List[TraceResponse]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
        for validator in StoreTracedTestCaseRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
        for validator in StoreTracedTestCaseRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("result", pre=True)
    def _pre_validate_result(
        cls, v: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial
    ) -> TestCaseResultWithStdout:
        for validator in StoreTracedTestCaseRequest.Validators._result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("result", pre=False)
    def _post_validate_result(
        cls, v: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial
    ) -> TestCaseResultWithStdout:
        for validator in StoreTracedTestCaseRequest.Validators._result_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=True)
    def _pre_validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedTestCaseRequest.Validators._trace_responses_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=False)
    def _post_validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedTestCaseRequest.Validators._trace_responses_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
