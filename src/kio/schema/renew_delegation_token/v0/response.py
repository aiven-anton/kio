"""
Generated from RenewDelegationTokenResponse.json.
"""

# ruff: noqa: A003

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from phantom.datetime import TZAware

from kio.schema.response_header.v0.header import ResponseHeader
from kio.static.constants import ErrorCode
from kio.static.primitive import i16
from kio.static.primitive import i32Timedelta


@dataclass(frozen=True, slots=True, kw_only=True)
class RenewDelegationTokenResponse:
    __version__: ClassVar[i16] = i16(0)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(39)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    error_code: ErrorCode = field(metadata={"kafka_type": "error_code"})
    """The error code, or 0 if there was no error."""
    expiry_timestamp: TZAware = field(metadata={"kafka_type": "datetime_i64"})
    """The timestamp in milliseconds at which this token expires."""
    throttle_time: i32Timedelta = field(metadata={"kafka_type": "timedelta_i32"})
    """The duration in milliseconds for which the request was throttled due to a quota violation, or zero if the request did not violate any quota."""
