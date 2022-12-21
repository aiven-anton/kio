"""
Generated from CreateTopicsResponse.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.entity import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class CreatableTopicConfigs:
    __flexible__: ClassVar[bool] = True
    name: str = field(metadata={"kafka_type": "string"})
    """The configuration name."""
    value: str | None = field(metadata={"kafka_type": "string"})
    """The configuration value."""
    read_only: bool = field(metadata={"kafka_type": "bool"})
    """True if the configuration is read-only."""
    config_source: int = field(metadata={"kafka_type": "int8"}, default=-1)
    """The configuration source."""
    is_sensitive: bool = field(metadata={"kafka_type": "bool"})
    """True if this configuration is sensitive."""


@dataclass(frozen=True, slots=True, kw_only=True)
class CreatableTopicResult:
    __flexible__: ClassVar[bool] = True
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    error_code: int = field(metadata={"kafka_type": "int16"})
    """The error code, or 0 if there was no error."""
    error_message: str | None = field(metadata={"kafka_type": "string"})
    """The error message, or null if there was no error."""
    topic_config_error_code: int = field(metadata={"kafka_type": "int16"})
    """Optional topic config error returned if configs are not returned in the response."""
    num_partitions: int = field(metadata={"kafka_type": "int32"}, default=-1)
    """Number of partitions of the topic."""
    replication_factor: int = field(metadata={"kafka_type": "int16"}, default=-1)
    """Replication factor of the topic."""
    configs: tuple[CreatableTopicConfigs, ...]
    """Configuration of the topic."""


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateTopicsResponse:
    __flexible__: ClassVar[bool] = True
    throttle_time_ms: int = field(metadata={"kafka_type": "int32"})
    """The duration in milliseconds for which the request was throttled due to a quota violation, or zero if the request did not violate any quota."""
    topics: tuple[CreatableTopicResult, ...]
    """Results for each topic we tried to create."""
