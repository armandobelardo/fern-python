# This file was auto-generated by Fern from our API Definition.

import typing

from .binary_tree_node_value import BinaryTreeNodeValue
from .node_id import NodeId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BinaryTreeValue(pydantic.BaseModel):
    root: typing.Optional[NodeId]
    nodes: typing.Dict[NodeId, BinaryTreeNodeValue]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
