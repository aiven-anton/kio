from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.list_groups.v1.response import ListedGroup
from kio.schema.list_groups.v1.response import ListGroupsResponse
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_listed_group: Final = entity_reader(ListedGroup)


@given(from_type(ListedGroup))
@settings(max_examples=1)
def test_listed_group_roundtrip(instance: ListedGroup) -> None:
    writer = entity_writer(ListedGroup)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_listed_group(buffer)
    assert instance == result


read_list_groups_response: Final = entity_reader(ListGroupsResponse)


@given(from_type(ListGroupsResponse))
@settings(max_examples=1)
def test_list_groups_response_roundtrip(instance: ListGroupsResponse) -> None:
    writer = entity_writer(ListGroupsResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_list_groups_response(buffer)
    assert instance == result
