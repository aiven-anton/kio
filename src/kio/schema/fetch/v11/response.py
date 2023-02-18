"""
Generated from FetchResponse.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.primitive import i32
from kio.schema.primitive import i64
from kio.schema.types import BrokerId
from kio.schema.types import ProducerId
from kio.schema.types import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class AbortedTransaction:
    __flexible__: ClassVar[bool] = False
    producer_id: ProducerId = field(metadata={"kafka_type": "int64"})
    """The producer id associated with the aborted transaction."""
    first_offset: i64 = field(metadata={"kafka_type": "int64"})
    """The first offset in the aborted transaction."""


@dataclass(frozen=True, slots=True, kw_only=True)
class PartitionData:
    __flexible__: ClassVar[bool] = False
    partition_index: i32 = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    error_code: i16 = field(metadata={"kafka_type": "int16"})
    """The error code, or 0 if there was no fetch error."""
    high_watermark: i64 = field(metadata={"kafka_type": "int64"})
    """The current high water mark."""
    last_stable_offset: i64 = field(metadata={"kafka_type": "int64"}, default=i64(-1))
    """The last stable offset (or LSO) of the partition. This is the last offset such that the state of all transactional records prior to this offset have been decided (ABORTED or COMMITTED)"""
    log_start_offset: i64 = field(metadata={"kafka_type": "int64"}, default=i64(-1))
    """The current log start offset."""
    aborted_transactions: tuple[AbortedTransaction, ...]
    """The aborted transactions."""
    preferred_read_replica: BrokerId = field(
        metadata={"kafka_type": "int32"}, default=BrokerId(i32(-1))
    )
    """The preferred read replica for the consumer to use on its next fetch request"""
    records: tuple[bytes | None, ...] | None = field(metadata={"kafka_type": "records"})
    """The record data."""


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchableTopicResponse:
    __flexible__: ClassVar[bool] = False
    topic: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    partitions: tuple[PartitionData, ...]
    """The topic partitions."""


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchResponse:
    __flexible__: ClassVar[bool] = False
    throttle_time_ms: i32 = field(metadata={"kafka_type": "int32"})
    """The duration in milliseconds for which the request was throttled due to a quota violation, or zero if the request did not violate any quota."""
    error_code: i16 = field(metadata={"kafka_type": "int16"})
    """The top level response error code."""
    session_id: i32 = field(metadata={"kafka_type": "int32"}, default=i32(0))
    """The fetch session ID, or 0 if this is not part of a fetch session."""
    responses: tuple[FetchableTopicResponse, ...]
    """The response topics."""