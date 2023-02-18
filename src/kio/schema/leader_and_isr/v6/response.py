"""
Generated from LeaderAndIsrResponse.json.
"""
import uuid
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.primitive import i32


@dataclass(frozen=True, slots=True, kw_only=True)
class LeaderAndIsrPartitionError:
    __flexible__: ClassVar[bool] = True
    partition_index: i32 = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    error_code: i16 = field(metadata={"kafka_type": "int16"})
    """The partition error code, or 0 if there was no error."""


@dataclass(frozen=True, slots=True, kw_only=True)
class LeaderAndIsrTopicError:
    __flexible__: ClassVar[bool] = True
    topic_id: uuid.UUID = field(metadata={"kafka_type": "uuid"})
    """The unique topic ID"""
    partition_errors: tuple[LeaderAndIsrPartitionError, ...]
    """Each partition."""


@dataclass(frozen=True, slots=True, kw_only=True)
class LeaderAndIsrResponse:
    __flexible__: ClassVar[bool] = True
    error_code: i16 = field(metadata={"kafka_type": "int16"})
    """The error code, or 0 if there was no error."""
    topics: tuple[LeaderAndIsrTopicError, ...]
    """Each topic"""