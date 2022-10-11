from __future__ import annotations

import typing

import pydantic
import typing_extensions

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def integer_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.IntegerType(type="integerType"))

    def double_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.DoubleType(type="doubleType"))

    def boolean_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.BooleanType(type="booleanType"))

    def string_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.StringType(type="stringType"))

    def char_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.CharType(type="charType"))

    def list_type(self, value: ListType) -> VariableType:
        return VariableType(__root__=_VariableType.ListType(**dict(value), type="listType"))

    def map_type(self, value: MapType) -> VariableType:
        return VariableType(__root__=_VariableType.MapType(**dict(value), type="mapType"))

    def binary_tree_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.BinaryTreeType(type="binaryTreeType"))

    def singly_linked_list_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.SinglyLinkedListType(type="singlyLinkedListType"))

    def doubly_linked_list_type(self) -> VariableType:
        return VariableType(__root__=_VariableType.DoublyLinkedListType(type="doublyLinkedListType"))


class VariableType(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _VariableType.IntegerType,
        _VariableType.DoubleType,
        _VariableType.BooleanType,
        _VariableType.StringType,
        _VariableType.CharType,
        _VariableType.ListType,
        _VariableType.MapType,
        _VariableType.BinaryTreeType,
        _VariableType.SinglyLinkedListType,
        _VariableType.DoublyLinkedListType,
    ]:
        return self.__root__

    def visit(
        self,
        integer_type: typing.Callable[[], T_Result],
        double_type: typing.Callable[[], T_Result],
        boolean_type: typing.Callable[[], T_Result],
        string_type: typing.Callable[[], T_Result],
        char_type: typing.Callable[[], T_Result],
        list_type: typing.Callable[[ListType], T_Result],
        map_type: typing.Callable[[MapType], T_Result],
        binary_tree_type: typing.Callable[[], T_Result],
        singly_linked_list_type: typing.Callable[[], T_Result],
        doubly_linked_list_type: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.__root__.type == "integerType":
            return integer_type()
        if self.__root__.type == "doubleType":
            return double_type()
        if self.__root__.type == "booleanType":
            return boolean_type()
        if self.__root__.type == "stringType":
            return string_type()
        if self.__root__.type == "charType":
            return char_type()
        if self.__root__.type == "listType":
            return list_type(self.__root__)
        if self.__root__.type == "mapType":
            return map_type(self.__root__)
        if self.__root__.type == "binaryTreeType":
            return binary_tree_type()
        if self.__root__.type == "singlyLinkedListType":
            return singly_linked_list_type()
        if self.__root__.type == "doublyLinkedListType":
            return doubly_linked_list_type()

    __root__: typing_extensions.Annotated[
        typing.Union[
            _VariableType.IntegerType,
            _VariableType.DoubleType,
            _VariableType.BooleanType,
            _VariableType.StringType,
            _VariableType.CharType,
            _VariableType.ListType,
            _VariableType.MapType,
            _VariableType.BinaryTreeType,
            _VariableType.SinglyLinkedListType,
            _VariableType.DoublyLinkedListType,
        ],
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
            typing.Union[
                _VariableType.IntegerType,
                _VariableType.DoubleType,
                _VariableType.BooleanType,
                _VariableType.StringType,
                _VariableType.CharType,
                _VariableType.ListType,
                _VariableType.MapType,
                _VariableType.BinaryTreeType,
                _VariableType.SinglyLinkedListType,
                _VariableType.DoublyLinkedListType,
            ],
            values.get("__root__"),
        )
        for validator in VariableType.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _VariableType.IntegerType,
                            _VariableType.DoubleType,
                            _VariableType.BooleanType,
                            _VariableType.StringType,
                            _VariableType.CharType,
                            _VariableType.ListType,
                            _VariableType.MapType,
                            _VariableType.BinaryTreeType,
                            _VariableType.SinglyLinkedListType,
                            _VariableType.DoublyLinkedListType,
                        ]
                    ],
                    typing.Union[
                        _VariableType.IntegerType,
                        _VariableType.DoubleType,
                        _VariableType.BooleanType,
                        _VariableType.StringType,
                        _VariableType.CharType,
                        _VariableType.ListType,
                        _VariableType.MapType,
                        _VariableType.BinaryTreeType,
                        _VariableType.SinglyLinkedListType,
                        _VariableType.DoublyLinkedListType,
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
                        _VariableType.IntegerType,
                        _VariableType.DoubleType,
                        _VariableType.BooleanType,
                        _VariableType.StringType,
                        _VariableType.CharType,
                        _VariableType.ListType,
                        _VariableType.MapType,
                        _VariableType.BinaryTreeType,
                        _VariableType.SinglyLinkedListType,
                        _VariableType.DoublyLinkedListType,
                    ]
                ],
                typing.Union[
                    _VariableType.IntegerType,
                    _VariableType.DoubleType,
                    _VariableType.BooleanType,
                    _VariableType.StringType,
                    _VariableType.CharType,
                    _VariableType.ListType,
                    _VariableType.MapType,
                    _VariableType.BinaryTreeType,
                    _VariableType.SinglyLinkedListType,
                    _VariableType.DoublyLinkedListType,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    class Config:
        frozen = True


from .list_type import ListType  # noqa: E402
from .map_type import MapType  # noqa: E402


class _VariableType:
    class IntegerType(pydantic.BaseModel):
        type: typing_extensions.Literal["integerType"]

        class Config:
            frozen = True

    class DoubleType(pydantic.BaseModel):
        type: typing_extensions.Literal["doubleType"]

        class Config:
            frozen = True

    class BooleanType(pydantic.BaseModel):
        type: typing_extensions.Literal["booleanType"]

        class Config:
            frozen = True

    class StringType(pydantic.BaseModel):
        type: typing_extensions.Literal["stringType"]

        class Config:
            frozen = True

    class CharType(pydantic.BaseModel):
        type: typing_extensions.Literal["charType"]

        class Config:
            frozen = True

    class ListType(ListType):
        type: typing_extensions.Literal["listType"]

        class Config:
            frozen = True

    class MapType(MapType):
        type: typing_extensions.Literal["mapType"]

        class Config:
            frozen = True

    class BinaryTreeType(pydantic.BaseModel):
        type: typing_extensions.Literal["binaryTreeType"]

        class Config:
            frozen = True

    class SinglyLinkedListType(pydantic.BaseModel):
        type: typing_extensions.Literal["singlyLinkedListType"]

        class Config:
            frozen = True

    class DoublyLinkedListType(pydantic.BaseModel):
        type: typing_extensions.Literal["doublyLinkedListType"]

        class Config:
            frozen = True


VariableType.update_forward_refs()
