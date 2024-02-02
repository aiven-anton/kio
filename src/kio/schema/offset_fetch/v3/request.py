"""
Generated from OffsetFetchRequest.json.

https://github.com/apache/kafka/tree/3.6.0/clients/src/main/resources/common/message/OffsetFetchRequest.json
"""

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.request_header.v1.header import RequestHeader
from kio.schema.types import GroupId
from kio.schema.types import TopicName
from kio.static.constants import EntityType
from kio.static.primitive import i16
from kio.static.primitive import i32


@dataclass(frozen=True, slots=True, kw_only=True)
class OffsetFetchRequestTopic:
    __type__: ClassVar = EntityType.nested
    __version__: ClassVar[i16] = i16(3)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(9)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    partition_indexes: tuple[i32, ...] = field(
        metadata={"kafka_type": "int32"}, default=()
    )
    """The partition indexes we would like to fetch offsets for."""


@dataclass(frozen=True, slots=True, kw_only=True)
class OffsetFetchRequest:
    __type__: ClassVar = EntityType.request
    __version__: ClassVar[i16] = i16(3)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(9)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    group_id: GroupId = field(metadata={"kafka_type": "string"})
    """The group to fetch offsets for."""
    topics: tuple[OffsetFetchRequestTopic, ...] | None
    """Each topic we would like to fetch offsets for, or null to fetch offsets for all topics."""
