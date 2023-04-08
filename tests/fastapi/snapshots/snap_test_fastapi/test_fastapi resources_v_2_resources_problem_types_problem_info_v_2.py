# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .....commons.types.language import Language
from .....commons.types.problem_id import ProblemId
from .....problem.types.problem_description import ProblemDescription
from .custom_files import CustomFiles
from .generated_files import GeneratedFiles
from .test_case_template import TestCaseTemplate
from .test_case_v_2 import TestCaseV2


class ProblemInfoV2(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_description: ProblemDescription = pydantic.Field(alias="problemDescription")
    problem_name: str = pydantic.Field(alias="problemName")
    problem_version: int = pydantic.Field(alias="problemVersion")
    supported_languages: typing.List[Language] = pydantic.Field(alias="supportedLanguages")
    custom_files: CustomFiles = pydantic.Field(alias="customFiles")
    generated_files: GeneratedFiles = pydantic.Field(alias="generatedFiles")
    custom_test_case_templates: typing.List[TestCaseTemplate] = pydantic.Field(alias="customTestCaseTemplates")
    testcases: typing.List[TestCaseV2]
    is_public: bool = pydantic.Field(alias="isPublic")

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_description: typing_extensions.NotRequired[ProblemDescription]
        problem_name: typing_extensions.NotRequired[str]
        problem_version: typing_extensions.NotRequired[int]
        supported_languages: typing_extensions.NotRequired[typing.List[Language]]
        custom_files: typing_extensions.NotRequired[CustomFiles]
        generated_files: typing_extensions.NotRequired[GeneratedFiles]
        custom_test_case_templates: typing_extensions.NotRequired[typing.List[TestCaseTemplate]]
        testcases: typing_extensions.NotRequired[typing.List[TestCaseV2]]
        is_public: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ProblemInfoV2.Validators.root()
            def validate(values: ProblemInfoV2.Partial) -> ProblemInfoV2.Partial:
                ...

            @ProblemInfoV2.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: ProblemInfoV2.Partial) -> ProblemId:
                ...

            @ProblemInfoV2.Validators.field("problem_description")
            def validate_problem_description(problem_description: ProblemDescription, values: ProblemInfoV2.Partial) -> ProblemDescription:
                ...

            @ProblemInfoV2.Validators.field("problem_name")
            def validate_problem_name(problem_name: str, values: ProblemInfoV2.Partial) -> str:
                ...

            @ProblemInfoV2.Validators.field("problem_version")
            def validate_problem_version(problem_version: int, values: ProblemInfoV2.Partial) -> int:
                ...

            @ProblemInfoV2.Validators.field("supported_languages")
            def validate_supported_languages(supported_languages: typing.List[Language], values: ProblemInfoV2.Partial) -> typing.List[Language]:
                ...

            @ProblemInfoV2.Validators.field("custom_files")
            def validate_custom_files(custom_files: CustomFiles, values: ProblemInfoV2.Partial) -> CustomFiles:
                ...

            @ProblemInfoV2.Validators.field("generated_files")
            def validate_generated_files(generated_files: GeneratedFiles, values: ProblemInfoV2.Partial) -> GeneratedFiles:
                ...

            @ProblemInfoV2.Validators.field("custom_test_case_templates")
            def validate_custom_test_case_templates(custom_test_case_templates: typing.List[TestCaseTemplate], values: ProblemInfoV2.Partial) -> typing.List[TestCaseTemplate]:
                ...

            @ProblemInfoV2.Validators.field("testcases")
            def validate_testcases(testcases: typing.List[TestCaseV2], values: ProblemInfoV2.Partial) -> typing.List[TestCaseV2]:
                ...

            @ProblemInfoV2.Validators.field("is_public")
            def validate_is_public(is_public: bool, values: ProblemInfoV2.Partial) -> bool:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators._RootValidator]] = []
        _problem_id_pre_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.PreProblemIdValidator]] = []
        _problem_id_post_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.ProblemIdValidator]] = []
        _problem_description_pre_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.PreProblemDescriptionValidator]
        ] = []
        _problem_description_post_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.ProblemDescriptionValidator]
        ] = []
        _problem_name_pre_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.PreProblemNameValidator]
        ] = []
        _problem_name_post_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.ProblemNameValidator]] = []
        _problem_version_pre_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.PreProblemVersionValidator]
        ] = []
        _problem_version_post_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.ProblemVersionValidator]
        ] = []
        _supported_languages_pre_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.PreSupportedLanguagesValidator]
        ] = []
        _supported_languages_post_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.SupportedLanguagesValidator]
        ] = []
        _custom_files_pre_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.PreCustomFilesValidator]
        ] = []
        _custom_files_post_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.CustomFilesValidator]] = []
        _generated_files_pre_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.PreGeneratedFilesValidator]
        ] = []
        _generated_files_post_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.GeneratedFilesValidator]
        ] = []
        _custom_test_case_templates_pre_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.PreCustomTestCaseTemplatesValidator]
        ] = []
        _custom_test_case_templates_post_validators: typing.ClassVar[
            typing.List[ProblemInfoV2.Validators.CustomTestCaseTemplatesValidator]
        ] = []
        _testcases_pre_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.PreTestcasesValidator]] = []
        _testcases_post_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.TestcasesValidator]] = []
        _is_public_pre_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.PreIsPublicValidator]] = []
        _is_public_post_validators: typing.ClassVar[typing.List[ProblemInfoV2.Validators.IsPublicValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ProblemInfoV2.Validators._RootValidator], ProblemInfoV2.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ProblemInfoV2.Validators._PreRootValidator], ProblemInfoV2.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreProblemIdValidator], ProblemInfoV2.Validators.PreProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemIdValidator], ProblemInfoV2.Validators.ProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_description"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreProblemDescriptionValidator],
            ProblemInfoV2.Validators.PreProblemDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["problem_description"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemDescriptionValidator], ProblemInfoV2.Validators.ProblemDescriptionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreProblemNameValidator], ProblemInfoV2.Validators.PreProblemNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemNameValidator], ProblemInfoV2.Validators.ProblemNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreProblemVersionValidator], ProblemInfoV2.Validators.PreProblemVersionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["problem_version"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.ProblemVersionValidator], ProblemInfoV2.Validators.ProblemVersionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["supported_languages"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreSupportedLanguagesValidator],
            ProblemInfoV2.Validators.PreSupportedLanguagesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["supported_languages"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.SupportedLanguagesValidator], ProblemInfoV2.Validators.SupportedLanguagesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreCustomFilesValidator], ProblemInfoV2.Validators.PreCustomFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_files"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.CustomFilesValidator], ProblemInfoV2.Validators.CustomFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["generated_files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreGeneratedFilesValidator], ProblemInfoV2.Validators.PreGeneratedFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["generated_files"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.GeneratedFilesValidator], ProblemInfoV2.Validators.GeneratedFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["custom_test_case_templates"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreCustomTestCaseTemplatesValidator],
            ProblemInfoV2.Validators.PreCustomTestCaseTemplatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["custom_test_case_templates"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.CustomTestCaseTemplatesValidator],
            ProblemInfoV2.Validators.CustomTestCaseTemplatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreTestcasesValidator], ProblemInfoV2.Validators.PreTestcasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.TestcasesValidator], ProblemInfoV2.Validators.TestcasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_public"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemInfoV2.Validators.PreIsPublicValidator], ProblemInfoV2.Validators.PreIsPublicValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_public"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ProblemInfoV2.Validators.IsPublicValidator], ProblemInfoV2.Validators.IsPublicValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    if pre:
                        cls._problem_id_pre_validators.append(validator)
                    else:
                        cls._problem_id_post_validators.append(validator)
                if field_name == "problem_description":
                    if pre:
                        cls._problem_description_pre_validators.append(validator)
                    else:
                        cls._problem_description_post_validators.append(validator)
                if field_name == "problem_name":
                    if pre:
                        cls._problem_name_pre_validators.append(validator)
                    else:
                        cls._problem_name_post_validators.append(validator)
                if field_name == "problem_version":
                    if pre:
                        cls._problem_version_pre_validators.append(validator)
                    else:
                        cls._problem_version_post_validators.append(validator)
                if field_name == "supported_languages":
                    if pre:
                        cls._supported_languages_pre_validators.append(validator)
                    else:
                        cls._supported_languages_post_validators.append(validator)
                if field_name == "custom_files":
                    if pre:
                        cls._custom_files_pre_validators.append(validator)
                    else:
                        cls._custom_files_post_validators.append(validator)
                if field_name == "generated_files":
                    if pre:
                        cls._generated_files_pre_validators.append(validator)
                    else:
                        cls._generated_files_post_validators.append(validator)
                if field_name == "custom_test_case_templates":
                    if pre:
                        cls._custom_test_case_templates_pre_validators.append(validator)
                    else:
                        cls._custom_test_case_templates_post_validators.append(validator)
                if field_name == "testcases":
                    if pre:
                        cls._testcases_pre_validators.append(validator)
                    else:
                        cls._testcases_post_validators.append(validator)
                if field_name == "is_public":
                    if pre:
                        cls._is_public_pre_validators.append(validator)
                    else:
                        cls._is_public_post_validators.append(validator)
                return validator

            return decorator

        class PreProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: ProblemInfoV2.Partial) -> ProblemId:
                ...

        class PreProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class ProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemDescription, __values: ProblemInfoV2.Partial) -> ProblemDescription:
                ...

        class PreProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: ProblemInfoV2.Partial) -> str:
                ...

        class PreProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: ProblemInfoV2.Partial) -> int:
                ...

        class PreSupportedLanguagesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class SupportedLanguagesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.List[Language], __values: ProblemInfoV2.Partial) -> typing.List[Language]:
                ...

        class PreCustomFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class CustomFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: CustomFiles, __values: ProblemInfoV2.Partial) -> CustomFiles:
                ...

        class PreGeneratedFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class GeneratedFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: GeneratedFiles, __values: ProblemInfoV2.Partial) -> GeneratedFiles:
                ...

        class PreCustomTestCaseTemplatesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class CustomTestCaseTemplatesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCaseTemplate], __values: ProblemInfoV2.Partial
            ) -> typing.List[TestCaseTemplate]:
                ...

        class PreTestcasesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class TestcasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCaseV2], __values: ProblemInfoV2.Partial
            ) -> typing.List[TestCaseV2]:
                ...

        class PreIsPublicValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemInfoV2.Partial) -> typing.Any:
                ...

        class IsPublicValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: ProblemInfoV2.Partial) -> bool:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ProblemInfoV2.Partial) -> ProblemInfoV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: ProblemInfoV2.Partial) -> ProblemInfoV2.Partial:
        for validator in ProblemInfoV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: ProblemInfoV2.Partial) -> ProblemInfoV2.Partial:
        for validator in ProblemInfoV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_id", pre=True)
    def _pre_validate_problem_id(cls, v: ProblemId, values: ProblemInfoV2.Partial) -> ProblemId:
        for validator in ProblemInfoV2.Validators._problem_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=False)
    def _post_validate_problem_id(cls, v: ProblemId, values: ProblemInfoV2.Partial) -> ProblemId:
        for validator in ProblemInfoV2.Validators._problem_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_description", pre=True)
    def _pre_validate_problem_description(
        cls, v: ProblemDescription, values: ProblemInfoV2.Partial
    ) -> ProblemDescription:
        for validator in ProblemInfoV2.Validators._problem_description_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_description", pre=False)
    def _post_validate_problem_description(
        cls, v: ProblemDescription, values: ProblemInfoV2.Partial
    ) -> ProblemDescription:
        for validator in ProblemInfoV2.Validators._problem_description_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_name", pre=True)
    def _pre_validate_problem_name(cls, v: str, values: ProblemInfoV2.Partial) -> str:
        for validator in ProblemInfoV2.Validators._problem_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_name", pre=False)
    def _post_validate_problem_name(cls, v: str, values: ProblemInfoV2.Partial) -> str:
        for validator in ProblemInfoV2.Validators._problem_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=True)
    def _pre_validate_problem_version(cls, v: int, values: ProblemInfoV2.Partial) -> int:
        for validator in ProblemInfoV2.Validators._problem_version_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=False)
    def _post_validate_problem_version(cls, v: int, values: ProblemInfoV2.Partial) -> int:
        for validator in ProblemInfoV2.Validators._problem_version_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("supported_languages", pre=True)
    def _pre_validate_supported_languages(
        cls, v: typing.List[Language], values: ProblemInfoV2.Partial
    ) -> typing.List[Language]:
        for validator in ProblemInfoV2.Validators._supported_languages_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("supported_languages", pre=False)
    def _post_validate_supported_languages(
        cls, v: typing.List[Language], values: ProblemInfoV2.Partial
    ) -> typing.List[Language]:
        for validator in ProblemInfoV2.Validators._supported_languages_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_files", pre=True)
    def _pre_validate_custom_files(cls, v: CustomFiles, values: ProblemInfoV2.Partial) -> CustomFiles:
        for validator in ProblemInfoV2.Validators._custom_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_files", pre=False)
    def _post_validate_custom_files(cls, v: CustomFiles, values: ProblemInfoV2.Partial) -> CustomFiles:
        for validator in ProblemInfoV2.Validators._custom_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("generated_files", pre=True)
    def _pre_validate_generated_files(cls, v: GeneratedFiles, values: ProblemInfoV2.Partial) -> GeneratedFiles:
        for validator in ProblemInfoV2.Validators._generated_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("generated_files", pre=False)
    def _post_validate_generated_files(cls, v: GeneratedFiles, values: ProblemInfoV2.Partial) -> GeneratedFiles:
        for validator in ProblemInfoV2.Validators._generated_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_test_case_templates", pre=True)
    def _pre_validate_custom_test_case_templates(
        cls, v: typing.List[TestCaseTemplate], values: ProblemInfoV2.Partial
    ) -> typing.List[TestCaseTemplate]:
        for validator in ProblemInfoV2.Validators._custom_test_case_templates_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_test_case_templates", pre=False)
    def _post_validate_custom_test_case_templates(
        cls, v: typing.List[TestCaseTemplate], values: ProblemInfoV2.Partial
    ) -> typing.List[TestCaseTemplate]:
        for validator in ProblemInfoV2.Validators._custom_test_case_templates_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("testcases", pre=True)
    def _pre_validate_testcases(
        cls, v: typing.List[TestCaseV2], values: ProblemInfoV2.Partial
    ) -> typing.List[TestCaseV2]:
        for validator in ProblemInfoV2.Validators._testcases_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("testcases", pre=False)
    def _post_validate_testcases(
        cls, v: typing.List[TestCaseV2], values: ProblemInfoV2.Partial
    ) -> typing.List[TestCaseV2]:
        for validator in ProblemInfoV2.Validators._testcases_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_public", pre=True)
    def _pre_validate_is_public(cls, v: bool, values: ProblemInfoV2.Partial) -> bool:
        for validator in ProblemInfoV2.Validators._is_public_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_public", pre=False)
    def _post_validate_is_public(cls, v: bool, values: ProblemInfoV2.Partial) -> bool:
        for validator in ProblemInfoV2.Validators._is_public_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
