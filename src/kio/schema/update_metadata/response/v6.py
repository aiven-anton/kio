"""
Generated from UpdateMetadataResponse.json.
"""
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateMetadataResponse:
    __flexible__: ClassVar[bool] = True
    error_code: int = field(metadata={"kafka_type": "int16"})
    """The error code, or 0 if there was no error."""
