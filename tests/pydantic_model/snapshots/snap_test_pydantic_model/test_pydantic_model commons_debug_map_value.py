# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class DebugMapValue(pydantic.BaseModel):
    key_value_pairs: typing.List[DebugKeyValuePairs] = pydantic.Field(alias="keyValuePairs")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DebugMapValue.Validators.root
            def validate(values: DebugMapValue.Partial) -> DebugMapValue.Partial:
                ...

            @DebugMapValue.Validators.field("key_value_pairs")
            def validate_key_value_pairs(v: typing.List[DebugKeyValuePairs], values: DebugMapValue.Partial) -> typing.List[DebugKeyValuePairs]:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[DebugMapValue.Partial], DebugMapValue.Partial]]] = []
        _key_value_pairs_validators: typing.ClassVar[typing.List[DebugMapValue.Validators.KeyValuePairsValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[DebugMapValue.Partial], DebugMapValue.Partial]
        ) -> typing.Callable[[DebugMapValue.Partial], DebugMapValue.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["key_value_pairs"]
        ) -> typing.Callable[
            [DebugMapValue.Validators.KeyValuePairsValidator], DebugMapValue.Validators.KeyValuePairsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "key_value_pairs":
                    cls._key_value_pairs_validators.append(validator)
                return validator

            return decorator

        class KeyValuePairsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[DebugKeyValuePairs], *, values: DebugMapValue.Partial
            ) -> typing.List[DebugKeyValuePairs]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: DebugMapValue.Partial) -> DebugMapValue.Partial:
        for validator in DebugMapValue.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("key_value_pairs")
    def _validate_key_value_pairs(
        cls, v: typing.List[DebugKeyValuePairs], values: DebugMapValue.Partial
    ) -> typing.List[DebugKeyValuePairs]:
        for validator in DebugMapValue.Validators._key_value_pairs_validators:
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


from .debug_key_value_pairs import DebugKeyValuePairs  # noqa: E402

DebugMapValue.update_forward_refs()
