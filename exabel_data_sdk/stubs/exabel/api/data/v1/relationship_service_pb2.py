"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....exabel.api.data.v1 import relationship_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='exabel/api/data/v1/relationship_service.proto', package='exabel.api.data.v1', syntax='proto3', serialized_options=b'\n\x16com.exabel.api.data.v1B\x18RelationshipServiceProtoP\x01Z\x16exabel.com/api/data/v1', create_key=_descriptor._internal_create_key, serialized_pb=b'\n-exabel/api/data/v1/relationship_service.proto\x12\x12exabel.api.data.v1\x1a.exabel/api/data/v1/relationship_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a.protoc_gen_openapiv2/options/annotations.proto"E\n\x1cListRelationshipTypesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"\x8e\x01\n\x1dListRelationshipTypesResponse\x12@\n\x12relationship_types\x18\x01 \x03(\x0b2$.exabel.api.data.v1.RelationshipType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"e\n\x1dCreateRelationshipTypeRequest\x12D\n\x11relationship_type\x18\x01 \x01(\x0b2$.exabel.api.data.v1.RelationshipTypeB\x03\xe0A\x02"\xad\x01\n\x1dUpdateRelationshipTypeRequest\x12D\n\x11relationship_type\x18\x01 \x01(\x0b2$.exabel.api.data.v1.RelationshipTypeB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rallow_missing\x18\x03 \x01(\x08"O\n\x1dDeleteRelationshipTypeRequest\x12.\n\x04name\x18\x01 \x01(\tB \xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName"L\n\x1aGetRelationshipTypeRequest\x12.\n\x04name\x18\x01 \x01(\tB \xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName"\x9b\x01\n\x18ListRelationshipsRequest\x120\n\x06parent\x18\x01 \x01(\tB \xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName\x12\x13\n\x0bfrom_entity\x18\x02 \x01(\t\x12\x11\n\tto_entity\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"\x81\x01\n\x19ListRelationshipsResponse\x127\n\rrelationships\x18\x01 \x03(\x0b2 .exabel.api.data.v1.Relationship\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"|\n\x16GetRelationshipRequest\x120\n\x06parent\x18\x01 \x01(\tB \xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName\x12\x18\n\x0bfrom_entity\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tto_entity\x18\x03 \x01(\tB\x03\xe0A\x02"X\n\x19CreateRelationshipRequest\x12;\n\x0crelationship\x18\x01 \x01(\x0b2 .exabel.api.data.v1.RelationshipB\x03\xe0A\x02"\xa0\x01\n\x19UpdateRelationshipRequest\x12;\n\x0crelationship\x18\x01 \x01(\x0b2 .exabel.api.data.v1.RelationshipB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rallow_missing\x18\x03 \x01(\x08"\x7f\n\x19DeleteRelationshipRequest\x120\n\x06parent\x18\x01 \x01(\tB \xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName\x12\x18\n\x0bfrom_entity\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tto_entity\x18\x03 \x01(\tB\x03\xe0A\x022\xc7\x0f\n\x13RelationshipService\x12\xb7\x01\n\x15ListRelationshipTypes\x120.exabel.api.data.v1.ListRelationshipTypesRequest\x1a1.exabel.api.data.v1.ListRelationshipTypesResponse"9\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/relationshipTypes\x92A\x19\x12\x17List relationship types\x12\xad\x01\n\x13GetRelationshipType\x12..exabel.api.data.v1.GetRelationshipTypeRequest\x1a$.exabel.api.data.v1.RelationshipType"@\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=relationshipTypes/*}\x92A\x17\x12\x15Get relationship type\x12\xc0\x01\n\x16CreateRelationshipType\x121.exabel.api.data.v1.CreateRelationshipTypeRequest\x1a$.exabel.api.data.v1.RelationshipType"M\x82\xd3\xe4\x93\x02*"\x15/v1/relationshipTypes:\x11relationship_type\x92A\x1a\x12\x18Create relationship type\x12\xdb\x01\n\x16UpdateRelationshipType\x121.exabel.api.data.v1.UpdateRelationshipTypeRequest\x1a$.exabel.api.data.v1.RelationshipType"h\x82\xd3\xe4\x93\x02E20/v1/{relationship_type.name=relationshipTypes/*}:\x11relationship_type\x92A\x1a\x12\x18Update relationship type\x12\xa8\x01\n\x16DeleteRelationshipType\x121.exabel.api.data.v1.DeleteRelationshipTypeRequest\x1a\x16.google.protobuf.Empty"C\x82\xd3\xe4\x93\x02 *\x1e/v1/{name=relationshipTypes/*}\x92A\x1a\x12\x18Delete relationship type\x12\xbf\x01\n\x11ListRelationships\x12,.exabel.api.data.v1.ListRelationshipsRequest\x1a-.exabel.api.data.v1.ListRelationshipsResponse"M\x82\xd3\xe4\x93\x020\x12./v1/{parent=relationshipTypes/*}/relationships\x92A\x14\x12\x12List relationships\x12\xe3\x01\n\x0fGetRelationship\x12*.exabel.api.data.v1.GetRelationshipRequest\x1a .exabel.api.data.v1.Relationship"\x81\x01\x82\xd3\xe4\x93\x02f\x12d/v1/{parent=relationshipTypes/*}/relationships/{from_entity=entityTypes/*}/{to_entity=entityTypes/*}\x92A\x12\x12\x10Get relationship\x12\xd0\x01\n\x12CreateRelationship\x12-.exabel.api.data.v1.CreateRelationshipRequest\x1a .exabel.api.data.v1.Relationship"i\x82\xd3\xe4\x93\x02K";/v1/{relationship.parent=relationshipTypes/*}/relationships:\x0crelationship\x92A\x15\x12\x13Create relationship\x12\xd0\x01\n\x12UpdateRelationship\x12-.exabel.api.data.v1.UpdateRelationshipRequest\x1a .exabel.api.data.v1.Relationship"i\x82\xd3\xe4\x93\x02K2;/v1/{relationship.parent=relationshipTypes/*}/relationships:\x0crelationship\x92A\x15\x12\x13Update relationship\x12\xab\x01\n\x12DeleteRelationship\x12-.exabel.api.data.v1.DeleteRelationshipRequest\x1a\x16.google.protobuf.Empty"N\x82\xd3\xe4\x93\x020*./v1/{parent=relationshipTypes/*}/relationships\x92A\x15\x12\x13Delete relationshipBL\n\x16com.exabel.api.data.v1B\x18RelationshipServiceProtoP\x01Z\x16exabel.com/api/data/v1b\x06proto3', dependencies=[exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2.DESCRIPTOR, google_dot_api_dot_annotations__pb2.DESCRIPTOR, google_dot_api_dot_field__behavior__pb2.DESCRIPTOR, google_dot_protobuf_dot_empty__pb2.DESCRIPTOR, google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR, protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR])
_LISTRELATIONSHIPTYPESREQUEST = _descriptor.Descriptor(name='ListRelationshipTypesRequest', full_name='exabel.api.data.v1.ListRelationshipTypesRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='page_size', full_name='exabel.api.data.v1.ListRelationshipTypesRequest.page_size', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='page_token', full_name='exabel.api.data.v1.ListRelationshipTypesRequest.page_token', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=291, serialized_end=360)
_LISTRELATIONSHIPTYPESRESPONSE = _descriptor.Descriptor(name='ListRelationshipTypesResponse', full_name='exabel.api.data.v1.ListRelationshipTypesResponse', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='relationship_types', full_name='exabel.api.data.v1.ListRelationshipTypesResponse.relationship_types', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='next_page_token', full_name='exabel.api.data.v1.ListRelationshipTypesResponse.next_page_token', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='total_size', full_name='exabel.api.data.v1.ListRelationshipTypesResponse.total_size', index=2, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=363, serialized_end=505)
_CREATERELATIONSHIPTYPEREQUEST = _descriptor.Descriptor(name='CreateRelationshipTypeRequest', full_name='exabel.api.data.v1.CreateRelationshipTypeRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='relationship_type', full_name='exabel.api.data.v1.CreateRelationshipTypeRequest.relationship_type', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=507, serialized_end=608)
_UPDATERELATIONSHIPTYPEREQUEST = _descriptor.Descriptor(name='UpdateRelationshipTypeRequest', full_name='exabel.api.data.v1.UpdateRelationshipTypeRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='relationship_type', full_name='exabel.api.data.v1.UpdateRelationshipTypeRequest.relationship_type', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='update_mask', full_name='exabel.api.data.v1.UpdateRelationshipTypeRequest.update_mask', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='allow_missing', full_name='exabel.api.data.v1.UpdateRelationshipTypeRequest.allow_missing', index=2, number=3, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=611, serialized_end=784)
_DELETERELATIONSHIPTYPEREQUEST = _descriptor.Descriptor(name='DeleteRelationshipTypeRequest', full_name='exabel.api.data.v1.DeleteRelationshipTypeRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='exabel.api.data.v1.DeleteRelationshipTypeRequest.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName', file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=786, serialized_end=865)
_GETRELATIONSHIPTYPEREQUEST = _descriptor.Descriptor(name='GetRelationshipTypeRequest', full_name='exabel.api.data.v1.GetRelationshipTypeRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='exabel.api.data.v1.GetRelationshipTypeRequest.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName', file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=867, serialized_end=943)
_LISTRELATIONSHIPSREQUEST = _descriptor.Descriptor(name='ListRelationshipsRequest', full_name='exabel.api.data.v1.ListRelationshipsRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='parent', full_name='exabel.api.data.v1.ListRelationshipsRequest.parent', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='from_entity', full_name='exabel.api.data.v1.ListRelationshipsRequest.from_entity', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='to_entity', full_name='exabel.api.data.v1.ListRelationshipsRequest.to_entity', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='page_size', full_name='exabel.api.data.v1.ListRelationshipsRequest.page_size', index=3, number=4, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='page_token', full_name='exabel.api.data.v1.ListRelationshipsRequest.page_token', index=4, number=5, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=946, serialized_end=1101)
_LISTRELATIONSHIPSRESPONSE = _descriptor.Descriptor(name='ListRelationshipsResponse', full_name='exabel.api.data.v1.ListRelationshipsResponse', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='relationships', full_name='exabel.api.data.v1.ListRelationshipsResponse.relationships', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='next_page_token', full_name='exabel.api.data.v1.ListRelationshipsResponse.next_page_token', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='total_size', full_name='exabel.api.data.v1.ListRelationshipsResponse.total_size', index=2, number=3, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1104, serialized_end=1233)
_GETRELATIONSHIPREQUEST = _descriptor.Descriptor(name='GetRelationshipRequest', full_name='exabel.api.data.v1.GetRelationshipRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='parent', full_name='exabel.api.data.v1.GetRelationshipRequest.parent', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='from_entity', full_name='exabel.api.data.v1.GetRelationshipRequest.from_entity', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='to_entity', full_name='exabel.api.data.v1.GetRelationshipRequest.to_entity', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1235, serialized_end=1359)
_CREATERELATIONSHIPREQUEST = _descriptor.Descriptor(name='CreateRelationshipRequest', full_name='exabel.api.data.v1.CreateRelationshipRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='relationship', full_name='exabel.api.data.v1.CreateRelationshipRequest.relationship', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1361, serialized_end=1449)
_UPDATERELATIONSHIPREQUEST = _descriptor.Descriptor(name='UpdateRelationshipRequest', full_name='exabel.api.data.v1.UpdateRelationshipRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='relationship', full_name='exabel.api.data.v1.UpdateRelationshipRequest.relationship', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='update_mask', full_name='exabel.api.data.v1.UpdateRelationshipRequest.update_mask', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='allow_missing', full_name='exabel.api.data.v1.UpdateRelationshipRequest.allow_missing', index=2, number=3, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1452, serialized_end=1612)
_DELETERELATIONSHIPREQUEST = _descriptor.Descriptor(name='DeleteRelationshipRequest', full_name='exabel.api.data.v1.DeleteRelationshipRequest', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='parent', full_name='exabel.api.data.v1.DeleteRelationshipRequest.parent', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02\x92A\x1a\xca>\x17\xfa\x02\x14relationshipTypeName', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='from_entity', full_name='exabel.api.data.v1.DeleteRelationshipRequest.from_entity', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='to_entity', full_name='exabel.api.data.v1.DeleteRelationshipRequest.to_entity', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x02', file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=1614, serialized_end=1741)
_LISTRELATIONSHIPTYPESRESPONSE.fields_by_name['relationship_types'].message_type = exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIPTYPE
_CREATERELATIONSHIPTYPEREQUEST.fields_by_name['relationship_type'].message_type = exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIPTYPE
_UPDATERELATIONSHIPTYPEREQUEST.fields_by_name['relationship_type'].message_type = exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIPTYPE
_UPDATERELATIONSHIPTYPEREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTRELATIONSHIPSRESPONSE.fields_by_name['relationships'].message_type = exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIP
_CREATERELATIONSHIPREQUEST.fields_by_name['relationship'].message_type = exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIP
_UPDATERELATIONSHIPREQUEST.fields_by_name['relationship'].message_type = exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIP
_UPDATERELATIONSHIPREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['ListRelationshipTypesRequest'] = _LISTRELATIONSHIPTYPESREQUEST
DESCRIPTOR.message_types_by_name['ListRelationshipTypesResponse'] = _LISTRELATIONSHIPTYPESRESPONSE
DESCRIPTOR.message_types_by_name['CreateRelationshipTypeRequest'] = _CREATERELATIONSHIPTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateRelationshipTypeRequest'] = _UPDATERELATIONSHIPTYPEREQUEST
DESCRIPTOR.message_types_by_name['DeleteRelationshipTypeRequest'] = _DELETERELATIONSHIPTYPEREQUEST
DESCRIPTOR.message_types_by_name['GetRelationshipTypeRequest'] = _GETRELATIONSHIPTYPEREQUEST
DESCRIPTOR.message_types_by_name['ListRelationshipsRequest'] = _LISTRELATIONSHIPSREQUEST
DESCRIPTOR.message_types_by_name['ListRelationshipsResponse'] = _LISTRELATIONSHIPSRESPONSE
DESCRIPTOR.message_types_by_name['GetRelationshipRequest'] = _GETRELATIONSHIPREQUEST
DESCRIPTOR.message_types_by_name['CreateRelationshipRequest'] = _CREATERELATIONSHIPREQUEST
DESCRIPTOR.message_types_by_name['UpdateRelationshipRequest'] = _UPDATERELATIONSHIPREQUEST
DESCRIPTOR.message_types_by_name['DeleteRelationshipRequest'] = _DELETERELATIONSHIPREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ListRelationshipTypesRequest = _reflection.GeneratedProtocolMessageType('ListRelationshipTypesRequest', (_message.Message,), {'DESCRIPTOR': _LISTRELATIONSHIPTYPESREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(ListRelationshipTypesRequest)
ListRelationshipTypesResponse = _reflection.GeneratedProtocolMessageType('ListRelationshipTypesResponse', (_message.Message,), {'DESCRIPTOR': _LISTRELATIONSHIPTYPESRESPONSE, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(ListRelationshipTypesResponse)
CreateRelationshipTypeRequest = _reflection.GeneratedProtocolMessageType('CreateRelationshipTypeRequest', (_message.Message,), {'DESCRIPTOR': _CREATERELATIONSHIPTYPEREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(CreateRelationshipTypeRequest)
UpdateRelationshipTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateRelationshipTypeRequest', (_message.Message,), {'DESCRIPTOR': _UPDATERELATIONSHIPTYPEREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(UpdateRelationshipTypeRequest)
DeleteRelationshipTypeRequest = _reflection.GeneratedProtocolMessageType('DeleteRelationshipTypeRequest', (_message.Message,), {'DESCRIPTOR': _DELETERELATIONSHIPTYPEREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(DeleteRelationshipTypeRequest)
GetRelationshipTypeRequest = _reflection.GeneratedProtocolMessageType('GetRelationshipTypeRequest', (_message.Message,), {'DESCRIPTOR': _GETRELATIONSHIPTYPEREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(GetRelationshipTypeRequest)
ListRelationshipsRequest = _reflection.GeneratedProtocolMessageType('ListRelationshipsRequest', (_message.Message,), {'DESCRIPTOR': _LISTRELATIONSHIPSREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(ListRelationshipsRequest)
ListRelationshipsResponse = _reflection.GeneratedProtocolMessageType('ListRelationshipsResponse', (_message.Message,), {'DESCRIPTOR': _LISTRELATIONSHIPSRESPONSE, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(ListRelationshipsResponse)
GetRelationshipRequest = _reflection.GeneratedProtocolMessageType('GetRelationshipRequest', (_message.Message,), {'DESCRIPTOR': _GETRELATIONSHIPREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(GetRelationshipRequest)
CreateRelationshipRequest = _reflection.GeneratedProtocolMessageType('CreateRelationshipRequest', (_message.Message,), {'DESCRIPTOR': _CREATERELATIONSHIPREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(CreateRelationshipRequest)
UpdateRelationshipRequest = _reflection.GeneratedProtocolMessageType('UpdateRelationshipRequest', (_message.Message,), {'DESCRIPTOR': _UPDATERELATIONSHIPREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(UpdateRelationshipRequest)
DeleteRelationshipRequest = _reflection.GeneratedProtocolMessageType('DeleteRelationshipRequest', (_message.Message,), {'DESCRIPTOR': _DELETERELATIONSHIPREQUEST, '__module__': 'exabel.api.data.v1.relationship_service_pb2'})
_sym_db.RegisterMessage(DeleteRelationshipRequest)
DESCRIPTOR._options = None
_CREATERELATIONSHIPTYPEREQUEST.fields_by_name['relationship_type']._options = None
_UPDATERELATIONSHIPTYPEREQUEST.fields_by_name['relationship_type']._options = None
_DELETERELATIONSHIPTYPEREQUEST.fields_by_name['name']._options = None
_GETRELATIONSHIPTYPEREQUEST.fields_by_name['name']._options = None
_LISTRELATIONSHIPSREQUEST.fields_by_name['parent']._options = None
_GETRELATIONSHIPREQUEST.fields_by_name['parent']._options = None
_GETRELATIONSHIPREQUEST.fields_by_name['from_entity']._options = None
_GETRELATIONSHIPREQUEST.fields_by_name['to_entity']._options = None
_CREATERELATIONSHIPREQUEST.fields_by_name['relationship']._options = None
_UPDATERELATIONSHIPREQUEST.fields_by_name['relationship']._options = None
_DELETERELATIONSHIPREQUEST.fields_by_name['parent']._options = None
_DELETERELATIONSHIPREQUEST.fields_by_name['from_entity']._options = None
_DELETERELATIONSHIPREQUEST.fields_by_name['to_entity']._options = None
_RELATIONSHIPSERVICE = _descriptor.ServiceDescriptor(name='RelationshipService', full_name='exabel.api.data.v1.RelationshipService', file=DESCRIPTOR, index=0, serialized_options=None, create_key=_descriptor._internal_create_key, serialized_start=1744, serialized_end=3735, methods=[_descriptor.MethodDescriptor(name='ListRelationshipTypes', full_name='exabel.api.data.v1.RelationshipService.ListRelationshipTypes', index=0, containing_service=None, input_type=_LISTRELATIONSHIPTYPESREQUEST, output_type=_LISTRELATIONSHIPTYPESRESPONSE, serialized_options=b'\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/relationshipTypes\x92A\x19\x12\x17List relationship types', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='GetRelationshipType', full_name='exabel.api.data.v1.RelationshipService.GetRelationshipType', index=1, containing_service=None, input_type=_GETRELATIONSHIPTYPEREQUEST, output_type=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIPTYPE, serialized_options=b'\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=relationshipTypes/*}\x92A\x17\x12\x15Get relationship type', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='CreateRelationshipType', full_name='exabel.api.data.v1.RelationshipService.CreateRelationshipType', index=2, containing_service=None, input_type=_CREATERELATIONSHIPTYPEREQUEST, output_type=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIPTYPE, serialized_options=b'\x82\xd3\xe4\x93\x02*"\x15/v1/relationshipTypes:\x11relationship_type\x92A\x1a\x12\x18Create relationship type', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='UpdateRelationshipType', full_name='exabel.api.data.v1.RelationshipService.UpdateRelationshipType', index=3, containing_service=None, input_type=_UPDATERELATIONSHIPTYPEREQUEST, output_type=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIPTYPE, serialized_options=b'\x82\xd3\xe4\x93\x02E20/v1/{relationship_type.name=relationshipTypes/*}:\x11relationship_type\x92A\x1a\x12\x18Update relationship type', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='DeleteRelationshipType', full_name='exabel.api.data.v1.RelationshipService.DeleteRelationshipType', index=4, containing_service=None, input_type=_DELETERELATIONSHIPTYPEREQUEST, output_type=google_dot_protobuf_dot_empty__pb2._EMPTY, serialized_options=b'\x82\xd3\xe4\x93\x02 *\x1e/v1/{name=relationshipTypes/*}\x92A\x1a\x12\x18Delete relationship type', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='ListRelationships', full_name='exabel.api.data.v1.RelationshipService.ListRelationships', index=5, containing_service=None, input_type=_LISTRELATIONSHIPSREQUEST, output_type=_LISTRELATIONSHIPSRESPONSE, serialized_options=b'\x82\xd3\xe4\x93\x020\x12./v1/{parent=relationshipTypes/*}/relationships\x92A\x14\x12\x12List relationships', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='GetRelationship', full_name='exabel.api.data.v1.RelationshipService.GetRelationship', index=6, containing_service=None, input_type=_GETRELATIONSHIPREQUEST, output_type=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIP, serialized_options=b'\x82\xd3\xe4\x93\x02f\x12d/v1/{parent=relationshipTypes/*}/relationships/{from_entity=entityTypes/*}/{to_entity=entityTypes/*}\x92A\x12\x12\x10Get relationship', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='CreateRelationship', full_name='exabel.api.data.v1.RelationshipService.CreateRelationship', index=7, containing_service=None, input_type=_CREATERELATIONSHIPREQUEST, output_type=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIP, serialized_options=b'\x82\xd3\xe4\x93\x02K";/v1/{relationship.parent=relationshipTypes/*}/relationships:\x0crelationship\x92A\x15\x12\x13Create relationship', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='UpdateRelationship', full_name='exabel.api.data.v1.RelationshipService.UpdateRelationship', index=8, containing_service=None, input_type=_UPDATERELATIONSHIPREQUEST, output_type=exabel_dot_api_dot_data_dot_v1_dot_relationship__messages__pb2._RELATIONSHIP, serialized_options=b'\x82\xd3\xe4\x93\x02K2;/v1/{relationship.parent=relationshipTypes/*}/relationships:\x0crelationship\x92A\x15\x12\x13Update relationship', create_key=_descriptor._internal_create_key), _descriptor.MethodDescriptor(name='DeleteRelationship', full_name='exabel.api.data.v1.RelationshipService.DeleteRelationship', index=9, containing_service=None, input_type=_DELETERELATIONSHIPREQUEST, output_type=google_dot_protobuf_dot_empty__pb2._EMPTY, serialized_options=b'\x82\xd3\xe4\x93\x020*./v1/{parent=relationshipTypes/*}/relationships\x92A\x15\x12\x13Delete relationship', create_key=_descriptor._internal_create_key)])
_sym_db.RegisterServiceDescriptor(_RELATIONSHIPSERVICE)
DESCRIPTOR.services_by_name['RelationshipService'] = _RELATIONSHIPSERVICE