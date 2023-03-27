# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .compile_error import CompileError
from .internal_error import InternalError
from .runtime_error import RuntimeError


class ErrorInfo_CompileError(CompileError):
    type: typing_extensions.Literal["compileError"]

    class Config:
        frozen = True


class ErrorInfo_RuntimeError(RuntimeError):
    type: typing_extensions.Literal["runtimeError"]

    class Config:
        frozen = True


class ErrorInfo_InternalError(InternalError):
    type: typing_extensions.Literal["internalError"]

    class Config:
        frozen = True


ErrorInfo = typing_extensions.Annotated[
    typing.Union[ErrorInfo_CompileError, ErrorInfo_RuntimeError, ErrorInfo_InternalError],
    pydantic.Field(discriminator="type"),
]
