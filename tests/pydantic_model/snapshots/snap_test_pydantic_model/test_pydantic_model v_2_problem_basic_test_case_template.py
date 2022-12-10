# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .parameter_id import ParameterId
from .test_case_implementation_description import TestCaseImplementationDescription
from .test_case_template_id import TestCaseTemplateId


class BasicTestCaseTemplate(pydantic.BaseModel):
    template_id: TestCaseTemplateId = pydantic.Field(alias="templateId")
    name: str
    description: TestCaseImplementationDescription
    expected_value_parameter_id: ParameterId = pydantic.Field(alias="expectedValueParameterId")

    class Partial(typing_extensions.TypedDict):
        template_id: typing_extensions.NotRequired[TestCaseTemplateId]
        name: typing_extensions.NotRequired[str]
        description: typing_extensions.NotRequired[TestCaseImplementationDescription]
        expected_value_parameter_id: typing_extensions.NotRequired[ParameterId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BasicTestCaseTemplate.Validators.root()
            def validate(values: BasicTestCaseTemplate.Partial) -> BasicTestCaseTemplate.Partial:
                ...

            @BasicTestCaseTemplate.Validators.field("template_id")
            def validate_template_id(template_id: TestCaseTemplateId, values: BasicTestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

            @BasicTestCaseTemplate.Validators.field("name")
            def validate_name(name: str, values: BasicTestCaseTemplate.Partial) -> str:
                ...

            @BasicTestCaseTemplate.Validators.field("description")
            def validate_description(description: TestCaseImplementationDescription, values: BasicTestCaseTemplate.Partial) -> TestCaseImplementationDescription:
                ...

            @BasicTestCaseTemplate.Validators.field("expected_value_parameter_id")
            def validate_expected_value_parameter_id(expected_value_parameter_id: ParameterId, values: BasicTestCaseTemplate.Partial) -> ParameterId:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[BasicTestCaseTemplate.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[BasicTestCaseTemplate.Validators._RootValidator]] = []
        _template_id_pre_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.PreTemplateIdValidator]
        ] = []
        _template_id_post_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.TemplateIdValidator]
        ] = []
        _name_pre_validators: typing.ClassVar[typing.List[BasicTestCaseTemplate.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[BasicTestCaseTemplate.Validators.NameValidator]] = []
        _description_pre_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.PreDescriptionValidator]
        ] = []
        _description_post_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.DescriptionValidator]
        ] = []
        _expected_value_parameter_id_pre_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.PreExpectedValueParameterIdValidator]
        ] = []
        _expected_value_parameter_id_post_validators: typing.ClassVar[
            typing.List[BasicTestCaseTemplate.Validators.ExpectedValueParameterIdValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators._RootValidator], BasicTestCaseTemplate.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators._PreRootValidator], BasicTestCaseTemplate.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["template_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.PreTemplateIdValidator],
            BasicTestCaseTemplate.Validators.PreTemplateIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.TemplateIdValidator], BasicTestCaseTemplate.Validators.TemplateIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.PreNameValidator], BasicTestCaseTemplate.Validators.PreNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.NameValidator], BasicTestCaseTemplate.Validators.NameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["description"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.PreDescriptionValidator],
            BasicTestCaseTemplate.Validators.PreDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["description"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.DescriptionValidator],
            BasicTestCaseTemplate.Validators.DescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["expected_value_parameter_id"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.PreExpectedValueParameterIdValidator],
            BasicTestCaseTemplate.Validators.PreExpectedValueParameterIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["expected_value_parameter_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [BasicTestCaseTemplate.Validators.ExpectedValueParameterIdValidator],
            BasicTestCaseTemplate.Validators.ExpectedValueParameterIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template_id":
                    if pre:
                        cls._template_id_pre_validators.append(validator)
                    else:
                        cls._template_id_post_validators.append(validator)
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                if field_name == "description":
                    if pre:
                        cls._description_pre_validators.append(validator)
                    else:
                        cls._description_post_validators.append(validator)
                if field_name == "expected_value_parameter_id":
                    if pre:
                        cls._expected_value_parameter_id_pre_validators.append(validator)
                    else:
                        cls._expected_value_parameter_id_post_validators.append(validator)
                return validator

            return decorator

        class PreTemplateIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicTestCaseTemplate.Partial) -> typing.Any:
                ...

        class TemplateIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseTemplateId, __values: BasicTestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicTestCaseTemplate.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: BasicTestCaseTemplate.Partial) -> str:
                ...

        class PreDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicTestCaseTemplate.Partial) -> typing.Any:
                ...

        class DescriptionValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseImplementationDescription, __values: BasicTestCaseTemplate.Partial
            ) -> TestCaseImplementationDescription:
                ...

        class PreExpectedValueParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicTestCaseTemplate.Partial) -> typing.Any:
                ...

        class ExpectedValueParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ParameterId, __values: BasicTestCaseTemplate.Partial) -> ParameterId:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: BasicTestCaseTemplate.Partial) -> BasicTestCaseTemplate.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: BasicTestCaseTemplate.Partial) -> BasicTestCaseTemplate.Partial:
        for validator in BasicTestCaseTemplate.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: BasicTestCaseTemplate.Partial) -> BasicTestCaseTemplate.Partial:
        for validator in BasicTestCaseTemplate.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("template_id", pre=True)
    def _pre_validate_template_id(
        cls, v: TestCaseTemplateId, values: BasicTestCaseTemplate.Partial
    ) -> TestCaseTemplateId:
        for validator in BasicTestCaseTemplate.Validators._template_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("template_id", pre=False)
    def _post_validate_template_id(
        cls, v: TestCaseTemplateId, values: BasicTestCaseTemplate.Partial
    ) -> TestCaseTemplateId:
        for validator in BasicTestCaseTemplate.Validators._template_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: BasicTestCaseTemplate.Partial) -> str:
        for validator in BasicTestCaseTemplate.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: BasicTestCaseTemplate.Partial) -> str:
        for validator in BasicTestCaseTemplate.Validators._name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("description", pre=True)
    def _pre_validate_description(
        cls, v: TestCaseImplementationDescription, values: BasicTestCaseTemplate.Partial
    ) -> TestCaseImplementationDescription:
        for validator in BasicTestCaseTemplate.Validators._description_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("description", pre=False)
    def _post_validate_description(
        cls, v: TestCaseImplementationDescription, values: BasicTestCaseTemplate.Partial
    ) -> TestCaseImplementationDescription:
        for validator in BasicTestCaseTemplate.Validators._description_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_value_parameter_id", pre=True)
    def _pre_validate_expected_value_parameter_id(
        cls, v: ParameterId, values: BasicTestCaseTemplate.Partial
    ) -> ParameterId:
        for validator in BasicTestCaseTemplate.Validators._expected_value_parameter_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_value_parameter_id", pre=False)
    def _post_validate_expected_value_parameter_id(
        cls, v: ParameterId, values: BasicTestCaseTemplate.Partial
    ) -> ParameterId:
        for validator in BasicTestCaseTemplate.Validators._expected_value_parameter_id_post_validators:
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
        allow_population_by_field_name = True
