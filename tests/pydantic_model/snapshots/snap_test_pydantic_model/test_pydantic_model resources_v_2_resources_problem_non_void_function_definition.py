# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .....core.datetime_utils import serialize_datetime
from .function_implementation_for_multiple_languages import FunctionImplementationForMultipleLanguages
from .non_void_function_signature import NonVoidFunctionSignature


class NonVoidFunctionDefinition(pydantic.BaseModel):
    signature: NonVoidFunctionSignature
    code: FunctionImplementationForMultipleLanguages

    class Partial(typing_extensions.TypedDict):
        signature: typing_extensions.NotRequired[NonVoidFunctionSignature]
        code: typing_extensions.NotRequired[FunctionImplementationForMultipleLanguages]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @NonVoidFunctionDefinition.Validators.root()
            def validate(values: NonVoidFunctionDefinition.Partial) -> NonVoidFunctionDefinition.Partial:
                ...

            @NonVoidFunctionDefinition.Validators.field("signature")
            def validate_signature(signature: NonVoidFunctionSignature, values: NonVoidFunctionDefinition.Partial) -> NonVoidFunctionSignature:
                ...

            @NonVoidFunctionDefinition.Validators.field("code")
            def validate_code(code: FunctionImplementationForMultipleLanguages, values: NonVoidFunctionDefinition.Partial) -> FunctionImplementationForMultipleLanguages:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[NonVoidFunctionDefinition.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[NonVoidFunctionDefinition.Validators._RootValidator]] = []
        _signature_pre_validators: typing.ClassVar[
            typing.List[NonVoidFunctionDefinition.Validators.PreSignatureValidator]
        ] = []
        _signature_post_validators: typing.ClassVar[
            typing.List[NonVoidFunctionDefinition.Validators.SignatureValidator]
        ] = []
        _code_pre_validators: typing.ClassVar[typing.List[NonVoidFunctionDefinition.Validators.PreCodeValidator]] = []
        _code_post_validators: typing.ClassVar[typing.List[NonVoidFunctionDefinition.Validators.CodeValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators._RootValidator], NonVoidFunctionDefinition.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators._PreRootValidator],
            NonVoidFunctionDefinition.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["signature"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators.PreSignatureValidator],
            NonVoidFunctionDefinition.Validators.PreSignatureValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators.SignatureValidator],
            NonVoidFunctionDefinition.Validators.SignatureValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators.PreCodeValidator],
            NonVoidFunctionDefinition.Validators.PreCodeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [NonVoidFunctionDefinition.Validators.CodeValidator], NonVoidFunctionDefinition.Validators.CodeValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "signature":
                    if pre:
                        cls._signature_pre_validators.append(validator)
                    else:
                        cls._signature_post_validators.append(validator)
                if field_name == "code":
                    if pre:
                        cls._code_pre_validators.append(validator)
                    else:
                        cls._code_post_validators.append(validator)
                return validator

            return decorator

        class PreSignatureValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: NonVoidFunctionDefinition.Partial) -> typing.Any:
                ...

        class SignatureValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: NonVoidFunctionSignature, __values: NonVoidFunctionDefinition.Partial
            ) -> NonVoidFunctionSignature:
                ...

        class PreCodeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: NonVoidFunctionDefinition.Partial) -> typing.Any:
                ...

        class CodeValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: FunctionImplementationForMultipleLanguages, __values: NonVoidFunctionDefinition.Partial
            ) -> FunctionImplementationForMultipleLanguages:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: NonVoidFunctionDefinition.Partial) -> NonVoidFunctionDefinition.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_v_2_non_void_function_definition_validate(
        cls, values: NonVoidFunctionDefinition.Partial
    ) -> NonVoidFunctionDefinition.Partial:
        for validator in NonVoidFunctionDefinition.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_v_2_non_void_function_definition_validate(
        cls, values: NonVoidFunctionDefinition.Partial
    ) -> NonVoidFunctionDefinition.Partial:
        for validator in NonVoidFunctionDefinition.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("signature", pre=True)
    def _pre_validate_signature(
        cls, v: NonVoidFunctionSignature, values: NonVoidFunctionDefinition.Partial
    ) -> NonVoidFunctionSignature:
        for validator in NonVoidFunctionDefinition.Validators._signature_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("signature", pre=False)
    def _post_validate_signature(
        cls, v: NonVoidFunctionSignature, values: NonVoidFunctionDefinition.Partial
    ) -> NonVoidFunctionSignature:
        for validator in NonVoidFunctionDefinition.Validators._signature_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("code", pre=True)
    def _pre_validate_code(
        cls, v: FunctionImplementationForMultipleLanguages, values: NonVoidFunctionDefinition.Partial
    ) -> FunctionImplementationForMultipleLanguages:
        for validator in NonVoidFunctionDefinition.Validators._code_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("code", pre=False)
    def _post_validate_code(
        cls, v: FunctionImplementationForMultipleLanguages, values: NonVoidFunctionDefinition.Partial
    ) -> FunctionImplementationForMultipleLanguages:
        for validator in NonVoidFunctionDefinition.Validators._code_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        json_encoders = {dt.datetime: serialize_datetime}
