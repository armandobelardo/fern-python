from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .custom_test_cases_unsupported import CustomTestCasesUnsupported
from .submission_id_not_found import SubmissionIdNotFound
from .unexpected_language_error import UnexpectedLanguageError

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def submission_id_not_found(self, value: SubmissionIdNotFound) -> InvalidRequestCause:
        return InvalidRequestCause(
            __root__=_InvalidRequestCause.SubmissionIdNotFound(**dict(value), type="submissionIdNotFound")
        )

    def custom_test_cases_unsupported(self, value: CustomTestCasesUnsupported) -> InvalidRequestCause:
        return InvalidRequestCause(
            __root__=_InvalidRequestCause.CustomTestCasesUnsupported(**dict(value), type="customTestCasesUnsupported")
        )

    def unexpected_language(self, value: UnexpectedLanguageError) -> InvalidRequestCause:
        return InvalidRequestCause(
            __root__=_InvalidRequestCause.UnexpectedLanguage(**dict(value), type="unexpectedLanguage")
        )


class InvalidRequestCause(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get(
        self,
    ) -> typing.Union[
        _InvalidRequestCause.SubmissionIdNotFound,
        _InvalidRequestCause.CustomTestCasesUnsupported,
        _InvalidRequestCause.UnexpectedLanguage,
    ]:
        return self.__root__

    def visit(
        self,
        submission_id_not_found: typing.Callable[[SubmissionIdNotFound], T_Result],
        custom_test_cases_unsupported: typing.Callable[[CustomTestCasesUnsupported], T_Result],
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

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)


class _InvalidRequestCause:
    class SubmissionIdNotFound(SubmissionIdNotFound):
        type: typing_extensions.Literal["submissionIdNotFound"]

    class CustomTestCasesUnsupported(CustomTestCasesUnsupported):
        type: typing_extensions.Literal["customTestCasesUnsupported"]

    class UnexpectedLanguage(UnexpectedLanguageError):
        type: typing_extensions.Literal["unexpectedLanguage"]


InvalidRequestCause.update_forward_refs()
