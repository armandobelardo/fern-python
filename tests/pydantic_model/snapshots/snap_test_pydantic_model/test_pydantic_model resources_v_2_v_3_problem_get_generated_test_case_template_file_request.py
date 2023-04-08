# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .....core.datetime_utils import serialize_datetime
from .test_case_template import TestCaseTemplate


class GetGeneratedTestCaseTemplateFileRequest(pydantic.BaseModel):
    template: TestCaseTemplate

    class Partial(typing_extensions.TypedDict):
        template: typing_extensions.NotRequired[TestCaseTemplate]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetGeneratedTestCaseTemplateFileRequest.Validators.root()
            def validate(values: GetGeneratedTestCaseTemplateFileRequest.Partial) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
                ...

            @GetGeneratedTestCaseTemplateFileRequest.Validators.field("template")
            def validate_template(template: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial) -> TestCaseTemplate:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators._PreRootValidator]
        ] = []
        _post_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators._RootValidator]
        ] = []
        _template_pre_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators.PreTemplateValidator]
        ] = []
        _template_post_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetGeneratedTestCaseTemplateFileRequest.Validators._RootValidator],
            GetGeneratedTestCaseTemplateFileRequest.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetGeneratedTestCaseTemplateFileRequest.Validators._PreRootValidator],
            GetGeneratedTestCaseTemplateFileRequest.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["template"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetGeneratedTestCaseTemplateFileRequest.Validators.PreTemplateValidator],
            GetGeneratedTestCaseTemplateFileRequest.Validators.PreTemplateValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator],
            GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template":
                    if pre:
                        cls._template_pre_validators.append(validator)
                    else:
                        cls._template_post_validators.append(validator)
                return validator

            return decorator

        class PreTemplateValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Any, __values: GetGeneratedTestCaseTemplateFileRequest.Partial
            ) -> typing.Any:
                ...

        class TemplateValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseTemplate, __values: GetGeneratedTestCaseTemplateFileRequest.Partial
            ) -> TestCaseTemplate:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: GetGeneratedTestCaseTemplateFileRequest.Partial
            ) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("template", pre=True)
    def _pre_validate_template(
        cls, v: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> TestCaseTemplate:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._template_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("template", pre=False)
    def _post_validate_template(
        cls, v: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> TestCaseTemplate:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._template_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        orm_mode = True
        json_encoders = {dt.datetime: serialize_datetime}
