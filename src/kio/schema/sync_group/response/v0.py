"""
Generated from SyncGroupResponse.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar


@dataclass(frozen=True, slots=True, kw_only=True)
class SyncGroupResponse:
    __flexible__: ClassVar[bool] = False
    error_code: int = field(metadata={"kafka_type": "int16"})
    """The error code, or 0 if there was no error."""
    assignment: bytes = field(metadata={"kafka_type": "bytes"})
    """The member assignment."""
