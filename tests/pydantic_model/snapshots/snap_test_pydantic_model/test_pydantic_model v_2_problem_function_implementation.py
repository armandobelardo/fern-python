# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class FunctionImplementation(pydantic.BaseModel):
    impl: str
    imports: typing.Optional[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FunctionImplementation.Validators.root
            def validate(values: FunctionImplementation.Partial) -> FunctionImplementation.Partial:
                ...

            @FunctionImplementation.Validators.field("impl")
            def validate_impl(v: str, values: FunctionImplementation.Partial) -> str:
                ...

            @FunctionImplementation.Validators.field("imports")
            def validate_imports(v: typing.Optional[str], values: FunctionImplementation.Partial) -> typing.Optional[str]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[FunctionImplementation.Partial], FunctionImplementation.Partial]]
        ] = []
        _impl_validators: typing.ClassVar[typing.List[FunctionImplementation.Validators.ImplValidator]] = []
        _imports_validators: typing.ClassVar[typing.List[FunctionImplementation.Validators.ImportsValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[FunctionImplementation.Partial], FunctionImplementation.Partial]
        ) -> typing.Callable[[FunctionImplementation.Partial], FunctionImplementation.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["impl"]
        ) -> typing.Callable[
            [FunctionImplementation.Validators.ImplValidator], FunctionImplementation.Validators.ImplValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["imports"]
        ) -> typing.Callable[
            [FunctionImplementation.Validators.ImportsValidator], FunctionImplementation.Validators.ImportsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "impl":
                    cls._impl_validators.append(validator)
                if field_name == "imports":
                    cls._imports_validators.append(validator)
                return validator

            return decorator

        class ImplValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: FunctionImplementation.Partial) -> str:
                ...

        class ImportsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[str], *, values: FunctionImplementation.Partial
            ) -> typing.Optional[str]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: FunctionImplementation.Partial) -> FunctionImplementation.Partial:
        for validator in FunctionImplementation.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("impl")
    def _validate_impl(cls, v: str, values: FunctionImplementation.Partial) -> str:
        for validator in FunctionImplementation.Validators._impl_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("imports")
    def _validate_imports(cls, v: typing.Optional[str], values: FunctionImplementation.Partial) -> typing.Optional[str]:
        for validator in FunctionImplementation.Validators._imports_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        impl: typing_extensions.NotRequired[str]
        imports: typing_extensions.NotRequired[typing.Optional[str]]

    class Config:
        frozen = True
