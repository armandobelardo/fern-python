from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .parameter_id import ParameterId

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def html(self, value: str) -> TestCaseImplementationDescriptionBoard:
        return TestCaseImplementationDescriptionBoard(
            __root__=_TestCaseImplementationDescriptionBoard.Html(type="html", value=value)
        )

    def param_id(self, value: ParameterId) -> TestCaseImplementationDescriptionBoard:
        return TestCaseImplementationDescriptionBoard(
            __root__=_TestCaseImplementationDescriptionBoard.ParamId(type="paramId", value=value)
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
            return html(self.__root__.html)
        if self.__root__.type == "paramId":
            return param_id(self.__root__.param_id)

    __root__: typing_extensions.Annotated[
        typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId],
        pydantic.Field(discriminator="type"),
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId],
            values.get("__root__"),
        )
        for validator in TestCaseImplementationDescriptionBoard.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
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

    class Config:
        frozen = True


class _TestCaseImplementationDescriptionBoard:
    class Html(pydantic.BaseModel):
        type: typing_extensions.Literal["html"]
        value: str

        class Config:
            frozen = True

    class ParamId(pydantic.BaseModel):
        type: typing_extensions.Literal["paramId"]
        value: ParameterId

        class Config:
            frozen = True


TestCaseImplementationDescriptionBoard.update_forward_refs()
