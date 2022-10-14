# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_implementation import TestCaseImplementation
from .test_case_template_id import TestCaseTemplateId


class TestCaseTemplate(pydantic.BaseModel):
    template_id: TestCaseTemplateId = pydantic.Field(alias="templateId")
    name: str
    implementation: TestCaseImplementation

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseTemplate.Validators.root
            def validate(values: TestCaseTemplate.Partial) -> TestCaseTemplate.Partial:
                ...

            @TestCaseTemplate.Validators.field("template_id")
            def validate_template_id(v: TestCaseTemplateId, values: TestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

            @TestCaseTemplate.Validators.field("name")
            def validate_name(v: str, values: TestCaseTemplate.Partial) -> str:
                ...

            @TestCaseTemplate.Validators.field("implementation")
            def validate_implementation(v: TestCaseImplementation, values: TestCaseTemplate.Partial) -> TestCaseImplementation:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TestCaseTemplate.Partial], TestCaseTemplate.Partial]]
        ] = []
        _template_id_validators: typing.ClassVar[typing.List[TestCaseTemplate.Validators.TemplateIdValidator]] = []
        _name_validators: typing.ClassVar[typing.List[TestCaseTemplate.Validators.NameValidator]] = []
        _implementation_validators: typing.ClassVar[
            typing.List[TestCaseTemplate.Validators.ImplementationValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestCaseTemplate.Partial], TestCaseTemplate.Partial]
        ) -> typing.Callable[[TestCaseTemplate.Partial], TestCaseTemplate.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template_id"]
        ) -> typing.Callable[
            [TestCaseTemplate.Validators.TemplateIdValidator], TestCaseTemplate.Validators.TemplateIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[[TestCaseTemplate.Validators.NameValidator], TestCaseTemplate.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["implementation"]
        ) -> typing.Callable[
            [TestCaseTemplate.Validators.ImplementationValidator], TestCaseTemplate.Validators.ImplementationValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template_id":
                    cls._template_id_validators.append(validator)
                if field_name == "name":
                    cls._name_validators.append(validator)
                if field_name == "implementation":
                    cls._implementation_validators.append(validator)
                return validator

            return decorator

        class TemplateIdValidator(typing_extensions.Protocol):
            def __call__(self, v: TestCaseTemplateId, *, values: TestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TestCaseTemplate.Partial) -> str:
                ...

        class ImplementationValidator(typing_extensions.Protocol):
            def __call__(
                self, v: TestCaseImplementation, *, values: TestCaseTemplate.Partial
            ) -> TestCaseImplementation:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestCaseTemplate.Partial) -> TestCaseTemplate.Partial:
        for validator in TestCaseTemplate.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("template_id")
    def _validate_template_id(cls, v: TestCaseTemplateId, values: TestCaseTemplate.Partial) -> TestCaseTemplateId:
        for validator in TestCaseTemplate.Validators._template_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("name")
    def _validate_name(cls, v: str, values: TestCaseTemplate.Partial) -> str:
        for validator in TestCaseTemplate.Validators._name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("implementation")
    def _validate_implementation(
        cls, v: TestCaseImplementation, values: TestCaseTemplate.Partial
    ) -> TestCaseImplementation:
        for validator in TestCaseTemplate.Validators._implementation_validators:
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
