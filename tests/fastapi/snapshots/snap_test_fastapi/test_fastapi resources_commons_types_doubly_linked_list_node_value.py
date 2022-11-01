# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .node_id import NodeId


class DoublyLinkedListNodeValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    val: float
    next: typing.Optional[NodeId]
    prev: typing.Optional[NodeId]

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        val: typing_extensions.NotRequired[float]
        next: typing_extensions.NotRequired[typing.Optional[NodeId]]
        prev: typing_extensions.NotRequired[typing.Optional[NodeId]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DoublyLinkedListNodeValue.Validators.root
            def validate(values: DoublyLinkedListNodeValue.Partial) -> DoublyLinkedListNodeValue.Partial:
                ...

            @DoublyLinkedListNodeValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: DoublyLinkedListNodeValue.Partial) -> NodeId:
                ...

            @DoublyLinkedListNodeValue.Validators.field("val")
            def validate_val(val: float, values: DoublyLinkedListNodeValue.Partial) -> float:
                ...

            @DoublyLinkedListNodeValue.Validators.field("next")
            def validate_next(next: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial) -> typing.Optional[NodeId]:
                ...

            @DoublyLinkedListNodeValue.Validators.field("prev")
            def validate_prev(prev: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial) -> typing.Optional[NodeId]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[DoublyLinkedListNodeValue.Partial], DoublyLinkedListNodeValue.Partial]]
        ] = []
        _node_id_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.NodeIdValidator]] = []
        _val_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.ValValidator]] = []
        _next_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.NextValidator]] = []
        _prev_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.PrevValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[DoublyLinkedListNodeValue.Partial], DoublyLinkedListNodeValue.Partial]
        ) -> typing.Callable[[DoublyLinkedListNodeValue.Partial], DoublyLinkedListNodeValue.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"]
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.NodeIdValidator], DoublyLinkedListNodeValue.Validators.NodeIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["val"]
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.ValValidator], DoublyLinkedListNodeValue.Validators.ValValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["next"]
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.NextValidator], DoublyLinkedListNodeValue.Validators.NextValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["prev"]
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.PrevValidator], DoublyLinkedListNodeValue.Validators.PrevValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    cls._node_id_validators.append(validator)
                if field_name == "val":
                    cls._val_validators.append(validator)
                if field_name == "next":
                    cls._next_validators.append(validator)
                if field_name == "prev":
                    cls._prev_validators.append(validator)
                return validator

            return decorator

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, *, node_id: NodeId, values: DoublyLinkedListNodeValue.Partial) -> NodeId:
                ...

        class ValValidator(typing_extensions.Protocol):
            def __call__(self, *, val: float, values: DoublyLinkedListNodeValue.Partial) -> float:
                ...

        class NextValidator(typing_extensions.Protocol):
            def __call__(
                self, *, next: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class PrevValidator(typing_extensions.Protocol):
            def __call__(
                self, *, prev: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: DoublyLinkedListNodeValue.Partial) -> DoublyLinkedListNodeValue.Partial:
        for validator in DoublyLinkedListNodeValue.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id")
    def _validate_node_id(cls, node_id: NodeId, values: DoublyLinkedListNodeValue.Partial) -> NodeId:
        for validator in DoublyLinkedListNodeValue.Validators._node_id_validators:
            node_id = validator(node_id, values=values)
        return node_id

    @pydantic.validator("val")
    def _validate_val(cls, val: float, values: DoublyLinkedListNodeValue.Partial) -> float:
        for validator in DoublyLinkedListNodeValue.Validators._val_validators:
            val = validator(val, values=values)
        return val

    @pydantic.validator("next")
    def _validate_next(
        cls, next: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListNodeValue.Validators._next_validators:
            next = validator(next, values=values)
        return next

    @pydantic.validator("prev")
    def _validate_prev(
        cls, prev: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListNodeValue.Validators._prev_validators:
            prev = validator(prev, values=values)
        return prev

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
