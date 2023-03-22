from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.alter_partition.v1.response import AlterPartitionResponse
from kio.schema.alter_partition.v1.response import PartitionData
from kio.schema.alter_partition.v1.response import TopicData
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_partition_data: Final = entity_reader(PartitionData)


@given(from_type(PartitionData))
@settings(max_examples=1)
def test_partition_data_roundtrip(instance: PartitionData) -> None:
    writer = entity_writer(PartitionData)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_partition_data(buffer)
    assert instance == result


read_topic_data: Final = entity_reader(TopicData)


@given(from_type(TopicData))
@settings(max_examples=1)
def test_topic_data_roundtrip(instance: TopicData) -> None:
    writer = entity_writer(TopicData)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_topic_data(buffer)
    assert instance == result


read_alter_partition_response: Final = entity_reader(AlterPartitionResponse)


@given(from_type(AlterPartitionResponse))
@settings(max_examples=1)
def test_alter_partition_response_roundtrip(instance: AlterPartitionResponse) -> None:
    writer = entity_writer(AlterPartitionResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_alter_partition_response(buffer)
    assert instance == result
