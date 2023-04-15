from dataclasses import Field
from dataclasses import fields
from typing import IO
from typing import TypeVar
from typing import assert_never

from kio.static.protocol import Entity

from . import readers
from ._introspect import FieldKind
from ._introspect import classify_field
from ._introspect import get_field_tag
from ._introspect import get_schema_field_type
from ._introspect import is_optional


def get_reader(
    kafka_type: str,
    flexible: bool,
    optional: bool,
) -> readers.Reader:
    match (kafka_type, flexible, optional):
        case ("int8", _, False):
            return readers.read_int8
        case ("int16", _, False):
            return readers.read_int16
        case ("int32", _, False):
            return readers.read_int32
        case ("int64", _, False):
            return readers.read_int64
        case ("uint8", _, False):
            return readers.read_uint8
        case ("uint16", _, False):
            return readers.read_uint16
        case ("uint32", _, False):
            return readers.read_uint32
        case ("uint64", _, False):
            return readers.read_uint64
        case ("float64", _, False):
            return readers.read_float64
        case ("string", True, False):
            return readers.read_compact_string
        case ("string", True, True):
            return readers.read_compact_string_nullable
        case ("string", False, False):
            return readers.read_legacy_string
        case ("string", False, True):
            return readers.read_nullable_legacy_string
        case ("bytes", True, False):
            return readers.read_compact_string_as_bytes
        case ("bytes", True, True):
            return readers.read_compact_string_as_bytes_nullable
        case ("bytes", False, False):
            return readers.read_legacy_bytes
        case ("bytes", False, True):
            return readers.read_nullable_legacy_bytes
        case ("records", _, True):
            return readers.read_nullable_legacy_bytes
        case ("uuid", _, True):
            return readers.read_uuid
        case ("bool", _, False):
            return readers.read_boolean
        case ("error_code", _, False):
            return readers.read_error_code

    raise NotImplementedError(
        f"Failed identifying reader for {kafka_type!r} field {flexible=} {optional=}"
    )


T = TypeVar("T")


def get_field_reader(
    entity_type: type[Entity],
    field: Field[T],
    is_request_header: bool,
    is_tagged_field: bool,
) -> readers.Reader[T]:
    # RequestHeader.client_id is special-cased by Kafka to always use the legacy string
    # format.
    # https://github.com/apache/kafka/blob/trunk/clients/src/main/resources/common/message/RequestHeader.json#L34-L38
    if is_request_header and field.name == "client_id":
        return readers.read_nullable_legacy_string  # type: ignore[return-value]

    field_kind, field_type = classify_field(field)
    flexible = entity_type.__flexible__
    array_reader = (
        readers.compact_array_reader if flexible else readers.legacy_array_reader
    )

    match field_kind:
        case FieldKind.primitive:
            return get_reader(
                kafka_type=get_schema_field_type(field),
                flexible=flexible,
                optional=is_optional(field) and not is_tagged_field,
            )
        case FieldKind.primitive_tuple:
            return array_reader(  # type: ignore[return-value]
                get_reader(
                    kafka_type=get_schema_field_type(field),
                    flexible=flexible,
                    optional=is_optional(field) and not is_tagged_field,
                )
            )
        case FieldKind.entity:
            return entity_reader(field_type)  # type: ignore[type-var]
        case FieldKind.entity_tuple:
            return array_reader(  # type: ignore[return-value]
                entity_reader(field_type)  # type: ignore[type-var]
            )
        case no_match:
            assert_never(no_match)


E = TypeVar("E", bound=Entity)


def entity_reader(entity_type: type[E]) -> readers.Reader[E]:
    def read_entity(buffer: IO[bytes]) -> E:
        is_request_header = entity_type.__name__ == "RequestHeader"
        kwargs = {}
        tagged_fields = {}

        for field in fields(entity_type):
            tag = get_field_tag(field)
            field_reader = get_field_reader(
                entity_type=entity_type,
                field=field,
                is_request_header=is_request_header,
                is_tagged_field=tag is not None,
            )
            if tag is not None:
                tagged_fields[tag] = field, field_reader
            else:
                kwargs[field.name] = field_reader(buffer)

        if not entity_type.__flexible__:
            # Assert we don't find tags for non-flexible models.
            assert not tagged_fields
            return entity_type(**kwargs)

        num_tagged_fields = readers.read_unsigned_varint(buffer)

        for _ in range(num_tagged_fields):
            field_tag = readers.read_unsigned_varint(buffer)
            readers.read_unsigned_varint(buffer)  # field length
            field, read_field = tagged_fields[field_tag]
            kwargs[field.name] = read_field(buffer)

        return entity_type(**kwargs)

    return read_entity