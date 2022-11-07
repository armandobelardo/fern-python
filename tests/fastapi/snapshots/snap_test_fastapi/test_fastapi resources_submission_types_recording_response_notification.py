# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .lightweight_stackframe_information import LightweightStackframeInformation
from .submission_id import SubmissionId
from .traced_file import TracedFile


class RecordingResponseNotification(pydantic.BaseModel):
    submission_id: SubmissionId
    test_case_id: typing.Optional[str]
    line_number: int
    lightweight_stack_info: LightweightStackframeInformation
    traced_file: typing.Optional[TracedFile]

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        test_case_id: typing_extensions.NotRequired[typing.Optional[str]]
        line_number: typing_extensions.NotRequired[int]
        lightweight_stack_info: typing_extensions.NotRequired[LightweightStackframeInformation]
        traced_file: typing_extensions.NotRequired[typing.Optional[TracedFile]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RecordingResponseNotification.Validators.root
            def validate(values: RecordingResponseNotification.Partial) -> RecordingResponseNotification.Partial:
                ...

            @RecordingResponseNotification.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: RecordingResponseNotification.Partial) -> SubmissionId:
                ...

            @RecordingResponseNotification.Validators.field("test_case_id")
            def validate_test_case_id(test_case_id: typing.Optional[str], values: RecordingResponseNotification.Partial) -> typing.Optional[str]:
                ...

            @RecordingResponseNotification.Validators.field("line_number")
            def validate_line_number(line_number: int, values: RecordingResponseNotification.Partial) -> int:
                ...

            @RecordingResponseNotification.Validators.field("lightweight_stack_info")
            def validate_lightweight_stack_info(lightweight_stack_info: LightweightStackframeInformation, values: RecordingResponseNotification.Partial) -> LightweightStackframeInformation:
                ...

            @RecordingResponseNotification.Validators.field("traced_file")
            def validate_traced_file(traced_file: typing.Optional[TracedFile], values: RecordingResponseNotification.Partial) -> typing.Optional[TracedFile]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[RecordingResponseNotification.Partial], RecordingResponseNotification.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.SubmissionIdValidator]
        ] = []
        _test_case_id_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.TestCaseIdValidator]
        ] = []
        _line_number_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.LineNumberValidator]
        ] = []
        _lightweight_stack_info_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.LightweightStackInfoValidator]
        ] = []
        _traced_file_validators: typing.ClassVar[
            typing.List[RecordingResponseNotification.Validators.TracedFileValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[[RecordingResponseNotification.Partial], RecordingResponseNotification.Partial],
        ) -> typing.Callable[[RecordingResponseNotification.Partial], RecordingResponseNotification.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.SubmissionIdValidator],
            RecordingResponseNotification.Validators.SubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case_id"]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.TestCaseIdValidator],
            RecordingResponseNotification.Validators.TestCaseIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.LineNumberValidator],
            RecordingResponseNotification.Validators.LineNumberValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["lightweight_stack_info"]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.LightweightStackInfoValidator],
            RecordingResponseNotification.Validators.LightweightStackInfoValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["traced_file"]
        ) -> typing.Callable[
            [RecordingResponseNotification.Validators.TracedFileValidator],
            RecordingResponseNotification.Validators.TracedFileValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "test_case_id":
                    cls._test_case_id_validators.append(validator)
                if field_name == "line_number":
                    cls._line_number_validators.append(validator)
                if field_name == "lightweight_stack_info":
                    cls._lightweight_stack_info_validators.append(validator)
                if field_name == "traced_file":
                    cls._traced_file_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: RecordingResponseNotification.Partial) -> SubmissionId:
                ...

        class TestCaseIdValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[str], __values: RecordingResponseNotification.Partial
            ) -> typing.Optional[str]:
                ...

        class LineNumberValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: RecordingResponseNotification.Partial) -> int:
                ...

        class LightweightStackInfoValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: LightweightStackframeInformation, __values: RecordingResponseNotification.Partial
            ) -> LightweightStackframeInformation:
                ...

        class TracedFileValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[TracedFile], __values: RecordingResponseNotification.Partial
            ) -> typing.Optional[TracedFile]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: RecordingResponseNotification.Partial) -> RecordingResponseNotification.Partial:
        for validator in RecordingResponseNotification.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: RecordingResponseNotification.Partial) -> SubmissionId:
        for validator in RecordingResponseNotification.Validators._submission_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case_id")
    def _validate_test_case_id(
        cls, v: typing.Optional[str], values: RecordingResponseNotification.Partial
    ) -> typing.Optional[str]:
        for validator in RecordingResponseNotification.Validators._test_case_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number")
    def _validate_line_number(cls, v: int, values: RecordingResponseNotification.Partial) -> int:
        for validator in RecordingResponseNotification.Validators._line_number_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("lightweight_stack_info")
    def _validate_lightweight_stack_info(
        cls, v: LightweightStackframeInformation, values: RecordingResponseNotification.Partial
    ) -> LightweightStackframeInformation:
        for validator in RecordingResponseNotification.Validators._lightweight_stack_info_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("traced_file")
    def _validate_traced_file(
        cls, v: typing.Optional[TracedFile], values: RecordingResponseNotification.Partial
    ) -> typing.Optional[TracedFile]:
        for validator in RecordingResponseNotification.Validators._traced_file_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
