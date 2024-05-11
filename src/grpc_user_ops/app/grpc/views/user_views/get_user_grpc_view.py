from grpc_user_ops.domain.interfaces.grpc_view_interface import IgRPCView
from grpc_user_ops.app.services.user_services.get_user_service import GetUserService
from google.protobuf.json_format import MessageToDict
from grpc_user_ops.protos_models.user_pb2 import (
    User
)
from google.protobuf.json_format import ParseDict
from google.protobuf.timestamp_pb2 import Timestamp
from grpc_user_ops.app.grpc.mapper import map_user_entity_to_user_protos
from grpc_user_ops.user_ops_api_pb2 import GetUserRequest

class GetUserGrpcView(IgRPCView):
    
    def dispatch(self, request:GetUserRequest)-> User :
        service = GetUserService(self.uow)
        response:dict = self.event_loop.run_until_complete(service.process( MessageToDict(request) ))
        return map_user_entity_to_user_protos(response)
