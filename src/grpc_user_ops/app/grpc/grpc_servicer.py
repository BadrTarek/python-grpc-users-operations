from grpc_user_ops.app.grpc.views.user_views.create_user_grpc_view import CreateUserGrpcView
from grpc_user_ops.app.grpc.views.user_views.get_user_grpc_view import GetUserGrpcView
from grpc_user_ops.app.grpc.views.user_views.delete_user_grpc_view import DeleteUserGrpcView
from grpc_user_ops.app.grpc.views.user_views.update_user_grpc_view import UpdateUserGrpcView
from grpc_user_ops.data.database.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from protobufs.protobufs_models.user_pb2 import (
    User
)
from protobufs.user_ops_api_pb2  import (
    GetUserRequest,
    DeleteUserRequest,
    Empty
)
from protobufs.user_ops_api_pb2_grpc import UserOpsApiServicer
from grpc_user_ops.data.logger.default_logger import DefaultLogger
import grpc
from grpc_user_ops.app.middleware.grpc_view_exception_handler import exceptions_handler_middleware


@exceptions_handler_middleware
class GRPCUserOPSServicer(UserOpsApiServicer):
    logger = DefaultLogger()
    uow = SqlAlchemyUnitOfWork(logger)
    
    def CreateUser(self, request: User, context:grpc.ServicerContext, *args, **kwargs) -> User:
        grpc_view = CreateUserGrpcView(uow=self.uow)
        response = grpc_view.dispatch(request) 
        return response
    
    
    def GetUser(self, request: GetUserRequest, context:grpc.ServicerContext, *args, **kwargs) -> User:
        grpc_view = GetUserGrpcView(uow=self.uow)
        response = grpc_view.dispatch(request) 
        return response

    
    def DeleteUser(self, request: DeleteUserRequest, context:grpc.ServicerContext, *args, **kwargs) -> Empty:
        grpc_view = DeleteUserGrpcView(uow=self.uow)
        response = grpc_view.dispatch(request) 
        return response

    
    def UpdateUser(self, request: User, context:grpc.ServicerContext, *args, **kwargs) -> Empty:
        grpc_view = UpdateUserGrpcView(uow=self.uow)
        response = grpc_view.dispatch(request) 
        return response