from __future__ import annotations

from typing import Final

import pytest

from hypothesis import given
from hypothesis.strategies import from_type

from kio.schema.delete_topics.v5.request import DeleteTopicsRequest
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import JavaTester
from tests.conftest import setup_buffer

read_delete_topics_request: Final = entity_reader(DeleteTopicsRequest)


@pytest.mark.roundtrip
@given(from_type(DeleteTopicsRequest))
def test_delete_topics_request_roundtrip(instance: DeleteTopicsRequest) -> None:
    writer = entity_writer(DeleteTopicsRequest)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_delete_topics_request(buffer)
    assert instance == result


@pytest.mark.java
@given(instance=from_type(DeleteTopicsRequest))
def test_delete_topics_request_java(
    instance: DeleteTopicsRequest, java_tester: JavaTester
) -> None:
    java_tester.test(instance)
