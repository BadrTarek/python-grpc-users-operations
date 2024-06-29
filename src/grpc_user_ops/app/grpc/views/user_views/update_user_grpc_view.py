from grpc_user_ops.domain.interfaces.grpc_view_interface import IgRPCView
from grpc_user_ops.app.services.user_services.update_user_service import UpdateUserService
from google.protobuf.json_format import MessageToDict
from protobufs.protobufs_models.user_pb2 import (
    User
)
from grpc_user_ops.app.grpc.mapper import map_user_entity_to_user_protos
from protobufs.user_ops_api_pb2  import Empty


class UpdateUserGrpcView(IgRPCView):
    
    def dispatch(self, request:User)-> Empty :
        service = UpdateUserService(self.uow)
        self.event_loop.run_until_complete(service.process( MessageToDict(request) ))
        return Empty()
