# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .migration_status import MigrationStatus


class Migration(pydantic.BaseModel):
    name: str
    status: MigrationStatus

    class Partial(typing_extensions.TypedDict):
        name: typing_extensions.NotRequired[str]
        status: typing_extensions.NotRequired[MigrationStatus]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Migration.Validators.root()
            def validate(values: Migration.Partial) -> Migration.Partial:
                ...

            @Migration.Validators.field("name")
            def validate_name(name: str, values: Migration.Partial) -> str:
                ...

            @Migration.Validators.field("status")
            def validate_status(status: MigrationStatus, values: Migration.Partial) -> MigrationStatus:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[Migration.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[Migration.Validators._RootValidator]] = []
        _name_pre_validators: typing.ClassVar[typing.List[Migration.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[Migration.Validators.NameValidator]] = []
        _status_pre_validators: typing.ClassVar[typing.List[Migration.Validators.PreStatusValidator]] = []
        _status_post_validators: typing.ClassVar[typing.List[Migration.Validators.StatusValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Migration.Validators._RootValidator], Migration.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Migration.Validators._PreRootValidator], Migration.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Migration.Validators.PreNameValidator], Migration.Validators.PreNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Migration.Validators.NameValidator], Migration.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Migration.Validators.PreStatusValidator], Migration.Validators.PreStatusValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Migration.Validators.StatusValidator], Migration.Validators.StatusValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                if field_name == "status":
                    if pre:
                        cls._status_pre_validators.append(validator)
                    else:
                        cls._status_post_validators.append(validator)
                return validator

            return decorator

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Migration.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: Migration.Partial) -> str:
                ...

        class PreStatusValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Migration.Partial) -> typing.Any:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(self, __v: MigrationStatus, __values: Migration.Partial) -> MigrationStatus:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: Migration.Partial) -> Migration.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_migration_validate(cls, values: Migration.Partial) -> Migration.Partial:
        for validator in Migration.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_migration_validate(cls, values: Migration.Partial) -> Migration.Partial:
        for validator in Migration.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: Migration.Partial) -> str:
        for validator in Migration.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: Migration.Partial) -> str:
        for validator in Migration.Validators._name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=True)
    def _pre_validate_status(cls, v: MigrationStatus, values: Migration.Partial) -> MigrationStatus:
        for validator in Migration.Validators._status_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=False)
    def _post_validate_status(cls, v: MigrationStatus, values: Migration.Partial) -> MigrationStatus:
        for validator in Migration.Validators._status_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        json_encoders = {dt.datetime: serialize_datetime}
