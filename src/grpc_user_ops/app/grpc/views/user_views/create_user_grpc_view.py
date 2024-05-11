from grpc_user_ops.domain.interfaces.grpc_view_interface import IgRPCView
from grpc_user_ops.app.services.user_services.create_user_service import CreateUserService
from google.protobuf.json_format import MessageToDict
from grpc_user_ops.protos_models.user_pb2 import (
    User
)
from grpc_user_ops.app.grpc.mapper import map_user_entity_to_user_protos


class CreateUserGrpcView(IgRPCView):
    
    def dispatch(self, request:User)-> User :
        service = CreateUserService(self.uow)
        response:dict = self.event_loop.run_until_complete(service.process( MessageToDict(request) ))
        return map_user_entity_to_user_protos(response)
