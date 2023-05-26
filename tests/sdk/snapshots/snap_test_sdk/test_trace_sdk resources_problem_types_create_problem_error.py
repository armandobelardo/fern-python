# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .generic_create_problem_error import GenericCreateProblemError


class CreateProblemError_Generic(GenericCreateProblemError):
    error_type: typing_extensions.Literal["generic"] = pydantic.Field(alias="_type")

    class Config:
        frozen = True
        allow_population_by_field_name = True


CreateProblemError = typing.Union[CreateProblemError_Generic]
