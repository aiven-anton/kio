"""
Generated from FetchRequest.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.entity import BrokerId
from kio.schema.entity import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchPartition:
    __flexible__: ClassVar[bool] = False
    partition: int = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    fetch_offset: int = field(metadata={"kafka_type": "int64"})
    """The message offset."""
    partition_max_bytes: int = field(metadata={"kafka_type": "int32"})
    """The maximum bytes to fetch from this partition.  See KIP-74 for cases where this limit may not be honored."""


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchTopic:
    __flexible__: ClassVar[bool] = False
    topic: TopicName = field(metadata={"kafka_type": "string"})
    """The name of the topic to fetch."""
    partitions: tuple[FetchPartition, ...]
    """The partitions to fetch."""


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchRequest:
    __flexible__: ClassVar[bool] = False
    replica_id: BrokerId = field(metadata={"kafka_type": "int32"})
    """The broker ID of the follower, of -1 if this request is from a consumer."""
    max_wait_ms: int = field(metadata={"kafka_type": "int32"})
    """The maximum time in milliseconds to wait for the response."""
    min_bytes: int = field(metadata={"kafka_type": "int32"})
    """The minimum bytes to accumulate in the response."""
    max_bytes: int = field(metadata={"kafka_type": "int32"}, default=2147483647)
    """The maximum bytes to fetch.  See KIP-74 for cases where this limit may not be honored."""
    isolation_level: int = field(metadata={"kafka_type": "int8"}, default=0)
    """This setting controls the visibility of transactional records. Using READ_UNCOMMITTED (isolation_level = 0) makes all records visible. With READ_COMMITTED (isolation_level = 1), non-transactional and COMMITTED transactional records are visible. To be more concrete, READ_COMMITTED returns all data from offsets smaller than the current LSO (last stable offset), and enables the inclusion of the list of aborted transactions in the result, which allows consumers to discard ABORTED transactional records"""
    topics: tuple[FetchTopic, ...]
    """The topics to fetch."""
