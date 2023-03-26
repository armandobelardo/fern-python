# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .parameter_id import ParameterId

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def html(self, value: str) -> TestCaseImplementationDescriptionBoard:
        return TestCaseImplementationDescriptionBoard(
            __root__=_TestCaseImplementationDescriptionBoard.Html(value=value)
        )

    def param_id(self, value: ParameterId) -> TestCaseImplementationDescriptionBoard:
        return TestCaseImplementationDescriptionBoard(
            __root__=_TestCaseImplementationDescriptionBoard.ParamId(value=value)
        )


class TestCaseImplementationDescriptionBoard(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId]:
        return self.__root__

    def visit(
        self, html: typing.Callable[[str], T_Result], param_id: typing.Callable[[ParameterId], T_Result]
    ) -> T_Result:
        if self.__root__.type == "html":
            return html(self.__root__.value)
        if self.__root__.type == "paramId":
            return param_id(self.__root__.value)

    __root__: typing_extensions.Annotated[
        typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseImplementationDescriptionBoard.Validators.validate
            def validate(value: typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId]) -> typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _TestCaseImplementationDescriptionBoard.Html,
                            _TestCaseImplementationDescriptionBoard.ParamId,
                        ]
                    ],
                    typing.Union[
                        _TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId
                    ],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId
                    ]
                ],
                typing.Union[
                    _TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId],
            values.get("__root__"),
        )
        for validator in TestCaseImplementationDescriptionBoard.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _TestCaseImplementationDescriptionBoard:
    class Html(pydantic.BaseModel):
        type: typing_extensions.Literal["html"] = "html"
        value: str

        class Config:
            frozen = True

    class ParamId(pydantic.BaseModel):
        type: typing_extensions.Literal["paramId"] = "paramId"
        value: ParameterId

        class Config:
            frozen = True


TestCaseImplementationDescriptionBoard.update_forward_refs()
