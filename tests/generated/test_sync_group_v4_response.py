from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.sync_group.v4.response import SyncGroupResponse
from kio.serial import entity_decoder
from kio.serial import entity_writer
from kio.serial import read_sync
from tests.conftest import setup_buffer


@given(from_type(SyncGroupResponse))
@settings(max_examples=1)
def test_sync_group_response_roundtrip(instance: SyncGroupResponse) -> None:
    writer = entity_writer(SyncGroupResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_sync(buffer, entity_decoder(SyncGroupResponse))
    assert instance == result
