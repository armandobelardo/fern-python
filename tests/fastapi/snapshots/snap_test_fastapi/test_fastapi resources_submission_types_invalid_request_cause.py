# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .custom_test_cases_unsupported import (
    CustomTestCasesUnsupported as resources_submission_types_custom_test_cases_unsupported_CustomTestCasesUnsupported,
)
from .submission_id_not_found import (
    SubmissionIdNotFound as resources_submission_types_submission_id_not_found_SubmissionIdNotFound,
)
from .unexpected_language_error import UnexpectedLanguageError

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def submission_id_not_found(
        self, value: resources_submission_types_submission_id_not_found_SubmissionIdNotFound
    ) -> InvalidRequestCause:
        return InvalidRequestCause(
            __root__=_InvalidRequestCause.SubmissionIdNotFound(**dict(value), type="submissionIdNotFound")
        )

    def custom_test_cases_unsupported(
        self, value: resources_submission_types_custom_test_cases_unsupported_CustomTestCasesUnsupported
    ) -> InvalidRequestCause:
        return InvalidRequestCause(
            __root__=_InvalidRequestCause.CustomTestCasesUnsupported(**dict(value), type="customTestCasesUnsupported")
        )

    def unexpected_language(self, value: UnexpectedLanguageError) -> InvalidRequestCause:
        return InvalidRequestCause(
            __root__=_InvalidRequestCause.UnexpectedLanguage(**dict(value), type="unexpectedLanguage")
        )


class InvalidRequestCause(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _InvalidRequestCause.SubmissionIdNotFound,
        _InvalidRequestCause.CustomTestCasesUnsupported,
        _InvalidRequestCause.UnexpectedLanguage,
    ]:
        return self.__root__

    def visit(
        self,
        submission_id_not_found: typing.Callable[
            [resources_submission_types_submission_id_not_found_SubmissionIdNotFound], T_Result
        ],
        custom_test_cases_unsupported: typing.Callable[
            [resources_submission_types_custom_test_cases_unsupported_CustomTestCasesUnsupported], T_Result
        ],
        unexpected_language: typing.Callable[[UnexpectedLanguageError], T_Result],
    ) -> T_Result:
        if self.__root__.type == "submissionIdNotFound":
            return submission_id_not_found(self.__root__)
        if self.__root__.type == "customTestCasesUnsupported":
            return custom_test_cases_unsupported(self.__root__)
        if self.__root__.type == "unexpectedLanguage":
            return unexpected_language(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _InvalidRequestCause.SubmissionIdNotFound,
            _InvalidRequestCause.CustomTestCasesUnsupported,
            _InvalidRequestCause.UnexpectedLanguage,
        ],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @InvalidRequestCause.Validators.validate
            def validate(value: typing.Union[_InvalidRequestCause.SubmissionIdNotFound, _InvalidRequestCause.CustomTestCasesUnsupported, _InvalidRequestCause.UnexpectedLanguage]) -> typing.Union[_InvalidRequestCause.SubmissionIdNotFound, _InvalidRequestCause.CustomTestCasesUnsupported, _InvalidRequestCause.UnexpectedLanguage]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _InvalidRequestCause.SubmissionIdNotFound,
                            _InvalidRequestCause.CustomTestCasesUnsupported,
                            _InvalidRequestCause.UnexpectedLanguage,
                        ]
                    ],
                    typing.Union[
                        _InvalidRequestCause.SubmissionIdNotFound,
                        _InvalidRequestCause.CustomTestCasesUnsupported,
                        _InvalidRequestCause.UnexpectedLanguage,
                    ],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _InvalidRequestCause.SubmissionIdNotFound,
                        _InvalidRequestCause.CustomTestCasesUnsupported,
                        _InvalidRequestCause.UnexpectedLanguage,
                    ]
                ],
                typing.Union[
                    _InvalidRequestCause.SubmissionIdNotFound,
                    _InvalidRequestCause.CustomTestCasesUnsupported,
                    _InvalidRequestCause.UnexpectedLanguage,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _InvalidRequestCause.SubmissionIdNotFound,
                _InvalidRequestCause.CustomTestCasesUnsupported,
                _InvalidRequestCause.UnexpectedLanguage,
            ],
            values.get("__root__"),
        )
        for validator in InvalidRequestCause.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: lambda v: v.isoformat()}


class _InvalidRequestCause:
    class SubmissionIdNotFound(resources_submission_types_submission_id_not_found_SubmissionIdNotFound):
        type: typing_extensions.Literal["submissionIdNotFound"]

        class Config:
            frozen = True
            json_encoders = {dt.datetime: lambda v: v.isoformat()}

    class CustomTestCasesUnsupported(
        resources_submission_types_custom_test_cases_unsupported_CustomTestCasesUnsupported
    ):
        type: typing_extensions.Literal["customTestCasesUnsupported"]

        class Config:
            frozen = True
            json_encoders = {dt.datetime: lambda v: v.isoformat()}

    class UnexpectedLanguage(UnexpectedLanguageError):
        type: typing_extensions.Literal["unexpectedLanguage"]

        class Config:
            frozen = True
            json_encoders = {dt.datetime: lambda v: v.isoformat()}


InvalidRequestCause.update_forward_refs()
