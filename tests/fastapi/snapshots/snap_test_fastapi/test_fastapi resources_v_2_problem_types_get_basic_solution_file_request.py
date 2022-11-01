# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .non_void_function_signature import NonVoidFunctionSignature


class GetBasicSolutionFileRequest(pydantic.BaseModel):
    method_name: str = pydantic.Field(alias="methodName")
    signature: NonVoidFunctionSignature

    class Partial(typing_extensions.TypedDict):
        method_name: typing_extensions.NotRequired[str]
        signature: typing_extensions.NotRequired[NonVoidFunctionSignature]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetBasicSolutionFileRequest.Validators.root
            def validate(values: GetBasicSolutionFileRequest.Partial) -> GetBasicSolutionFileRequest.Partial:
                ...

            @GetBasicSolutionFileRequest.Validators.field("method_name")
            def validate_method_name(method_name: str, values: GetBasicSolutionFileRequest.Partial) -> str:
                ...

            @GetBasicSolutionFileRequest.Validators.field("signature")
            def validate_signature(signature: NonVoidFunctionSignature, values: GetBasicSolutionFileRequest.Partial) -> NonVoidFunctionSignature:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[GetBasicSolutionFileRequest.Partial], GetBasicSolutionFileRequest.Partial]]
        ] = []
        _method_name_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileRequest.Validators.MethodNameValidator]
        ] = []
        _signature_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileRequest.Validators.SignatureValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[GetBasicSolutionFileRequest.Partial], GetBasicSolutionFileRequest.Partial]
        ) -> typing.Callable[[GetBasicSolutionFileRequest.Partial], GetBasicSolutionFileRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"]
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators.MethodNameValidator],
            GetBasicSolutionFileRequest.Validators.MethodNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"]
        ) -> typing.Callable[
            [GetBasicSolutionFileRequest.Validators.SignatureValidator],
            GetBasicSolutionFileRequest.Validators.SignatureValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "method_name":
                    cls._method_name_validators.append(validator)
                if field_name == "signature":
                    cls._signature_validators.append(validator)
                return validator

            return decorator

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, *, method_name: str, values: GetBasicSolutionFileRequest.Partial) -> str:
                ...

        class SignatureValidator(typing_extensions.Protocol):
            def __call__(
                self, *, signature: NonVoidFunctionSignature, values: GetBasicSolutionFileRequest.Partial
            ) -> NonVoidFunctionSignature:
                ...

    @pydantic.root_validator
    def _validate(cls, values: GetBasicSolutionFileRequest.Partial) -> GetBasicSolutionFileRequest.Partial:
        for validator in GetBasicSolutionFileRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("method_name")
    def _validate_method_name(cls, method_name: str, values: GetBasicSolutionFileRequest.Partial) -> str:
        for validator in GetBasicSolutionFileRequest.Validators._method_name_validators:
            method_name = validator(method_name, values=values)
        return method_name

    @pydantic.validator("signature")
    def _validate_signature(
        cls, signature: NonVoidFunctionSignature, values: GetBasicSolutionFileRequest.Partial
    ) -> NonVoidFunctionSignature:
        for validator in GetBasicSolutionFileRequest.Validators._signature_validators:
            signature = validator(signature, values=values)
        return signature

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
