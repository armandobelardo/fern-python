import pydantic

from .submission_id import SubmissionId


class FinishedResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")

    class Config:
        allow_population_by_field_name = True
