# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class ExpressionLocation(pydantic.BaseModel):
    start: int
    offset: int

    class Partial(typing_extensions.TypedDict):
        start: typing_extensions.NotRequired[int]
        offset: typing_extensions.NotRequired[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ExpressionLocation.Validators.root()
            def validate(values: ExpressionLocation.Partial) -> ExpressionLocation.Partial:
                ...

            @ExpressionLocation.Validators.field("start")
            def validate_start(start: int, values: ExpressionLocation.Partial) -> int:
                ...

            @ExpressionLocation.Validators.field("offset")
            def validate_offset(offset: int, values: ExpressionLocation.Partial) -> int:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ExpressionLocation.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ExpressionLocation.Validators._RootValidator]] = []
        _start_pre_validators: typing.ClassVar[typing.List[ExpressionLocation.Validators.PreStartValidator]] = []
        _start_post_validators: typing.ClassVar[typing.List[ExpressionLocation.Validators.StartValidator]] = []
        _offset_pre_validators: typing.ClassVar[typing.List[ExpressionLocation.Validators.PreOffsetValidator]] = []
        _offset_post_validators: typing.ClassVar[typing.List[ExpressionLocation.Validators.OffsetValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExpressionLocation.Validators._RootValidator], ExpressionLocation.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExpressionLocation.Validators._PreRootValidator], ExpressionLocation.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["start"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExpressionLocation.Validators.PreStartValidator], ExpressionLocation.Validators.PreStartValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["start"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExpressionLocation.Validators.StartValidator], ExpressionLocation.Validators.StartValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExpressionLocation.Validators.PreOffsetValidator], ExpressionLocation.Validators.PreOffsetValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExpressionLocation.Validators.OffsetValidator], ExpressionLocation.Validators.OffsetValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "start":
                    if pre:
                        cls._start_pre_validators.append(validator)
                    else:
                        cls._start_post_validators.append(validator)
                if field_name == "offset":
                    if pre:
                        cls._offset_pre_validators.append(validator)
                    else:
                        cls._offset_post_validators.append(validator)
                return validator

            return decorator

        class PreStartValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExpressionLocation.Partial) -> typing.Any:
                ...

        class StartValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: ExpressionLocation.Partial) -> int:
                ...

        class PreOffsetValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExpressionLocation.Partial) -> typing.Any:
                ...

        class OffsetValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: ExpressionLocation.Partial) -> int:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ExpressionLocation.Partial) -> ExpressionLocation.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: ExpressionLocation.Partial) -> ExpressionLocation.Partial:
        for validator in ExpressionLocation.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: ExpressionLocation.Partial) -> ExpressionLocation.Partial:
        for validator in ExpressionLocation.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("start", pre=True)
    def _pre_validate_start(cls, v: int, values: ExpressionLocation.Partial) -> int:
        for validator in ExpressionLocation.Validators._start_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("start", pre=False)
    def _post_validate_start(cls, v: int, values: ExpressionLocation.Partial) -> int:
        for validator in ExpressionLocation.Validators._start_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("offset", pre=True)
    def _pre_validate_offset(cls, v: int, values: ExpressionLocation.Partial) -> int:
        for validator in ExpressionLocation.Validators._offset_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("offset", pre=False)
    def _post_validate_offset(cls, v: int, values: ExpressionLocation.Partial) -> int:
        for validator in ExpressionLocation.Validators._offset_post_validators:
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
        orm_mode = True
        json_encoders = {dt.datetime: serialize_datetime}
