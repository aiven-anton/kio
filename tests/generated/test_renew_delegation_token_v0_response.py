from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.renew_delegation_token.v0.response import RenewDelegationTokenResponse
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_renew_delegation_token_response: Final = entity_reader(
    RenewDelegationTokenResponse
)


@given(from_type(RenewDelegationTokenResponse))
@settings(max_examples=1)
def test_renew_delegation_token_response_roundtrip(
    instance: RenewDelegationTokenResponse,
) -> None:
    writer = entity_writer(RenewDelegationTokenResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_renew_delegation_token_response(buffer)
    assert instance == result
