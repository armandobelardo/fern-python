import typing

import pydantic
import typing_extensions

from ..commons.language import Language
from .submission_file_info import SubmissionFileInfo
from .submission_id import SubmissionId


class WorkspaceSubmitRequest(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    language: Language
    submission_files: typing.List[SubmissionFileInfo] = pydantic.Field(alias="submissionFiles")
    user_id: typing.Optional[str] = pydantic.Field(alias="userId")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, submission_id: SubmissionId) -> SubmissionId:
        for validator in WorkspaceSubmitRequest.Validators._submission_id_validators:
            submission_id = validator(submission_id)
        return submission_id

    @pydantic.validator("language")
    def _validate_language(cls, language: Language) -> Language:
        for validator in WorkspaceSubmitRequest.Validators._language_validators:
            language = validator(language)
        return language

    @pydantic.validator("submission_files")
    def _validate_submission_files(
        cls, submission_files: typing.List[SubmissionFileInfo]
    ) -> typing.List[SubmissionFileInfo]:
        for validator in WorkspaceSubmitRequest.Validators._submission_files_validators:
            submission_files = validator(submission_files)
        return submission_files

    @pydantic.validator("user_id")
    def _validate_user_id(cls, user_id: typing.Optional[str]) -> typing.Optional[str]:
        for validator in WorkspaceSubmitRequest.Validators._user_id_validators:
            user_id = validator(user_id)
        return user_id

    class Validators:
        _submission_id_validators: typing.ClassVar[typing.List[typing.Callable[[SubmissionId], SubmissionId]]] = []
        _language_validators: typing.ClassVar[typing.List[typing.Callable[[Language], Language]]] = []
        _submission_files_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[SubmissionFileInfo]], typing.List[SubmissionFileInfo]]]
        ] = []
        _user_id_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.Optional[str]], typing.Optional[str]]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [typing.Callable[[SubmissionId], SubmissionId]], typing.Callable[[SubmissionId], SubmissionId]
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"]
        ) -> typing.Callable[[typing.Callable[[Language], Language]], typing.Callable[[Language], Language]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_files"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[SubmissionFileInfo]], typing.List[SubmissionFileInfo]]],
            typing.Callable[[typing.List[SubmissionFileInfo]], typing.List[SubmissionFileInfo]],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["user_id"]
        ) -> typing.Callable[
            [typing.Callable[[typing.Optional[str]], typing.Optional[str]]],
            typing.Callable[[typing.Optional[str]], typing.Optional[str]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                elif field_name == "language":
                    cls._language_validators.append(validator)
                elif field_name == "submission_files":
                    cls._submission_files_validators.append(validator)
                elif field_name == "user_id":
                    cls._user_id_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on WorkspaceSubmitRequest: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
