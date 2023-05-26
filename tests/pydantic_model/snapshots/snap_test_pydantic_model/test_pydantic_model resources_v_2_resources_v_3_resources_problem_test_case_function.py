# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ......commons.list_type import ListType
from ......commons.map_type import MapType
from ......commons.variable_type import VariableType
from .test_case_with_actual_result_implementation import TestCaseWithActualResultImplementation
from .void_function_definition import VoidFunctionDefinition


class TestCaseFunction_WithActualResult(TestCaseWithActualResultImplementation):
    type: typing_extensions.Literal["withActualResult"]

    class Config:
        allow_population_by_field_name = True


class TestCaseFunction_Custom(VoidFunctionDefinition):
    type: typing_extensions.Literal["custom"]

    class Config:
        allow_population_by_field_name = True


TestCaseFunction = typing.Union[TestCaseFunction_WithActualResult, TestCaseFunction_Custom]
TestCaseFunction_WithActualResult.update_forward_refs(ListType=ListType, MapType=MapType, VariableType=VariableType)
TestCaseFunction_Custom.update_forward_refs(ListType=ListType, MapType=MapType, VariableType=VariableType)
