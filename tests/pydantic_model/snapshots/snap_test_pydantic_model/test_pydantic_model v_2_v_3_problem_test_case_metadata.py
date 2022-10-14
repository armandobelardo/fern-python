# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_id import TestCaseId


class TestCaseMetadata(pydantic.BaseModel):
    id: TestCaseId
    name: str
    hidden: bool

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseMetadata.Validators.root
            def validate(values: TestCaseMetadata.Partial) -> TestCaseMetadata.Partial:
                ...

            @TestCaseMetadata.Validators.field("id")
            def validate_id(v: TestCaseId, values: TestCaseMetadata.Partial) -> TestCaseId:
                ...

            @TestCaseMetadata.Validators.field("name")
            def validate_name(v: str, values: TestCaseMetadata.Partial) -> str:
                ...

            @TestCaseMetadata.Validators.field("hidden")
            def validate_hidden(v: bool, values: TestCaseMetadata.Partial) -> bool:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TestCaseMetadata.Partial], TestCaseMetadata.Partial]]
        ] = []
        _id_validators: typing.ClassVar[typing.List[TestCaseMetadata.Validators.IdValidator]] = []
        _name_validators: typing.ClassVar[typing.List[TestCaseMetadata.Validators.NameValidator]] = []
        _hidden_validators: typing.ClassVar[typing.List[TestCaseMetadata.Validators.HiddenValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestCaseMetadata.Partial], TestCaseMetadata.Partial]
        ) -> typing.Callable[[TestCaseMetadata.Partial], TestCaseMetadata.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"]
        ) -> typing.Callable[[TestCaseMetadata.Validators.IdValidator], TestCaseMetadata.Validators.IdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[[TestCaseMetadata.Validators.NameValidator], TestCaseMetadata.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["hidden"]
        ) -> typing.Callable[
            [TestCaseMetadata.Validators.HiddenValidator], TestCaseMetadata.Validators.HiddenValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    cls._id_validators.append(validator)
                if field_name == "name":
                    cls._name_validators.append(validator)
                if field_name == "hidden":
                    cls._hidden_validators.append(validator)
                return validator

            return decorator

        class IdValidator(typing_extensions.Protocol):
            def __call__(self, v: TestCaseId, *, values: TestCaseMetadata.Partial) -> TestCaseId:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TestCaseMetadata.Partial) -> str:
                ...

        class HiddenValidator(typing_extensions.Protocol):
            def __call__(self, v: bool, *, values: TestCaseMetadata.Partial) -> bool:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestCaseMetadata.Partial) -> TestCaseMetadata.Partial:
        for validator in TestCaseMetadata.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("id")
    def _validate_id(cls, v: TestCaseId, values: TestCaseMetadata.Partial) -> TestCaseId:
        for validator in TestCaseMetadata.Validators._id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("name")
    def _validate_name(cls, v: str, values: TestCaseMetadata.Partial) -> str:
        for validator in TestCaseMetadata.Validators._name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("hidden")
    def _validate_hidden(cls, v: bool, values: TestCaseMetadata.Partial) -> bool:
        for validator in TestCaseMetadata.Validators._hidden_validators:
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
