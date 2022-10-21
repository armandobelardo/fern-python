# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .function_implementation_for_multiple_languages import FunctionImplementationForMultipleLanguages
from .parameter import Parameter


class VoidFunctionDefinitionThatTakesActualResult(pydantic.BaseModel):
    additional_parameters: typing.List[Parameter] = pydantic.Field(alias="additionalParameters")
    code: FunctionImplementationForMultipleLanguages

    class Partial(typing_extensions.TypedDict):
        additional_parameters: typing_extensions.NotRequired[typing.List[Parameter]]
        code: typing_extensions.NotRequired[FunctionImplementationForMultipleLanguages]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VoidFunctionDefinitionThatTakesActualResult.Validators.root
            def validate(values: VoidFunctionDefinitionThatTakesActualResult.Partial) -> VoidFunctionDefinitionThatTakesActualResult.Partial:
                ...

            @VoidFunctionDefinitionThatTakesActualResult.Validators.field("additional_parameters")
            def validate_additional_parameters(v: typing.List[Parameter], values: VoidFunctionDefinitionThatTakesActualResult.Partial) -> typing.List[Parameter]:
                ...

            @VoidFunctionDefinitionThatTakesActualResult.Validators.field("code")
            def validate_code(v: FunctionImplementationForMultipleLanguages, values: VoidFunctionDefinitionThatTakesActualResult.Partial) -> FunctionImplementationForMultipleLanguages:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [VoidFunctionDefinitionThatTakesActualResult.Partial],
                    VoidFunctionDefinitionThatTakesActualResult.Partial,
                ]
            ]
        ] = []
        _additional_parameters_validators: typing.ClassVar[
            typing.List[VoidFunctionDefinitionThatTakesActualResult.Validators.AdditionalParametersValidator]
        ] = []
        _code_validators: typing.ClassVar[
            typing.List[VoidFunctionDefinitionThatTakesActualResult.Validators.CodeValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [VoidFunctionDefinitionThatTakesActualResult.Partial],
                VoidFunctionDefinitionThatTakesActualResult.Partial,
            ],
        ) -> typing.Callable[
            [VoidFunctionDefinitionThatTakesActualResult.Partial], VoidFunctionDefinitionThatTakesActualResult.Partial
        ]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["additional_parameters"]
        ) -> typing.Callable[
            [VoidFunctionDefinitionThatTakesActualResult.Validators.AdditionalParametersValidator],
            VoidFunctionDefinitionThatTakesActualResult.Validators.AdditionalParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code"]
        ) -> typing.Callable[
            [VoidFunctionDefinitionThatTakesActualResult.Validators.CodeValidator],
            VoidFunctionDefinitionThatTakesActualResult.Validators.CodeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "additional_parameters":
                    cls._additional_parameters_validators.append(validator)
                if field_name == "code":
                    cls._code_validators.append(validator)
                return validator

            return decorator

        class AdditionalParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[Parameter], *, values: VoidFunctionDefinitionThatTakesActualResult.Partial
            ) -> typing.List[Parameter]:
                ...

        class CodeValidator(typing_extensions.Protocol):
            def __call__(
                self,
                v: FunctionImplementationForMultipleLanguages,
                *,
                values: VoidFunctionDefinitionThatTakesActualResult.Partial,
            ) -> FunctionImplementationForMultipleLanguages:
                ...

    @pydantic.root_validator
    def _validate(
        cls, values: VoidFunctionDefinitionThatTakesActualResult.Partial
    ) -> VoidFunctionDefinitionThatTakesActualResult.Partial:
        for validator in VoidFunctionDefinitionThatTakesActualResult.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("additional_parameters")
    def _validate_additional_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionDefinitionThatTakesActualResult.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionDefinitionThatTakesActualResult.Validators._additional_parameters_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("code")
    def _validate_code(
        cls, v: FunctionImplementationForMultipleLanguages, values: VoidFunctionDefinitionThatTakesActualResult.Partial
    ) -> FunctionImplementationForMultipleLanguages:
        for validator in VoidFunctionDefinitionThatTakesActualResult.Validators._code_validators:
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
