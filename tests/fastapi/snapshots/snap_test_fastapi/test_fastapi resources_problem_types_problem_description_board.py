from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.variable_value import VariableValue

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def html(self, value: str) -> ProblemDescriptionBoard:
        return ProblemDescriptionBoard(__root__=_ProblemDescriptionBoard.Html(type="html", value=value))

    def variable(self, value: VariableValue) -> ProblemDescriptionBoard:
        return ProblemDescriptionBoard(__root__=_ProblemDescriptionBoard.Variable(type="variable", value=value))

    def test_case_id(self, value: str) -> ProblemDescriptionBoard:
        return ProblemDescriptionBoard(__root__=_ProblemDescriptionBoard.TestCaseId(type="testCaseId", value=value))


class ProblemDescriptionBoard(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _ProblemDescriptionBoard.Html, _ProblemDescriptionBoard.Variable, _ProblemDescriptionBoard.TestCaseId
    ]:
        return self.__root__

    def visit(
        self,
        html: typing.Callable[[str], T_Result],
        variable: typing.Callable[[VariableValue], T_Result],
        test_case_id: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self.__root__.type == "html":
            return html(self.__root__.html)
        if self.__root__.type == "variable":
            return variable(self.__root__.variable)
        if self.__root__.type == "testCaseId":
            return test_case_id(self.__root__.test_case_id)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _ProblemDescriptionBoard.Html, _ProblemDescriptionBoard.Variable, _ProblemDescriptionBoard.TestCaseId
        ],
        pydantic.Field(discriminator="type"),
    ]

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _ProblemDescriptionBoard.Html, _ProblemDescriptionBoard.Variable, _ProblemDescriptionBoard.TestCaseId
            ],
            values.get("__root__"),
        )
        for validator in ProblemDescriptionBoard.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _ProblemDescriptionBoard.Html,
                            _ProblemDescriptionBoard.Variable,
                            _ProblemDescriptionBoard.TestCaseId,
                        ]
                    ],
                    typing.Union[
                        _ProblemDescriptionBoard.Html,
                        _ProblemDescriptionBoard.Variable,
                        _ProblemDescriptionBoard.TestCaseId,
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
                        _ProblemDescriptionBoard.Html,
                        _ProblemDescriptionBoard.Variable,
                        _ProblemDescriptionBoard.TestCaseId,
                    ]
                ],
                typing.Union[
                    _ProblemDescriptionBoard.Html,
                    _ProblemDescriptionBoard.Variable,
                    _ProblemDescriptionBoard.TestCaseId,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True


class _ProblemDescriptionBoard:
    class Html(pydantic.BaseModel):
        type: typing_extensions.Literal["html"]
        value: str

        class Config:
            frozen = True

    class Variable(pydantic.BaseModel):
        type: typing_extensions.Literal["variable"]
        value: VariableValue

        class Config:
            frozen = True

    class TestCaseId(pydantic.BaseModel):
        type: typing_extensions.Literal["testCaseId"]
        value: str

        class Config:
            frozen = True


ProblemDescriptionBoard.update_forward_refs()