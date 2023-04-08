# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .doubly_linked_list_node_value import DoublyLinkedListNodeValue
from .node_id import NodeId


class DoublyLinkedListValue(pydantic.BaseModel):
    head: typing.Optional[NodeId]
    nodes: typing.Dict[NodeId, DoublyLinkedListNodeValue]

    class Partial(typing_extensions.TypedDict):
        head: typing_extensions.NotRequired[typing.Optional[NodeId]]
        nodes: typing_extensions.NotRequired[typing.Dict[NodeId, DoublyLinkedListNodeValue]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DoublyLinkedListValue.Validators.root()
            def validate(values: DoublyLinkedListValue.Partial) -> DoublyLinkedListValue.Partial:
                ...

            @DoublyLinkedListValue.Validators.field("head")
            def validate_head(head: typing.Optional[NodeId], values: DoublyLinkedListValue.Partial) -> typing.Optional[NodeId]:
                ...

            @DoublyLinkedListValue.Validators.field("nodes")
            def validate_nodes(nodes: typing.Dict[NodeId, DoublyLinkedListNodeValue], values: DoublyLinkedListValue.Partial) -> typing.Dict[NodeId, DoublyLinkedListNodeValue]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators._RootValidator]] = []
        _head_pre_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators.PreHeadValidator]] = []
        _head_post_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators.HeadValidator]] = []
        _nodes_pre_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators.PreNodesValidator]] = []
        _nodes_post_validators: typing.ClassVar[typing.List[DoublyLinkedListValue.Validators.NodesValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators._RootValidator], DoublyLinkedListValue.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators._PreRootValidator], DoublyLinkedListValue.Validators._PreRootValidator
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["head"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators.PreHeadValidator], DoublyLinkedListValue.Validators.PreHeadValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["head"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators.HeadValidator], DoublyLinkedListValue.Validators.HeadValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["nodes"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators.PreNodesValidator], DoublyLinkedListValue.Validators.PreNodesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["nodes"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DoublyLinkedListValue.Validators.NodesValidator], DoublyLinkedListValue.Validators.NodesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "head":
                    if pre:
                        cls._head_pre_validators.append(validator)
                    else:
                        cls._head_post_validators.append(validator)
                if field_name == "nodes":
                    if pre:
                        cls._nodes_pre_validators.append(validator)
                    else:
                        cls._nodes_post_validators.append(validator)
                return validator

            return decorator

        class PreHeadValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DoublyLinkedListValue.Partial) -> typing.Any:
                ...

        class HeadValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[NodeId], __values: DoublyLinkedListValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class PreNodesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DoublyLinkedListValue.Partial) -> typing.Any:
                ...

        class NodesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[NodeId, DoublyLinkedListNodeValue], __values: DoublyLinkedListValue.Partial
            ) -> typing.Dict[NodeId, DoublyLinkedListNodeValue]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: DoublyLinkedListValue.Partial) -> DoublyLinkedListValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: DoublyLinkedListValue.Partial) -> DoublyLinkedListValue.Partial:
        for validator in DoublyLinkedListValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: DoublyLinkedListValue.Partial) -> DoublyLinkedListValue.Partial:
        for validator in DoublyLinkedListValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("head", pre=True)
    def _pre_validate_head(
        cls, v: typing.Optional[NodeId], values: DoublyLinkedListValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListValue.Validators._head_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("head", pre=False)
    def _post_validate_head(
        cls, v: typing.Optional[NodeId], values: DoublyLinkedListValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListValue.Validators._head_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("nodes", pre=True)
    def _pre_validate_nodes(
        cls, v: typing.Dict[NodeId, DoublyLinkedListNodeValue], values: DoublyLinkedListValue.Partial
    ) -> typing.Dict[NodeId, DoublyLinkedListNodeValue]:
        for validator in DoublyLinkedListValue.Validators._nodes_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("nodes", pre=False)
    def _post_validate_nodes(
        cls, v: typing.Dict[NodeId, DoublyLinkedListNodeValue], values: DoublyLinkedListValue.Partial
    ) -> typing.Dict[NodeId, DoublyLinkedListNodeValue]:
        for validator in DoublyLinkedListValue.Validators._nodes_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        orm_mode = True
        json_encoders = {dt.datetime: serialize_datetime}
