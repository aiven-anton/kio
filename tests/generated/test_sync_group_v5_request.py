from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.sync_group.v5.request import SyncGroupRequest
from kio.schema.sync_group.v5.request import SyncGroupRequestAssignment
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_sync_group_request_assignment: Final = entity_reader(SyncGroupRequestAssignment)


@given(from_type(SyncGroupRequestAssignment))
@settings(max_examples=1)
def test_sync_group_request_assignment_roundtrip(
    instance: SyncGroupRequestAssignment,
) -> None:
    writer = entity_writer(SyncGroupRequestAssignment)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_sync_group_request_assignment(buffer)
    assert instance == result


read_sync_group_request: Final = entity_reader(SyncGroupRequest)


@given(from_type(SyncGroupRequest))
@settings(max_examples=1)
def test_sync_group_request_roundtrip(instance: SyncGroupRequest) -> None:
    writer = entity_writer(SyncGroupRequest)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_sync_group_request(buffer)
    assert instance == result
