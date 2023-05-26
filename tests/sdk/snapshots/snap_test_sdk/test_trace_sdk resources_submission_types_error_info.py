# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .compile_error import CompileError
from .internal_error import InternalError
from .runtime_error import RuntimeError


class ErrorInfo_CompileError(CompileError):
    type: typing_extensions.Literal["compileError"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class ErrorInfo_RuntimeError(RuntimeError):
    type: typing_extensions.Literal["runtimeError"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class ErrorInfo_InternalError(InternalError):
    type: typing_extensions.Literal["internalError"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


ErrorInfo = typing.Union[ErrorInfo_CompileError, ErrorInfo_RuntimeError, ErrorInfo_InternalError]
