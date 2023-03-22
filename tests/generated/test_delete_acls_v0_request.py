from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.delete_acls.v0.request import DeleteAclsFilter
from kio.schema.delete_acls.v0.request import DeleteAclsRequest
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_delete_acls_filter: Final = entity_reader(DeleteAclsFilter)


@given(from_type(DeleteAclsFilter))
@settings(max_examples=1)
def test_delete_acls_filter_roundtrip(instance: DeleteAclsFilter) -> None:
    writer = entity_writer(DeleteAclsFilter)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_delete_acls_filter(buffer)
    assert instance == result


read_delete_acls_request: Final = entity_reader(DeleteAclsRequest)


@given(from_type(DeleteAclsRequest))
@settings(max_examples=1)
def test_delete_acls_request_roundtrip(instance: DeleteAclsRequest) -> None:
    writer = entity_writer(DeleteAclsRequest)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_delete_acls_request(buffer)
    assert instance == result
