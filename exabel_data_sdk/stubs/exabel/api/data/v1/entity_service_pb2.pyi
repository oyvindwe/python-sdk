"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from exabel.api.data.v1.entity_messages_pb2 import Entity as exabel___api___data___v1___entity_messages_pb2___Entity, EntityType as exabel___api___data___v1___entity_messages_pb2___EntityType
from exabel.api.data.v1.search_messages_pb2 import SearchTerm as exabel___api___data___v1___search_messages_pb2___SearchTerm
from google.protobuf.descriptor import Descriptor as google___protobuf___descriptor___Descriptor, FileDescriptor as google___protobuf___descriptor___FileDescriptor
from google.protobuf.field_mask_pb2 import FieldMask as google___protobuf___field_mask_pb2___FieldMask
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer
from google.protobuf.message import Message as google___protobuf___message___Message
from typing import Iterable as typing___Iterable, Optional as typing___Optional, Text as typing___Text
from typing_extensions import Literal as typing_extensions___Literal
builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ListEntityTypesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page_size: builtin___int = ...
    page_token: typing___Text = ...

    def __init__(self, *, page_size: typing___Optional[builtin___int]=None, page_token: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'page_size', b'page_size', u'page_token', b'page_token']) -> None:
        ...
type___ListEntityTypesRequest = ListEntityTypesRequest

class ListEntityTypesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    next_page_token: typing___Text = ...
    total_size: builtin___int = ...

    @property
    def entity_types(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[exabel___api___data___v1___entity_messages_pb2___EntityType]:
        ...

    def __init__(self, *, entity_types: typing___Optional[typing___Iterable[exabel___api___data___v1___entity_messages_pb2___EntityType]]=None, next_page_token: typing___Optional[typing___Text]=None, total_size: typing___Optional[builtin___int]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'entity_types', b'entity_types', u'next_page_token', b'next_page_token', u'total_size', b'total_size']) -> None:
        ...
type___ListEntityTypesResponse = ListEntityTypesResponse

class GetEntityTypeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...

    def __init__(self, *, name: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'name', b'name']) -> None:
        ...
type___GetEntityTypeRequest = GetEntityTypeRequest

class CreateEntityTypeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def entity_type(self) -> exabel___api___data___v1___entity_messages_pb2___EntityType:
        ...

    def __init__(self, *, entity_type: typing___Optional[exabel___api___data___v1___entity_messages_pb2___EntityType]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'entity_type', b'entity_type']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'entity_type', b'entity_type']) -> None:
        ...
type___CreateEntityTypeRequest = CreateEntityTypeRequest

class UpdateEntityTypeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    allow_missing: builtin___bool = ...

    @property
    def entity_type(self) -> exabel___api___data___v1___entity_messages_pb2___EntityType:
        ...

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask:
        ...

    def __init__(self, *, entity_type: typing___Optional[exabel___api___data___v1___entity_messages_pb2___EntityType]=None, update_mask: typing___Optional[google___protobuf___field_mask_pb2___FieldMask]=None, allow_missing: typing___Optional[builtin___bool]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'entity_type', b'entity_type', u'update_mask', b'update_mask']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'allow_missing', b'allow_missing', u'entity_type', b'entity_type', u'update_mask', b'update_mask']) -> None:
        ...
type___UpdateEntityTypeRequest = UpdateEntityTypeRequest

class DeleteEntityTypeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...

    def __init__(self, *, name: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'name', b'name']) -> None:
        ...
type___DeleteEntityTypeRequest = DeleteEntityTypeRequest

class ListEntitiesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent: typing___Text = ...
    page_size: builtin___int = ...
    page_token: typing___Text = ...

    def __init__(self, *, parent: typing___Optional[typing___Text]=None, page_size: typing___Optional[builtin___int]=None, page_token: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'page_size', b'page_size', u'page_token', b'page_token', u'parent', b'parent']) -> None:
        ...
type___ListEntitiesRequest = ListEntitiesRequest

class ListEntitiesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    next_page_token: typing___Text = ...
    total_size: builtin___int = ...

    @property
    def entities(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[exabel___api___data___v1___entity_messages_pb2___Entity]:
        ...

    def __init__(self, *, entities: typing___Optional[typing___Iterable[exabel___api___data___v1___entity_messages_pb2___Entity]]=None, next_page_token: typing___Optional[typing___Text]=None, total_size: typing___Optional[builtin___int]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'entities', b'entities', u'next_page_token', b'next_page_token', u'total_size', b'total_size']) -> None:
        ...
type___ListEntitiesResponse = ListEntitiesResponse

class DeleteEntitiesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent: typing___Text = ...
    confirm: builtin___bool = ...

    def __init__(self, *, parent: typing___Optional[typing___Text]=None, confirm: typing___Optional[builtin___bool]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'confirm', b'confirm', u'parent', b'parent']) -> None:
        ...
type___DeleteEntitiesRequest = DeleteEntitiesRequest

class GetEntityRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...

    def __init__(self, *, name: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'name', b'name']) -> None:
        ...
type___GetEntityRequest = GetEntityRequest

class CreateEntityRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent: typing___Text = ...

    @property
    def entity(self) -> exabel___api___data___v1___entity_messages_pb2___Entity:
        ...

    def __init__(self, *, parent: typing___Optional[typing___Text]=None, entity: typing___Optional[exabel___api___data___v1___entity_messages_pb2___Entity]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'entity', b'entity']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'entity', b'entity', u'parent', b'parent']) -> None:
        ...
type___CreateEntityRequest = CreateEntityRequest

class UpdateEntityRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    allow_missing: builtin___bool = ...

    @property
    def entity(self) -> exabel___api___data___v1___entity_messages_pb2___Entity:
        ...

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask:
        ...

    def __init__(self, *, entity: typing___Optional[exabel___api___data___v1___entity_messages_pb2___Entity]=None, update_mask: typing___Optional[google___protobuf___field_mask_pb2___FieldMask]=None, allow_missing: typing___Optional[builtin___bool]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'entity', b'entity', u'update_mask', b'update_mask']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'allow_missing', b'allow_missing', u'entity', b'entity', u'update_mask', b'update_mask']) -> None:
        ...
type___UpdateEntityRequest = UpdateEntityRequest

class DeleteEntityRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...

    def __init__(self, *, name: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'name', b'name']) -> None:
        ...
type___DeleteEntityRequest = DeleteEntityRequest

class SearchEntitiesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    parent: typing___Text = ...
    page_size: builtin___int = ...
    page_token: typing___Text = ...

    @property
    def terms(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[exabel___api___data___v1___search_messages_pb2___SearchTerm]:
        ...

    def __init__(self, *, parent: typing___Optional[typing___Text]=None, terms: typing___Optional[typing___Iterable[exabel___api___data___v1___search_messages_pb2___SearchTerm]]=None, page_size: typing___Optional[builtin___int]=None, page_token: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'page_size', b'page_size', u'page_token', b'page_token', u'parent', b'parent', u'terms', b'terms']) -> None:
        ...
type___SearchEntitiesRequest = SearchEntitiesRequest

class SearchEntitiesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class SearchResult(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def terms(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[exabel___api___data___v1___search_messages_pb2___SearchTerm]:
            ...

        @property
        def entities(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[exabel___api___data___v1___entity_messages_pb2___Entity]:
            ...

        def __init__(self, *, terms: typing___Optional[typing___Iterable[exabel___api___data___v1___search_messages_pb2___SearchTerm]]=None, entities: typing___Optional[typing___Iterable[exabel___api___data___v1___entity_messages_pb2___Entity]]=None) -> None:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'entities', b'entities', u'terms', b'terms']) -> None:
            ...
    type___SearchResult = SearchResult
    next_page_token: typing___Text = ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___SearchEntitiesResponse.SearchResult]:
        ...

    @property
    def entities(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[exabel___api___data___v1___entity_messages_pb2___Entity]:
        ...

    def __init__(self, *, results: typing___Optional[typing___Iterable[type___SearchEntitiesResponse.SearchResult]]=None, next_page_token: typing___Optional[typing___Text]=None, entities: typing___Optional[typing___Iterable[exabel___api___data___v1___entity_messages_pb2___Entity]]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'entities', b'entities', u'next_page_token', b'next_page_token', u'results', b'results']) -> None:
        ...
type___SearchEntitiesResponse = SearchEntitiesResponse