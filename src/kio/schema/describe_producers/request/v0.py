"""
Generated from DescribeProducersRequest.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.entity import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class TopicRequest:
    __flexible__: ClassVar[bool] = True
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    partition_indexes: tuple[int, ...] = field(
        metadata={"kafka_type": "int32"}, default=()
    )
    """The indexes of the partitions to list producers for."""


@dataclass(frozen=True, slots=True, kw_only=True)
class DescribeProducersRequest:
    __flexible__: ClassVar[bool] = True
    topics: tuple[TopicRequest, ...]
