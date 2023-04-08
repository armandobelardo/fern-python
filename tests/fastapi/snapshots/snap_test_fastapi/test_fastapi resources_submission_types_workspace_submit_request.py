# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...commons.types.language import Language
from .submission_file_info import SubmissionFileInfo
from .submission_id import SubmissionId


class WorkspaceSubmitRequest(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    language: Language
    submission_files: typing.List[SubmissionFileInfo] = pydantic.Field(alias="submissionFiles")
    user_id: typing.Optional[str] = pydantic.Field(alias="userId")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        language: typing_extensions.NotRequired[Language]
        submission_files: typing_extensions.NotRequired[typing.List[SubmissionFileInfo]]
        user_id: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceSubmitRequest.Validators.root()
            def validate(values: WorkspaceSubmitRequest.Partial) -> WorkspaceSubmitRequest.Partial:
                ...

            @WorkspaceSubmitRequest.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: WorkspaceSubmitRequest.Partial) -> SubmissionId:
                ...

            @WorkspaceSubmitRequest.Validators.field("language")
            def validate_language(language: Language, values: WorkspaceSubmitRequest.Partial) -> Language:
                ...

            @WorkspaceSubmitRequest.Validators.field("submission_files")
            def validate_submission_files(submission_files: typing.List[SubmissionFileInfo], values: WorkspaceSubmitRequest.Partial) -> typing.List[SubmissionFileInfo]:
                ...

            @WorkspaceSubmitRequest.Validators.field("user_id")
            def validate_user_id(user_id: typing.Optional[str], values: WorkspaceSubmitRequest.Partial) -> typing.Optional[str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[WorkspaceSubmitRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[WorkspaceSubmitRequest.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.SubmissionIdValidator]
        ] = []
        _language_pre_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.PreLanguageValidator]
        ] = []
        _language_post_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.LanguageValidator]
        ] = []
        _submission_files_pre_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.PreSubmissionFilesValidator]
        ] = []
        _submission_files_post_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.SubmissionFilesValidator]
        ] = []
        _user_id_pre_validators: typing.ClassVar[typing.List[WorkspaceSubmitRequest.Validators.PreUserIdValidator]] = []
        _user_id_post_validators: typing.ClassVar[typing.List[WorkspaceSubmitRequest.Validators.UserIdValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators._RootValidator], WorkspaceSubmitRequest.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators._PreRootValidator], WorkspaceSubmitRequest.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.PreSubmissionIdValidator],
            WorkspaceSubmitRequest.Validators.PreSubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.SubmissionIdValidator],
            WorkspaceSubmitRequest.Validators.SubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.PreLanguageValidator],
            WorkspaceSubmitRequest.Validators.PreLanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.LanguageValidator], WorkspaceSubmitRequest.Validators.LanguageValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.PreSubmissionFilesValidator],
            WorkspaceSubmitRequest.Validators.PreSubmissionFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_files"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.SubmissionFilesValidator],
            WorkspaceSubmitRequest.Validators.SubmissionFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["user_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.PreUserIdValidator], WorkspaceSubmitRequest.Validators.PreUserIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["user_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.UserIdValidator], WorkspaceSubmitRequest.Validators.UserIdValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "language":
                    if pre:
                        cls._language_pre_validators.append(validator)
                    else:
                        cls._language_post_validators.append(validator)
                if field_name == "submission_files":
                    if pre:
                        cls._submission_files_pre_validators.append(validator)
                    else:
                        cls._submission_files_post_validators.append(validator)
                if field_name == "user_id":
                    if pre:
                        cls._user_id_pre_validators.append(validator)
                    else:
                        cls._user_id_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: WorkspaceSubmitRequest.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: WorkspaceSubmitRequest.Partial) -> SubmissionId:
                ...

        class PreLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: WorkspaceSubmitRequest.Partial) -> typing.Any:
                ...

        class LanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: WorkspaceSubmitRequest.Partial) -> Language:
                ...

        class PreSubmissionFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: WorkspaceSubmitRequest.Partial) -> typing.Any:
                ...

        class SubmissionFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[SubmissionFileInfo], __values: WorkspaceSubmitRequest.Partial
            ) -> typing.List[SubmissionFileInfo]:
                ...

        class PreUserIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: WorkspaceSubmitRequest.Partial) -> typing.Any:
                ...

        class UserIdValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[str], __values: WorkspaceSubmitRequest.Partial
            ) -> typing.Optional[str]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: WorkspaceSubmitRequest.Partial) -> WorkspaceSubmitRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: WorkspaceSubmitRequest.Partial) -> WorkspaceSubmitRequest.Partial:
        for validator in WorkspaceSubmitRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: WorkspaceSubmitRequest.Partial) -> WorkspaceSubmitRequest.Partial:
        for validator in WorkspaceSubmitRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: WorkspaceSubmitRequest.Partial) -> SubmissionId:
        for validator in WorkspaceSubmitRequest.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: WorkspaceSubmitRequest.Partial) -> SubmissionId:
        for validator in WorkspaceSubmitRequest.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("language", pre=True)
    def _pre_validate_language(cls, v: Language, values: WorkspaceSubmitRequest.Partial) -> Language:
        for validator in WorkspaceSubmitRequest.Validators._language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("language", pre=False)
    def _post_validate_language(cls, v: Language, values: WorkspaceSubmitRequest.Partial) -> Language:
        for validator in WorkspaceSubmitRequest.Validators._language_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_files", pre=True)
    def _pre_validate_submission_files(
        cls, v: typing.List[SubmissionFileInfo], values: WorkspaceSubmitRequest.Partial
    ) -> typing.List[SubmissionFileInfo]:
        for validator in WorkspaceSubmitRequest.Validators._submission_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_files", pre=False)
    def _post_validate_submission_files(
        cls, v: typing.List[SubmissionFileInfo], values: WorkspaceSubmitRequest.Partial
    ) -> typing.List[SubmissionFileInfo]:
        for validator in WorkspaceSubmitRequest.Validators._submission_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("user_id", pre=True)
    def _pre_validate_user_id(
        cls, v: typing.Optional[str], values: WorkspaceSubmitRequest.Partial
    ) -> typing.Optional[str]:
        for validator in WorkspaceSubmitRequest.Validators._user_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("user_id", pre=False)
    def _post_validate_user_id(
        cls, v: typing.Optional[str], values: WorkspaceSubmitRequest.Partial
    ) -> typing.Optional[str]:
        for validator in WorkspaceSubmitRequest.Validators._user_id_post_validators:
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
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
