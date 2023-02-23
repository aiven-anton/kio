from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.envelope.v0.response import EnvelopeResponse
from kio.serial import entity_decoder
from kio.serial import entity_writer
from kio.serial import read_sync
from tests.conftest import setup_buffer


@given(from_type(EnvelopeResponse))
@settings(max_examples=1)
def test_envelope_response_roundtrip(instance: EnvelopeResponse) -> None:
    writer = entity_writer(EnvelopeResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_sync(buffer, entity_decoder(EnvelopeResponse))
    assert instance == result