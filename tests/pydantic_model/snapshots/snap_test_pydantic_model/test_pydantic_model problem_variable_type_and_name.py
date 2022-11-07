# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.variable_type import VariableType


class VariableTypeAndName(pydantic.BaseModel):
    variable_type: VariableType
    name: str

    class Partial(typing_extensions.TypedDict):
        variable_type: typing_extensions.NotRequired[VariableType]
        name: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VariableTypeAndName.Validators.root
            def validate(values: VariableTypeAndName.Partial) -> VariableTypeAndName.Partial:
                ...

            @VariableTypeAndName.Validators.field("variable_type")
            def validate_variable_type(variable_type: VariableType, values: VariableTypeAndName.Partial) -> VariableType:
                ...

            @VariableTypeAndName.Validators.field("name")
            def validate_name(name: str, values: VariableTypeAndName.Partial) -> str:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[VariableTypeAndName.Partial], VariableTypeAndName.Partial]]
        ] = []
        _variable_type_validators: typing.ClassVar[
            typing.List[VariableTypeAndName.Validators.VariableTypeValidator]
        ] = []
        _name_validators: typing.ClassVar[typing.List[VariableTypeAndName.Validators.NameValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[VariableTypeAndName.Partial], VariableTypeAndName.Partial]
        ) -> typing.Callable[[VariableTypeAndName.Partial], VariableTypeAndName.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variable_type"]
        ) -> typing.Callable[
            [VariableTypeAndName.Validators.VariableTypeValidator], VariableTypeAndName.Validators.VariableTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[
            [VariableTypeAndName.Validators.NameValidator], VariableTypeAndName.Validators.NameValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "variable_type":
                    cls._variable_type_validators.append(validator)
                if field_name == "name":
                    cls._name_validators.append(validator)
                return validator

            return decorator

        class VariableTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: VariableTypeAndName.Partial) -> VariableType:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: VariableTypeAndName.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: VariableTypeAndName.Partial) -> VariableTypeAndName.Partial:
        for validator in VariableTypeAndName.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("variable_type")
    def _validate_variable_type(cls, v: VariableType, values: VariableTypeAndName.Partial) -> VariableType:
        for validator in VariableTypeAndName.Validators._variable_type_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name")
    def _validate_name(cls, v: str, values: VariableTypeAndName.Partial) -> str:
        for validator in VariableTypeAndName.Validators._name_validators:
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
