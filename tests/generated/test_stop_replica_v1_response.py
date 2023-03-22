from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.stop_replica.v1.response import StopReplicaPartitionError
from kio.schema.stop_replica.v1.response import StopReplicaResponse
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_stop_replica_partition_error: Final = entity_reader(StopReplicaPartitionError)


@given(from_type(StopReplicaPartitionError))
@settings(max_examples=1)
def test_stop_replica_partition_error_roundtrip(
    instance: StopReplicaPartitionError,
) -> None:
    writer = entity_writer(StopReplicaPartitionError)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_stop_replica_partition_error(buffer)
    assert instance == result


read_stop_replica_response: Final = entity_reader(StopReplicaResponse)


@given(from_type(StopReplicaResponse))
@settings(max_examples=1)
def test_stop_replica_response_roundtrip(instance: StopReplicaResponse) -> None:
    writer = entity_writer(StopReplicaResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_stop_replica_response(buffer)
    assert instance == result
