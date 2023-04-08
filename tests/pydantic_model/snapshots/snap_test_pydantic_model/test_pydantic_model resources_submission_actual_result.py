# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.variable_value import VariableValue
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2


class ActualResult_Value(pydantic.BaseModel):
    type: typing_extensions.Literal["value"]
    value: VariableValue

    class Config:
        frozen = True
        orm_mode = True


class ActualResult_Exception(ExceptionInfo):
    type: typing_extensions.Literal["exception"]

    class Config:
        frozen = True
        orm_mode = True


class ActualResult_ExceptionV2(pydantic.BaseModel):
    type: typing_extensions.Literal["exceptionV2"]
    value: ExceptionV2

    class Config:
        frozen = True
        orm_mode = True


ActualResult = typing_extensions.Annotated[
    typing.Union[ActualResult_Value, ActualResult_Exception, ActualResult_ExceptionV2],
    pydantic.Field(discriminator="type"),
]
