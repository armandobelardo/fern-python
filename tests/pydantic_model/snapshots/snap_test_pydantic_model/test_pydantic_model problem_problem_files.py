# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.file_info import FileInfo


class ProblemFiles(pydantic.BaseModel):
    solution_file: FileInfo = pydantic.Field(alias="solutionFile")
    read_only_files: typing.List[FileInfo] = pydantic.Field(alias="readOnlyFiles")

    class Partial(typing_extensions.TypedDict):
        solution_file: typing_extensions.NotRequired[FileInfo]
        read_only_files: typing_extensions.NotRequired[typing.List[FileInfo]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ProblemFiles.Validators.root
            def validate(values: ProblemFiles.Partial) -> ProblemFiles.Partial:
                ...

            @ProblemFiles.Validators.field("solution_file")
            def validate_solution_file(v: FileInfo, values: ProblemFiles.Partial) -> FileInfo:
                ...

            @ProblemFiles.Validators.field("read_only_files")
            def validate_read_only_files(v: typing.List[FileInfo], values: ProblemFiles.Partial) -> typing.List[FileInfo]:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[ProblemFiles.Partial], ProblemFiles.Partial]]] = []
        _solution_file_validators: typing.ClassVar[typing.List[ProblemFiles.Validators.SolutionFileValidator]] = []
        _read_only_files_validators: typing.ClassVar[typing.List[ProblemFiles.Validators.ReadOnlyFilesValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[ProblemFiles.Partial], ProblemFiles.Partial]
        ) -> typing.Callable[[ProblemFiles.Partial], ProblemFiles.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["solution_file"]
        ) -> typing.Callable[
            [ProblemFiles.Validators.SolutionFileValidator], ProblemFiles.Validators.SolutionFileValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["read_only_files"]
        ) -> typing.Callable[
            [ProblemFiles.Validators.ReadOnlyFilesValidator], ProblemFiles.Validators.ReadOnlyFilesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "solution_file":
                    cls._solution_file_validators.append(validator)
                if field_name == "read_only_files":
                    cls._read_only_files_validators.append(validator)
                return validator

            return decorator

        class SolutionFileValidator(typing_extensions.Protocol):
            def __call__(self, v: FileInfo, *, values: ProblemFiles.Partial) -> FileInfo:
                ...

        class ReadOnlyFilesValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.List[FileInfo], *, values: ProblemFiles.Partial) -> typing.List[FileInfo]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: ProblemFiles.Partial) -> ProblemFiles.Partial:
        for validator in ProblemFiles.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("solution_file")
    def _validate_solution_file(cls, v: FileInfo, values: ProblemFiles.Partial) -> FileInfo:
        for validator in ProblemFiles.Validators._solution_file_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("read_only_files")
    def _validate_read_only_files(cls, v: typing.List[FileInfo], values: ProblemFiles.Partial) -> typing.List[FileInfo]:
        for validator in ProblemFiles.Validators._read_only_files_validators:
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
