# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .....commons.types.list_type import ListType
from .....commons.types.map_type import MapType
from .....commons.types.variable_type import VariableType
from .non_void_function_signature import NonVoidFunctionSignature
from .void_function_signature import VoidFunctionSignature
from .void_function_signature_that_takes_actual_result import VoidFunctionSignatureThatTakesActualResult


class FunctionSignature_Void(VoidFunctionSignature):
    type: typing_extensions.Literal["void"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class FunctionSignature_NonVoid(NonVoidFunctionSignature):
    type: typing_extensions.Literal["nonVoid"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class FunctionSignature_VoidThatTakesActualResult(VoidFunctionSignatureThatTakesActualResult):
    type: typing_extensions.Literal["voidThatTakesActualResult"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


FunctionSignature = typing.Union[
    FunctionSignature_Void, FunctionSignature_NonVoid, FunctionSignature_VoidThatTakesActualResult
]
FunctionSignature_Void.update_forward_refs(ListType=ListType, MapType=MapType, VariableType=VariableType)
FunctionSignature_NonVoid.update_forward_refs(ListType=ListType, MapType=MapType, VariableType=VariableType)
FunctionSignature_VoidThatTakesActualResult.update_forward_refs(
    ListType=ListType, MapType=MapType, VariableType=VariableType
)
