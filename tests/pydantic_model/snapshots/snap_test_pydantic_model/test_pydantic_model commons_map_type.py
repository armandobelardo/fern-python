# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions


class MapType(pydantic.BaseModel):
    key_type: VariableType = pydantic.Field(alias="keyType")
    value_type: VariableType = pydantic.Field(alias="valueType")

    class Partial(typing_extensions.TypedDict):
        key_type: typing_extensions.NotRequired[VariableType]
        value_type: typing_extensions.NotRequired[VariableType]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @MapType.Validators.root()
            def validate(values: MapType.Partial) -> MapType.Partial:
                ...

            @MapType.Validators.field("key_type")
            def validate_key_type(key_type: VariableType, values: MapType.Partial) -> VariableType:
                ...

            @MapType.Validators.field("value_type")
            def validate_value_type(value_type: VariableType, values: MapType.Partial) -> VariableType:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[MapType.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[MapType.Validators._RootValidator]] = []
        _key_type_pre_validators: typing.ClassVar[typing.List[MapType.Validators.PreKeyTypeValidator]] = []
        _key_type_post_validators: typing.ClassVar[typing.List[MapType.Validators.KeyTypeValidator]] = []
        _value_type_pre_validators: typing.ClassVar[typing.List[MapType.Validators.PreValueTypeValidator]] = []
        _value_type_post_validators: typing.ClassVar[typing.List[MapType.Validators.ValueTypeValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[MapType.Validators._RootValidator], MapType.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[MapType.Validators._PreRootValidator], MapType.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["key_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[MapType.Validators.PreKeyTypeValidator], MapType.Validators.PreKeyTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["key_type"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[MapType.Validators.KeyTypeValidator], MapType.Validators.KeyTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[MapType.Validators.PreValueTypeValidator], MapType.Validators.PreValueTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[MapType.Validators.ValueTypeValidator], MapType.Validators.ValueTypeValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "key_type":
                    if pre:
                        cls._key_type_pre_validators.append(validator)
                    else:
                        cls._key_type_post_validators.append(validator)
                if field_name == "value_type":
                    if pre:
                        cls._value_type_pre_validators.append(validator)
                    else:
                        cls._value_type_post_validators.append(validator)
                return validator

            return decorator

        class PreKeyTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: MapType.Partial) -> typing.Any:
                ...

        class KeyTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: MapType.Partial) -> VariableType:
                ...

        class PreValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: MapType.Partial) -> typing.Any:
                ...

        class ValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: MapType.Partial) -> VariableType:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: MapType.Partial) -> MapType.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: MapType.Partial) -> MapType.Partial:
        for validator in MapType.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: MapType.Partial) -> MapType.Partial:
        for validator in MapType.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("key_type", pre=True)
    def _pre_validate_key_type(cls, v: VariableType, values: MapType.Partial) -> VariableType:
        for validator in MapType.Validators._key_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("key_type", pre=False)
    def _post_validate_key_type(cls, v: VariableType, values: MapType.Partial) -> VariableType:
        for validator in MapType.Validators._key_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value_type", pre=True)
    def _pre_validate_value_type(cls, v: VariableType, values: MapType.Partial) -> VariableType:
        for validator in MapType.Validators._value_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value_type", pre=False)
    def _post_validate_value_type(cls, v: VariableType, values: MapType.Partial) -> VariableType:
        for validator in MapType.Validators._value_type_post_validators:
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
        json_encoders = {dt.datetime: lambda v: v.isoformat()}


from .variable_type import VariableType  # noqa: E402

MapType.update_forward_refs()
