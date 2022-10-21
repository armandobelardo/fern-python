# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.language import Language
from .files import Files


class GeneratedFiles(pydantic.BaseModel):
    generated_test_case_files: typing.Dict[Language, Files] = pydantic.Field(alias="generatedTestCaseFiles")
    generated_template_files: typing.Dict[Language, Files] = pydantic.Field(alias="generatedTemplateFiles")
    other: typing.Dict[Language, Files]

    class Partial(typing_extensions.TypedDict):
        generated_test_case_files: typing_extensions.NotRequired[typing.Dict[Language, Files]]
        generated_template_files: typing_extensions.NotRequired[typing.Dict[Language, Files]]
        other: typing_extensions.NotRequired[typing.Dict[Language, Files]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GeneratedFiles.Validators.root
            def validate(values: GeneratedFiles.Partial) -> GeneratedFiles.Partial:
                ...

            @GeneratedFiles.Validators.field("generated_test_case_files")
            def validate_generated_test_case_files(v: typing.Dict[Language, Files], values: GeneratedFiles.Partial) -> typing.Dict[Language, Files]:
                ...

            @GeneratedFiles.Validators.field("generated_template_files")
            def validate_generated_template_files(v: typing.Dict[Language, Files], values: GeneratedFiles.Partial) -> typing.Dict[Language, Files]:
                ...

            @GeneratedFiles.Validators.field("other")
            def validate_other(v: typing.Dict[Language, Files], values: GeneratedFiles.Partial) -> typing.Dict[Language, Files]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[GeneratedFiles.Partial], GeneratedFiles.Partial]]
        ] = []
        _generated_test_case_files_validators: typing.ClassVar[
            typing.List[GeneratedFiles.Validators.GeneratedTestCaseFilesValidator]
        ] = []
        _generated_template_files_validators: typing.ClassVar[
            typing.List[GeneratedFiles.Validators.GeneratedTemplateFilesValidator]
        ] = []
        _other_validators: typing.ClassVar[typing.List[GeneratedFiles.Validators.OtherValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[GeneratedFiles.Partial], GeneratedFiles.Partial]
        ) -> typing.Callable[[GeneratedFiles.Partial], GeneratedFiles.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["generated_test_case_files"]
        ) -> typing.Callable[
            [GeneratedFiles.Validators.GeneratedTestCaseFilesValidator],
            GeneratedFiles.Validators.GeneratedTestCaseFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["generated_template_files"]
        ) -> typing.Callable[
            [GeneratedFiles.Validators.GeneratedTemplateFilesValidator],
            GeneratedFiles.Validators.GeneratedTemplateFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["other"]
        ) -> typing.Callable[[GeneratedFiles.Validators.OtherValidator], GeneratedFiles.Validators.OtherValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "generated_test_case_files":
                    cls._generated_test_case_files_validators.append(validator)
                if field_name == "generated_template_files":
                    cls._generated_template_files_validators.append(validator)
                if field_name == "other":
                    cls._other_validators.append(validator)
                return validator

            return decorator

        class GeneratedTestCaseFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, Files], *, values: GeneratedFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

        class GeneratedTemplateFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, Files], *, values: GeneratedFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

        class OtherValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, Files], *, values: GeneratedFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: GeneratedFiles.Partial) -> GeneratedFiles.Partial:
        for validator in GeneratedFiles.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("generated_test_case_files")
    def _validate_generated_test_case_files(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._generated_test_case_files_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("generated_template_files")
    def _validate_generated_template_files(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._generated_template_files_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("other")
    def _validate_other(
        cls, v: typing.Dict[Language, Files], values: GeneratedFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in GeneratedFiles.Validators._other_validators:
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
