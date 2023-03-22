from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.end_txn.v1.request import EndTxnRequest
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_end_txn_request: Final = entity_reader(EndTxnRequest)


@given(from_type(EndTxnRequest))
@settings(max_examples=1)
def test_end_txn_request_roundtrip(instance: EndTxnRequest) -> None:
    writer = entity_writer(EndTxnRequest)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_end_txn_request(buffer)
    assert instance == result
