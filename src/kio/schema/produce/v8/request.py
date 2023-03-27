"""
Generated from ProduceRequest.json.
"""

# ruff: noqa: A003

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.primitive import i32
from kio.schema.request_header.v1.header import RequestHeader
from kio.schema.types import TopicName
from kio.schema.types import TransactionalId


@dataclass(frozen=True, slots=True, kw_only=True)
class PartitionProduceData:
    __version__: ClassVar[i16] = i16(8)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(0)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    index: i32 = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    records: tuple[bytes | None, ...] = field(metadata={"kafka_type": "records"})
    """The record data to be produced."""


@dataclass(frozen=True, slots=True, kw_only=True)
class TopicProduceData:
    __version__: ClassVar[i16] = i16(8)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(0)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    partition_data: tuple[PartitionProduceData, ...]
    """Each partition to produce to."""


@dataclass(frozen=True, slots=True, kw_only=True)
class ProduceRequest:
    __version__: ClassVar[i16] = i16(8)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(0)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    transactional_id: TransactionalId | None = field(
        metadata={"kafka_type": "string"}, default=None
    )
    """The transactional ID, or null if the producer is not transactional."""
    acks: i16 = field(metadata={"kafka_type": "int16"})
    """The number of acknowledgments the producer requires the leader to have received before considering a request complete. Allowed values: 0 for no acknowledgments, 1 for only the leader and -1 for the full ISR."""
    timeout_ms: i32 = field(metadata={"kafka_type": "int32"})
    """The timeout to await a response in milliseconds."""
    topic_data: tuple[TopicProduceData, ...]
    """Each topic to produce to."""
