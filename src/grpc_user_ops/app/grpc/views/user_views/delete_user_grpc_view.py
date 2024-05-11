from grpc_user_ops.domain.interfaces.grpc_view_interface import IgRPCView
from grpc_user_ops.app.services.user_services.delete_user_service import DeleteUserService
from google.protobuf.json_format import MessageToDict
from grpc_user_ops.user_ops_api_pb2 import Empty, DeleteUserRequest


class DeleteUserGrpcView(IgRPCView):
    
    def dispatch(self, request:DeleteUserRequest)-> Empty :
        service = DeleteUserService(self.uow)
        self.event_loop.run_until_complete(service.process( MessageToDict(request) ))
        return Empty()
