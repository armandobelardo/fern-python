# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_submission_update_info import TestSubmissionUpdateInfo


class TestSubmissionUpdate(pydantic.BaseModel):
    update_time: str = pydantic.Field(alias="updateTime")
    update_info: TestSubmissionUpdateInfo = pydantic.Field(alias="updateInfo")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestSubmissionUpdate.Validators.root
            def validate(values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdate.Partial:
                ...

            @TestSubmissionUpdate.Validators.field("update_time")
            def validate_update_time(v: str, values: TestSubmissionUpdate.Partial) -> str:
                ...

            @TestSubmissionUpdate.Validators.field("update_info")
            def validate_update_info(v: TestSubmissionUpdateInfo, values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdateInfo:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TestSubmissionUpdate.Partial], TestSubmissionUpdate.Partial]]
        ] = []
        _update_time_validators: typing.ClassVar[typing.List[TestSubmissionUpdate.Validators.UpdateTimeValidator]] = []
        _update_info_validators: typing.ClassVar[typing.List[TestSubmissionUpdate.Validators.UpdateInfoValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestSubmissionUpdate.Partial], TestSubmissionUpdate.Partial]
        ) -> typing.Callable[[TestSubmissionUpdate.Partial], TestSubmissionUpdate.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["update_time"]
        ) -> typing.Callable[
            [TestSubmissionUpdate.Validators.UpdateTimeValidator], TestSubmissionUpdate.Validators.UpdateTimeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["update_info"]
        ) -> typing.Callable[
            [TestSubmissionUpdate.Validators.UpdateInfoValidator], TestSubmissionUpdate.Validators.UpdateInfoValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "update_time":
                    cls._update_time_validators.append(validator)
                if field_name == "update_info":
                    cls._update_info_validators.append(validator)
                return validator

            return decorator

        class UpdateTimeValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TestSubmissionUpdate.Partial) -> str:
                ...

        class UpdateInfoValidator(typing_extensions.Protocol):
            def __call__(
                self, v: TestSubmissionUpdateInfo, *, values: TestSubmissionUpdate.Partial
            ) -> TestSubmissionUpdateInfo:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestSubmissionUpdate.Partial) -> TestSubmissionUpdate.Partial:
        for validator in TestSubmissionUpdate.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("update_time")
    def _validate_update_time(cls, v: str, values: TestSubmissionUpdate.Partial) -> str:
        for validator in TestSubmissionUpdate.Validators._update_time_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("update_info")
    def _validate_update_info(
        cls, v: TestSubmissionUpdateInfo, values: TestSubmissionUpdate.Partial
    ) -> TestSubmissionUpdateInfo:
        for validator in TestSubmissionUpdate.Validators._update_info_validators:
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
