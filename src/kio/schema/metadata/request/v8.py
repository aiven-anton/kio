"""
Generated from MetadataRequest.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.entity import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataRequestTopic:
    __flexible__: ClassVar[bool] = False
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataRequest:
    __flexible__: ClassVar[bool] = False
    topics: tuple[MetadataRequestTopic, ...]
    """The topics to fetch metadata for."""
    allow_auto_topic_creation: bool = field(
        metadata={"kafka_type": "bool"}, default=True
    )
    """If this is true, the broker may auto-create topics that we requested which do not already exist, if it is configured to do so."""
    include_cluster_authorized_operations: bool = field(metadata={"kafka_type": "bool"})
    """Whether to include cluster authorized operations."""
    include_topic_authorized_operations: bool = field(metadata={"kafka_type": "bool"})
    """Whether to include topic authorized operations."""
