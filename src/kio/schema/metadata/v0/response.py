"""
Generated from MetadataResponse.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.primitive import i32
from kio.schema.types import BrokerId
from kio.schema.types import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataResponseBroker:
    __flexible__: ClassVar[bool] = False
    node_id: BrokerId = field(metadata={"kafka_type": "int32"})
    """The broker ID."""
    host: str = field(metadata={"kafka_type": "string"})
    """The broker hostname."""
    port: i32 = field(metadata={"kafka_type": "int32"})
    """The broker port."""


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataResponsePartition:
    __flexible__: ClassVar[bool] = False
    error_code: i16 = field(metadata={"kafka_type": "int16"})
    """The partition error, or 0 if there was no error."""
    partition_index: i32 = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    leader_id: BrokerId = field(metadata={"kafka_type": "int32"})
    """The ID of the leader broker."""
    replica_nodes: tuple[BrokerId, ...] = field(
        metadata={"kafka_type": "int32"}, default=()
    )
    """The set of all nodes that host this partition."""
    isr_nodes: tuple[BrokerId, ...] = field(
        metadata={"kafka_type": "int32"}, default=()
    )
    """The set of nodes that are in sync with the leader for this partition."""


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataResponseTopic:
    __flexible__: ClassVar[bool] = False
    error_code: i16 = field(metadata={"kafka_type": "int16"})
    """The topic error, or 0 if there was no error."""
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    partitions: tuple[MetadataResponsePartition, ...]
    """Each partition in the topic."""


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataResponse:
    __flexible__: ClassVar[bool] = False
    brokers: tuple[MetadataResponseBroker, ...]
    """Each broker in the response."""
    topics: tuple[MetadataResponseTopic, ...]
    """Each topic in the response."""