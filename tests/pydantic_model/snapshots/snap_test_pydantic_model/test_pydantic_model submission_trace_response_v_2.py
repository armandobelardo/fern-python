# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.debug_variable_value import DebugVariableValue
from .expression_location import ExpressionLocation
from .stack_information import StackInformation
from .submission_id import SubmissionId
from .traced_file import TracedFile


class TraceResponseV2(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    line_number: int = pydantic.Field(alias="lineNumber")
    file: TracedFile
    return_value: typing.Optional[DebugVariableValue] = pydantic.Field(alias="returnValue")
    expression_location: typing.Optional[ExpressionLocation] = pydantic.Field(alias="expressionLocation")
    stack: StackInformation
    stdout: typing.Optional[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TraceResponseV2.Validators.root
            def validate(values: TraceResponseV2.Partial) -> TraceResponseV2.Partial:
                ...

            @TraceResponseV2.Validators.field("submission_id")
            def validate_submission_id(v: SubmissionId, values: TraceResponseV2.Partial) -> SubmissionId:
                ...

            @TraceResponseV2.Validators.field("line_number")
            def validate_line_number(v: int, values: TraceResponseV2.Partial) -> int:
                ...

            @TraceResponseV2.Validators.field("file")
            def validate_file(v: TracedFile, values: TraceResponseV2.Partial) -> TracedFile:
                ...

            @TraceResponseV2.Validators.field("return_value")
            def validate_return_value(v: typing.Optional[DebugVariableValue], values: TraceResponseV2.Partial) -> typing.Optional[DebugVariableValue]:
                ...

            @TraceResponseV2.Validators.field("expression_location")
            def validate_expression_location(v: typing.Optional[ExpressionLocation], values: TraceResponseV2.Partial) -> typing.Optional[ExpressionLocation]:
                ...

            @TraceResponseV2.Validators.field("stack")
            def validate_stack(v: StackInformation, values: TraceResponseV2.Partial) -> StackInformation:
                ...

            @TraceResponseV2.Validators.field("stdout")
            def validate_stdout(v: typing.Optional[str], values: TraceResponseV2.Partial) -> typing.Optional[str]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TraceResponseV2.Partial], TraceResponseV2.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.SubmissionIdValidator]] = []
        _line_number_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.LineNumberValidator]] = []
        _file_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.FileValidator]] = []
        _return_value_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.ReturnValueValidator]] = []
        _expression_location_validators: typing.ClassVar[
            typing.List[TraceResponseV2.Validators.ExpressionLocationValidator]
        ] = []
        _stack_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.StackValidator]] = []
        _stdout_validators: typing.ClassVar[typing.List[TraceResponseV2.Validators.StdoutValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TraceResponseV2.Partial], TraceResponseV2.Partial]
        ) -> typing.Callable[[TraceResponseV2.Partial], TraceResponseV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.SubmissionIdValidator], TraceResponseV2.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.LineNumberValidator], TraceResponseV2.Validators.LineNumberValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file"]
        ) -> typing.Callable[[TraceResponseV2.Validators.FileValidator], TraceResponseV2.Validators.FileValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["return_value"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.ReturnValueValidator], TraceResponseV2.Validators.ReturnValueValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expression_location"]
        ) -> typing.Callable[
            [TraceResponseV2.Validators.ExpressionLocationValidator],
            TraceResponseV2.Validators.ExpressionLocationValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stack"]
        ) -> typing.Callable[[TraceResponseV2.Validators.StackValidator], TraceResponseV2.Validators.StackValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"]
        ) -> typing.Callable[[TraceResponseV2.Validators.StdoutValidator], TraceResponseV2.Validators.StdoutValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "line_number":
                    cls._line_number_validators.append(validator)
                if field_name == "file":
                    cls._file_validators.append(validator)
                if field_name == "return_value":
                    cls._return_value_validators.append(validator)
                if field_name == "expression_location":
                    cls._expression_location_validators.append(validator)
                if field_name == "stack":
                    cls._stack_validators.append(validator)
                if field_name == "stdout":
                    cls._stdout_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: SubmissionId, *, values: TraceResponseV2.Partial) -> SubmissionId:
                ...

        class LineNumberValidator(typing_extensions.Protocol):
            def __call__(self, v: int, *, values: TraceResponseV2.Partial) -> int:
                ...

        class FileValidator(typing_extensions.Protocol):
            def __call__(self, v: TracedFile, *, values: TraceResponseV2.Partial) -> TracedFile:
                ...

        class ReturnValueValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[DebugVariableValue], *, values: TraceResponseV2.Partial
            ) -> typing.Optional[DebugVariableValue]:
                ...

        class ExpressionLocationValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[ExpressionLocation], *, values: TraceResponseV2.Partial
            ) -> typing.Optional[ExpressionLocation]:
                ...

        class StackValidator(typing_extensions.Protocol):
            def __call__(self, v: StackInformation, *, values: TraceResponseV2.Partial) -> StackInformation:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.Optional[str], *, values: TraceResponseV2.Partial) -> typing.Optional[str]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TraceResponseV2.Partial) -> TraceResponseV2.Partial:
        for validator in TraceResponseV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: TraceResponseV2.Partial) -> SubmissionId:
        for validator in TraceResponseV2.Validators._submission_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("line_number")
    def _validate_line_number(cls, v: int, values: TraceResponseV2.Partial) -> int:
        for validator in TraceResponseV2.Validators._line_number_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("file")
    def _validate_file(cls, v: TracedFile, values: TraceResponseV2.Partial) -> TracedFile:
        for validator in TraceResponseV2.Validators._file_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("return_value")
    def _validate_return_value(
        cls, v: typing.Optional[DebugVariableValue], values: TraceResponseV2.Partial
    ) -> typing.Optional[DebugVariableValue]:
        for validator in TraceResponseV2.Validators._return_value_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("expression_location")
    def _validate_expression_location(
        cls, v: typing.Optional[ExpressionLocation], values: TraceResponseV2.Partial
    ) -> typing.Optional[ExpressionLocation]:
        for validator in TraceResponseV2.Validators._expression_location_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stack")
    def _validate_stack(cls, v: StackInformation, values: TraceResponseV2.Partial) -> StackInformation:
        for validator in TraceResponseV2.Validators._stack_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stdout")
    def _validate_stdout(cls, v: typing.Optional[str], values: TraceResponseV2.Partial) -> typing.Optional[str]:
        for validator in TraceResponseV2.Validators._stdout_validators:
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
