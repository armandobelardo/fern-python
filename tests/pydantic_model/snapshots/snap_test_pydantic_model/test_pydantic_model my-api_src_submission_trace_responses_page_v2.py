import typing

import pydantic

from .trace_response_v2 import TraceResponseV2


class TraceResponsesPageV2(pydantic.BaseModel):
    offset: typing.Optional[int]
    trace_responses: typing.List[TraceResponseV2] = pydantic.Field(alias="traceResponses")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True