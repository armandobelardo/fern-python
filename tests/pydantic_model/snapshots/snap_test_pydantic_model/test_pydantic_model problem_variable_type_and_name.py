import typing

import pydantic
import typing_extensions

from ..commons.variable_type import VariableType


class VariableTypeAndName(pydantic.BaseModel):
    variable_type: VariableType = pydantic.Field(alias="variableType")
    name: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("variable_type")
    def _validate_variable_type(cls, variable_type: VariableType) -> VariableType:
        for validator in VariableTypeAndName.Validators._variable_type_validators:
            variable_type = validator(variable_type)
        return variable_type

    @pydantic.validator("name")
    def _validate_name(cls, name: str) -> str:
        for validator in VariableTypeAndName.Validators._name_validators:
            name = validator(name)
        return name

    class Validators:
        _variable_type_validators: typing.ClassVar[typing.List[typing.Callable[[VariableType], VariableType]]] = []
        _name_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variable_type"]
        ) -> typing.Callable[
            [typing.Callable[[VariableType], VariableType]], typing.Callable[[VariableType], VariableType]
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "variable_type":
                    cls._variable_type_validators.append(validator)
                elif field_name == "name":
                    cls._name_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on VariableTypeAndName: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
