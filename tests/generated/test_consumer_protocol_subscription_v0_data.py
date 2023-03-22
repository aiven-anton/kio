from __future__ import annotations

from typing import Final

from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import from_type

from kio.schema.consumer_protocol_subscription.v0.data import (
    ConsumerProtocolSubscription,
)
from kio.serial import entity_reader
from kio.serial import entity_writer
from tests.conftest import setup_buffer

read_consumer_protocol_subscription: Final = entity_reader(ConsumerProtocolSubscription)


@given(from_type(ConsumerProtocolSubscription))
@settings(max_examples=1)
def test_consumer_protocol_subscription_roundtrip(
    instance: ConsumerProtocolSubscription,
) -> None:
    writer = entity_writer(ConsumerProtocolSubscription)
    with setup_buffer() as buffer:
        writer(buffer, instance)
        buffer.seek(0)
        result = read_consumer_protocol_subscription(buffer)
    assert instance == result
