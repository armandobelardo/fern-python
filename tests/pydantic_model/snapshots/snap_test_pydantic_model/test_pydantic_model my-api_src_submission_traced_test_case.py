import typing

import pydantic

from .test_case_result_with_stdout import TestCaseResultWithStdout


class TracedTestCase(pydantic.BaseModel):
    result: TestCaseResultWithStdout
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
