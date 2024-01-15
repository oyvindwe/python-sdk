"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Exabel AS. All rights reserved."""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RunTaskRequest(google.protobuf.message.Message):
    """The request run task."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'The resource name of the task to run, for example `tasks/123`.'

    def __init__(self, *, name: builtins.str | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___RunTaskRequest = RunTaskRequest

@typing_extensions.final
class RunTaskResponse(google.protobuf.message.Message):
    """The response to run task."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___RunTaskResponse = RunTaskResponse