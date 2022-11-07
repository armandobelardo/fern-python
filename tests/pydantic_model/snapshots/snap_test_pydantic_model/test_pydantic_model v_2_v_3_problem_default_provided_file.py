# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.variable_type import VariableType
from .file_info_v_2 import FileInfoV2


class DefaultProvidedFile(pydantic.BaseModel):
    file: FileInfoV2
    related_types: typing.List[VariableType]

    class Partial(typing_extensions.TypedDict):
        file: typing_extensions.NotRequired[FileInfoV2]
        related_types: typing_extensions.NotRequired[typing.List[VariableType]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DefaultProvidedFile.Validators.root
            def validate(values: DefaultProvidedFile.Partial) -> DefaultProvidedFile.Partial:
                ...

            @DefaultProvidedFile.Validators.field("file")
            def validate_file(file: FileInfoV2, values: DefaultProvidedFile.Partial) -> FileInfoV2:
                ...

            @DefaultProvidedFile.Validators.field("related_types")
            def validate_related_types(related_types: typing.List[VariableType], values: DefaultProvidedFile.Partial) -> typing.List[VariableType]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[DefaultProvidedFile.Partial], DefaultProvidedFile.Partial]]
        ] = []
        _file_validators: typing.ClassVar[typing.List[DefaultProvidedFile.Validators.FileValidator]] = []
        _related_types_validators: typing.ClassVar[
            typing.List[DefaultProvidedFile.Validators.RelatedTypesValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[DefaultProvidedFile.Partial], DefaultProvidedFile.Partial]
        ) -> typing.Callable[[DefaultProvidedFile.Partial], DefaultProvidedFile.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file"]
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators.FileValidator], DefaultProvidedFile.Validators.FileValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["related_types"]
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators.RelatedTypesValidator], DefaultProvidedFile.Validators.RelatedTypesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "file":
                    cls._file_validators.append(validator)
                if field_name == "related_types":
                    cls._related_types_validators.append(validator)
                return validator

            return decorator

        class FileValidator(typing_extensions.Protocol):
            def __call__(self, __v: FileInfoV2, __values: DefaultProvidedFile.Partial) -> FileInfoV2:
                ...

        class RelatedTypesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[VariableType], __values: DefaultProvidedFile.Partial
            ) -> typing.List[VariableType]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: DefaultProvidedFile.Partial) -> DefaultProvidedFile.Partial:
        for validator in DefaultProvidedFile.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("file")
    def _validate_file(cls, v: FileInfoV2, values: DefaultProvidedFile.Partial) -> FileInfoV2:
        for validator in DefaultProvidedFile.Validators._file_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("related_types")
    def _validate_related_types(
        cls, v: typing.List[VariableType], values: DefaultProvidedFile.Partial
    ) -> typing.List[VariableType]:
        for validator in DefaultProvidedFile.Validators._related_types_validators:
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
