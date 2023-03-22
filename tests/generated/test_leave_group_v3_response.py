from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.leave_group.v3.response import LeaveGroupResponse
from kio.schema.leave_group.v3.response import MemberResponse
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_member_response: Final = entity_reader(MemberResponse)


@given(from_type(MemberResponse))
@settings(max_examples=1)
def test_member_response_roundtrip(instance: MemberResponse) -> None:
    writer = entity_writer(MemberResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_member_response(buffer)
    assert instance == result


read_leave_group_response: Final = entity_reader(LeaveGroupResponse)


@given(from_type(LeaveGroupResponse))
@settings(max_examples=1)
def test_leave_group_response_roundtrip(instance: LeaveGroupResponse) -> None:
    writer = entity_writer(LeaveGroupResponse)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_leave_group_response(buffer)
    assert instance == result
