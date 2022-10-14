# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class LightweightStackframeInformation(pydantic.BaseModel):
    num_stack_frames: int = pydantic.Field(alias="numStackFrames")
    top_stack_frame_method_name: str = pydantic.Field(alias="topStackFrameMethodName")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @LightweightStackframeInformation.Validators.root
            def validate(values: LightweightStackframeInformation.Partial) -> LightweightStackframeInformation.Partial:
                ...

            @LightweightStackframeInformation.Validators.field("num_stack_frames")
            def validate_num_stack_frames(v: int, values: LightweightStackframeInformation.Partial) -> int:
                ...

            @LightweightStackframeInformation.Validators.field("top_stack_frame_method_name")
            def validate_top_stack_frame_method_name(v: str, values: LightweightStackframeInformation.Partial) -> str:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[[LightweightStackframeInformation.Partial], LightweightStackframeInformation.Partial]
            ]
        ] = []
        _num_stack_frames_validators: typing.ClassVar[
            typing.List[LightweightStackframeInformation.Validators.NumStackFramesValidator]
        ] = []
        _top_stack_frame_method_name_validators: typing.ClassVar[
            typing.List[LightweightStackframeInformation.Validators.TopStackFrameMethodNameValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [LightweightStackframeInformation.Partial], LightweightStackframeInformation.Partial
            ],
        ) -> typing.Callable[[LightweightStackframeInformation.Partial], LightweightStackframeInformation.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["num_stack_frames"]
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators.NumStackFramesValidator],
            LightweightStackframeInformation.Validators.NumStackFramesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["top_stack_frame_method_name"]
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators.TopStackFrameMethodNameValidator],
            LightweightStackframeInformation.Validators.TopStackFrameMethodNameValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "num_stack_frames":
                    cls._num_stack_frames_validators.append(validator)
                if field_name == "top_stack_frame_method_name":
                    cls._top_stack_frame_method_name_validators.append(validator)
                return validator

            return decorator

        class NumStackFramesValidator(typing_extensions.Protocol):
            def __call__(self, v: int, *, values: LightweightStackframeInformation.Partial) -> int:
                ...

        class TopStackFrameMethodNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: LightweightStackframeInformation.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: LightweightStackframeInformation.Partial) -> LightweightStackframeInformation.Partial:
        for validator in LightweightStackframeInformation.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("num_stack_frames")
    def _validate_num_stack_frames(cls, v: int, values: LightweightStackframeInformation.Partial) -> int:
        for validator in LightweightStackframeInformation.Validators._num_stack_frames_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("top_stack_frame_method_name")
    def _validate_top_stack_frame_method_name(cls, v: str, values: LightweightStackframeInformation.Partial) -> str:
        for validator in LightweightStackframeInformation.Validators._top_stack_frame_method_name_validators:
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
