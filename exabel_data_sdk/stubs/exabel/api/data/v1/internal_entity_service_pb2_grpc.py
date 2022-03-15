"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .....exabel.api.data.v1 import entity_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2
from .....exabel.api.data.v1 import internal_entity_service_pb2 as exabel_dot_api_dot_data_dot_v1_dot_internal__entity__service__pb2

class InternalEntityServiceStub(object):
    """Manages entity types in the Data API, for internal usage.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEntityType = channel.unary_unary('/exabel.api.data.v1.InternalEntityService/CreateEntityType', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_internal__entity__service__pb2.CreateEntityTypeRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.EntityType.FromString)
        self.UpdateEntityType = channel.unary_unary('/exabel.api.data.v1.InternalEntityService/UpdateEntityType', request_serializer=exabel_dot_api_dot_data_dot_v1_dot_internal__entity__service__pb2.UpdateEntityTypeRequest.SerializeToString, response_deserializer=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.EntityType.FromString)

class InternalEntityServiceServicer(object):
    """Manages entity types in the Data API, for internal usage.
    """

    def CreateEntityType(self, request, context):
        """Creates one entity type and returns it. (Exabel internal.)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEntityType(self, request, context):
        """Updates one entity type and returns it.
        (Exabel internal.)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_InternalEntityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateEntityType': grpc.unary_unary_rpc_method_handler(servicer.CreateEntityType, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_internal__entity__service__pb2.CreateEntityTypeRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.EntityType.SerializeToString), 'UpdateEntityType': grpc.unary_unary_rpc_method_handler(servicer.UpdateEntityType, request_deserializer=exabel_dot_api_dot_data_dot_v1_dot_internal__entity__service__pb2.UpdateEntityTypeRequest.FromString, response_serializer=exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.EntityType.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('exabel.api.data.v1.InternalEntityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class InternalEntityService(object):
    """Manages entity types in the Data API, for internal usage.
    """

    @staticmethod
    def CreateEntityType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.InternalEntityService/CreateEntityType', exabel_dot_api_dot_data_dot_v1_dot_internal__entity__service__pb2.CreateEntityTypeRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.EntityType.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEntityType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exabel.api.data.v1.InternalEntityService/UpdateEntityType', exabel_dot_api_dot_data_dot_v1_dot_internal__entity__service__pb2.UpdateEntityTypeRequest.SerializeToString, exabel_dot_api_dot_data_dot_v1_dot_entity__messages__pb2.EntityType.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)