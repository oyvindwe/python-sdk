"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import Descriptor as google___protobuf___descriptor___Descriptor, FileDescriptor as google___protobuf___descriptor___FileDescriptor
from google.protobuf.message import Message as google___protobuf___message___Message
from typing import Optional as typing___Optional, Text as typing___Text
from typing_extensions import Literal as typing_extensions___Literal
builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class SearchTerm(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    field: typing___Text = ...
    query: typing___Text = ...

    def __init__(self, *, field: typing___Optional[typing___Text]=None, query: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'field', b'field', u'query', b'query']) -> None:
        ...
type___SearchTerm = SearchTerm