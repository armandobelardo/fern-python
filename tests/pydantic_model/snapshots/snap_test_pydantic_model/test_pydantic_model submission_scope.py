# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.debug_variable_value import DebugVariableValue


class Scope(pydantic.BaseModel):
    variables: typing.Dict[str, DebugVariableValue]

    class Partial(typing_extensions.TypedDict):
        variables: typing_extensions.NotRequired[typing.Dict[str, DebugVariableValue]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Scope.Validators.root()
            def validate(values: Scope.Partial) -> Scope.Partial:
                ...

            @Scope.Validators.field("variables")
            def validate_variables(variables: typing.Dict[str, DebugVariableValue], values: Scope.Partial) -> typing.Dict[str, DebugVariableValue]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[Scope.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[Scope.Validators._RootValidator]] = []
        _variables_pre_validators: typing.ClassVar[typing.List[Scope.Validators.PreVariablesValidator]] = []
        _variables_post_validators: typing.ClassVar[typing.List[Scope.Validators.VariablesValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Scope.Validators._RootValidator], Scope.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Scope.Validators._PreRootValidator], Scope.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["variables"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Scope.Validators.PreVariablesValidator], Scope.Validators.PreVariablesValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variables"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Scope.Validators.VariablesValidator], Scope.Validators.VariablesValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "variables":
                    if pre:
                        cls._variables_pre_validators.append(validator)
                    else:
                        cls._variables_post_validators.append(validator)
                return validator

            return decorator

        class PreVariablesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Scope.Partial) -> typing.Any:
                ...

        class VariablesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[str, DebugVariableValue], __values: Scope.Partial
            ) -> typing.Dict[str, DebugVariableValue]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: Scope.Partial) -> Scope.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: Scope.Partial) -> Scope.Partial:
        for validator in Scope.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: Scope.Partial) -> Scope.Partial:
        for validator in Scope.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("variables", pre=True)
    def _pre_validate_variables(
        cls, v: typing.Dict[str, DebugVariableValue], values: Scope.Partial
    ) -> typing.Dict[str, DebugVariableValue]:
        for validator in Scope.Validators._variables_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("variables", pre=False)
    def _post_validate_variables(
        cls, v: typing.Dict[str, DebugVariableValue], values: Scope.Partial
    ) -> typing.Dict[str, DebugVariableValue]:
        for validator in Scope.Validators._variables_post_validators:
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
