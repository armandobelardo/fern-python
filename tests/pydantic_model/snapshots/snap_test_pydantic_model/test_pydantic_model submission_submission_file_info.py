# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions


class SubmissionFileInfo(pydantic.BaseModel):
    directory: str
    filename: str
    contents: str

    class Partial(typing_extensions.TypedDict):
        directory: typing_extensions.NotRequired[str]
        filename: typing_extensions.NotRequired[str]
        contents: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionFileInfo.Validators.root()
            def validate(values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
                ...

            @SubmissionFileInfo.Validators.field("directory")
            def validate_directory(directory: str, values: SubmissionFileInfo.Partial) -> str:
                ...

            @SubmissionFileInfo.Validators.field("filename")
            def validate_filename(filename: str, values: SubmissionFileInfo.Partial) -> str:
                ...

            @SubmissionFileInfo.Validators.field("contents")
            def validate_contents(contents: str, values: SubmissionFileInfo.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators._RootValidator]] = []
        _directory_pre_validators: typing.ClassVar[
            typing.List[SubmissionFileInfo.Validators.PreDirectoryValidator]
        ] = []
        _directory_post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.DirectoryValidator]] = []
        _filename_pre_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.PreFilenameValidator]] = []
        _filename_post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.FilenameValidator]] = []
        _contents_pre_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.PreContentsValidator]] = []
        _contents_post_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.ContentsValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators._RootValidator], SubmissionFileInfo.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators._PreRootValidator], SubmissionFileInfo.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["directory"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.PreDirectoryValidator], SubmissionFileInfo.Validators.PreDirectoryValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.DirectoryValidator], SubmissionFileInfo.Validators.DirectoryValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.PreFilenameValidator], SubmissionFileInfo.Validators.PreFilenameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.FilenameValidator], SubmissionFileInfo.Validators.FilenameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.PreContentsValidator], SubmissionFileInfo.Validators.PreContentsValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.ContentsValidator], SubmissionFileInfo.Validators.ContentsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "directory":
                    if pre:
                        cls._directory_pre_validators.append(validator)
                    else:
                        cls._directory_post_validators.append(validator)
                if field_name == "filename":
                    if pre:
                        cls._filename_pre_validators.append(validator)
                    else:
                        cls._filename_post_validators.append(validator)
                if field_name == "contents":
                    if pre:
                        cls._contents_pre_validators.append(validator)
                    else:
                        cls._contents_post_validators.append(validator)
                return validator

            return decorator

        class PreDirectoryValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmissionFileInfo.Partial) -> typing.Any:
                ...

        class DirectoryValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: SubmissionFileInfo.Partial) -> str:
                ...

        class PreFilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmissionFileInfo.Partial) -> typing.Any:
                ...

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: SubmissionFileInfo.Partial) -> str:
                ...

        class PreContentsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmissionFileInfo.Partial) -> typing.Any:
                ...

        class ContentsValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: SubmissionFileInfo.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
        for validator in SubmissionFileInfo.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: SubmissionFileInfo.Partial) -> SubmissionFileInfo.Partial:
        for validator in SubmissionFileInfo.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("directory", pre=True)
    def _pre_validate_directory(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._directory_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("directory", pre=False)
    def _post_validate_directory(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._directory_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=True)
    def _pre_validate_filename(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._filename_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=False)
    def _post_validate_filename(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._filename_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=True)
    def _pre_validate_contents(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._contents_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=False)
    def _post_validate_contents(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._contents_post_validators:
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
        json_encoders = {dt.datetime: lambda v: v.isoformat()}
