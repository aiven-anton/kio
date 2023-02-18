"""
Generated from WriteTxnMarkersRequest.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.primitive import i32
from kio.schema.types import ProducerId
from kio.schema.types import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class WritableTxnMarkerTopic:
    __flexible__: ClassVar[bool] = False
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    partition_indexes: tuple[i32, ...] = field(
        metadata={"kafka_type": "int32"}, default=()
    )
    """The indexes of the partitions to write transaction markers for."""


@dataclass(frozen=True, slots=True, kw_only=True)
class WritableTxnMarker:
    __flexible__: ClassVar[bool] = False
    producer_id: ProducerId = field(metadata={"kafka_type": "int64"})
    """The current producer ID."""
    producer_epoch: i16 = field(metadata={"kafka_type": "int16"})
    """The current epoch associated with the producer ID."""
    transaction_result: bool = field(metadata={"kafka_type": "bool"})
    """The result of the transaction to write to the partitions (false = ABORT, true = COMMIT)."""
    topics: tuple[WritableTxnMarkerTopic, ...]
    """Each topic that we want to write transaction marker(s) for."""
    coordinator_epoch: i32 = field(metadata={"kafka_type": "int32"})
    """Epoch associated with the transaction state partition hosted by this transaction coordinator"""


@dataclass(frozen=True, slots=True, kw_only=True)
class WriteTxnMarkersRequest:
    __flexible__: ClassVar[bool] = False
    markers: tuple[WritableTxnMarker, ...]
    """The transaction markers to be written."""
