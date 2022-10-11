import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId
from .workspace_run_details import WorkspaceRunDetails


class WorkspaceRanResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    run_details: WorkspaceRunDetails = pydantic.Field(alias="runDetails")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, submission_id: SubmissionId) -> SubmissionId:
        for validator in WorkspaceRanResponse.Validators._submission_id_validators:
            submission_id = validator(submission_id)
        return submission_id

    @pydantic.validator("run_details")
    def _validate_run_details(cls, run_details: WorkspaceRunDetails) -> WorkspaceRunDetails:
        for validator in WorkspaceRanResponse.Validators._run_details_validators:
            run_details = validator(run_details)
        return run_details

    class Validators:
        _submission_id_validators: typing.ClassVar[typing.List[typing.Callable[[SubmissionId], SubmissionId]]] = []
        _run_details_validators: typing.ClassVar[
            typing.List[typing.Callable[[WorkspaceRunDetails], WorkspaceRunDetails]]
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
            cls, field_name: typing_extensions.Literal["run_details"]
        ) -> typing.Callable[
            [typing.Callable[[WorkspaceRunDetails], WorkspaceRunDetails]],
            typing.Callable[[WorkspaceRunDetails], WorkspaceRunDetails],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                elif field_name == "run_details":
                    cls._run_details_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on WorkspaceRanResponse: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
