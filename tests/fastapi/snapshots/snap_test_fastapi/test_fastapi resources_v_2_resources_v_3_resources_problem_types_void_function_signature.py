# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ........core.datetime_utils import serialize_datetime
from .parameter import Parameter


class VoidFunctionSignature(pydantic.BaseModel):
    parameters: typing.List[Parameter]

    class Partial(typing_extensions.TypedDict):
        parameters: typing_extensions.NotRequired[typing.List[Parameter]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VoidFunctionSignature.Validators.root()
            def validate(values: VoidFunctionSignature.Partial) -> VoidFunctionSignature.Partial:
                ...

            @VoidFunctionSignature.Validators.field("parameters")
            def validate_parameters(parameters: typing.List[Parameter], values: VoidFunctionSignature.Partial) -> typing.List[Parameter]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[VoidFunctionSignature.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[VoidFunctionSignature.Validators._RootValidator]] = []
        _parameters_pre_validators: typing.ClassVar[
            typing.List[VoidFunctionSignature.Validators.PreParametersValidator]
        ] = []
        _parameters_post_validators: typing.ClassVar[
            typing.List[VoidFunctionSignature.Validators.ParametersValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [VoidFunctionSignature.Validators._RootValidator], VoidFunctionSignature.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VoidFunctionSignature.Validators._PreRootValidator], VoidFunctionSignature.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["parameters"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VoidFunctionSignature.Validators.PreParametersValidator],
            VoidFunctionSignature.Validators.PreParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["parameters"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [VoidFunctionSignature.Validators.ParametersValidator], VoidFunctionSignature.Validators.ParametersValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameters":
                    if pre:
                        cls._parameters_pre_validators.append(validator)
                    else:
                        cls._parameters_post_validators.append(validator)
                return validator

            return decorator

        class PreParametersValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: VoidFunctionSignature.Partial) -> typing.Any:
                ...

        class ParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[Parameter], __values: VoidFunctionSignature.Partial
            ) -> typing.List[Parameter]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: VoidFunctionSignature.Partial) -> VoidFunctionSignature.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_v_2_v_3_void_function_signature_validate(
        cls, values: VoidFunctionSignature.Partial
    ) -> VoidFunctionSignature.Partial:
        for validator in VoidFunctionSignature.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_v_2_v_3_void_function_signature_validate(
        cls, values: VoidFunctionSignature.Partial
    ) -> VoidFunctionSignature.Partial:
        for validator in VoidFunctionSignature.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("parameters", pre=True)
    def _pre_validate_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionSignature.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionSignature.Validators._parameters_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("parameters", pre=False)
    def _post_validate_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionSignature.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionSignature.Validators._parameters_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
