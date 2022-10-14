# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.language import Language
from ..commons.test_case_with_expected_result import TestCaseWithExpectedResult
from ..commons.variable_type import VariableType
from .problem_description import ProblemDescription
from .problem_files import ProblemFiles
from .variable_type_and_name import VariableTypeAndName


class CreateProblemRequest(pydantic.BaseModel):
    problem_name: str = pydantic.Field(alias="problemName")
    problem_description: ProblemDescription = pydantic.Field(alias="problemDescription")
    files: typing.Dict[Language, ProblemFiles]
    input_params: typing.List[VariableTypeAndName] = pydantic.Field(alias="inputParams")
    output_type: VariableType = pydantic.Field(alias="outputType")
    testcases: typing.List[TestCaseWithExpectedResult]
    method_name: str = pydantic.Field(alias="methodName")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CreateProblemRequest.Validators.root
            def validate(values: CreateProblemRequest.Partial) -> CreateProblemRequest.Partial:
                ...

            @CreateProblemRequest.Validators.field("problem_name")
            def validate_problem_name(v: str, values: CreateProblemRequest.Partial) -> str:
                ...

            @CreateProblemRequest.Validators.field("problem_description")
            def validate_problem_description(v: ProblemDescription, values: CreateProblemRequest.Partial) -> ProblemDescription:
                ...

            @CreateProblemRequest.Validators.field("files")
            def validate_files(v: typing.Dict[Language, ProblemFiles], values: CreateProblemRequest.Partial) -> typing.Dict[Language, ProblemFiles]:
                ...

            @CreateProblemRequest.Validators.field("input_params")
            def validate_input_params(v: typing.List[VariableTypeAndName], values: CreateProblemRequest.Partial) -> typing.List[VariableTypeAndName]:
                ...

            @CreateProblemRequest.Validators.field("output_type")
            def validate_output_type(v: VariableType, values: CreateProblemRequest.Partial) -> VariableType:
                ...

            @CreateProblemRequest.Validators.field("testcases")
            def validate_testcases(v: typing.List[TestCaseWithExpectedResult], values: CreateProblemRequest.Partial) -> typing.List[TestCaseWithExpectedResult]:
                ...

            @CreateProblemRequest.Validators.field("method_name")
            def validate_method_name(v: str, values: CreateProblemRequest.Partial) -> str:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[CreateProblemRequest.Partial], CreateProblemRequest.Partial]]
        ] = []
        _problem_name_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.ProblemNameValidator]
        ] = []
        _problem_description_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.ProblemDescriptionValidator]
        ] = []
        _files_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators.FilesValidator]] = []
        _input_params_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.InputParamsValidator]
        ] = []
        _output_type_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators.OutputTypeValidator]] = []
        _testcases_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators.TestcasesValidator]] = []
        _method_name_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators.MethodNameValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[CreateProblemRequest.Partial], CreateProblemRequest.Partial]
        ) -> typing.Callable[[CreateProblemRequest.Partial], CreateProblemRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.ProblemNameValidator], CreateProblemRequest.Validators.ProblemNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_description"]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.ProblemDescriptionValidator],
            CreateProblemRequest.Validators.ProblemDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files"]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.FilesValidator], CreateProblemRequest.Validators.FilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["input_params"]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.InputParamsValidator], CreateProblemRequest.Validators.InputParamsValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["output_type"]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.OutputTypeValidator], CreateProblemRequest.Validators.OutputTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.TestcasesValidator], CreateProblemRequest.Validators.TestcasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.MethodNameValidator], CreateProblemRequest.Validators.MethodNameValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_name":
                    cls._problem_name_validators.append(validator)
                if field_name == "problem_description":
                    cls._problem_description_validators.append(validator)
                if field_name == "files":
                    cls._files_validators.append(validator)
                if field_name == "input_params":
                    cls._input_params_validators.append(validator)
                if field_name == "output_type":
                    cls._output_type_validators.append(validator)
                if field_name == "testcases":
                    cls._testcases_validators.append(validator)
                if field_name == "method_name":
                    cls._method_name_validators.append(validator)
                return validator

            return decorator

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: CreateProblemRequest.Partial) -> str:
                ...

        class ProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, v: ProblemDescription, *, values: CreateProblemRequest.Partial) -> ProblemDescription:
                ...

        class FilesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, ProblemFiles], *, values: CreateProblemRequest.Partial
            ) -> typing.Dict[Language, ProblemFiles]:
                ...

        class InputParamsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[VariableTypeAndName], *, values: CreateProblemRequest.Partial
            ) -> typing.List[VariableTypeAndName]:
                ...

        class OutputTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: CreateProblemRequest.Partial) -> VariableType:
                ...

        class TestcasesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TestCaseWithExpectedResult], *, values: CreateProblemRequest.Partial
            ) -> typing.List[TestCaseWithExpectedResult]:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: CreateProblemRequest.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: CreateProblemRequest.Partial) -> CreateProblemRequest.Partial:
        for validator in CreateProblemRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_name")
    def _validate_problem_name(cls, v: str, values: CreateProblemRequest.Partial) -> str:
        for validator in CreateProblemRequest.Validators._problem_name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_description")
    def _validate_problem_description(
        cls, v: ProblemDescription, values: CreateProblemRequest.Partial
    ) -> ProblemDescription:
        for validator in CreateProblemRequest.Validators._problem_description_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("files")
    def _validate_files(
        cls, v: typing.Dict[Language, ProblemFiles], values: CreateProblemRequest.Partial
    ) -> typing.Dict[Language, ProblemFiles]:
        for validator in CreateProblemRequest.Validators._files_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("input_params")
    def _validate_input_params(
        cls, v: typing.List[VariableTypeAndName], values: CreateProblemRequest.Partial
    ) -> typing.List[VariableTypeAndName]:
        for validator in CreateProblemRequest.Validators._input_params_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("output_type")
    def _validate_output_type(cls, v: VariableType, values: CreateProblemRequest.Partial) -> VariableType:
        for validator in CreateProblemRequest.Validators._output_type_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("testcases")
    def _validate_testcases(
        cls, v: typing.List[TestCaseWithExpectedResult], values: CreateProblemRequest.Partial
    ) -> typing.List[TestCaseWithExpectedResult]:
        for validator in CreateProblemRequest.Validators._testcases_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("method_name")
    def _validate_method_name(cls, v: str, values: CreateProblemRequest.Partial) -> str:
        for validator in CreateProblemRequest.Validators._method_name_validators:
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
