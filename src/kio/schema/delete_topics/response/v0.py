"""
Generated from DeleteTopicsResponse.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.entity import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class DeletableTopicResult:
    __flexible__: ClassVar[bool] = False
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name"""
    error_code: int = field(metadata={"kafka_type": "int16"})
    """The deletion error, or 0 if the deletion succeeded."""


@dataclass(frozen=True, slots=True, kw_only=True)
class DeleteTopicsResponse:
    __flexible__: ClassVar[bool] = False
    responses: tuple[DeletableTopicResult, ...]
    """The results for each topic we tried to delete."""
