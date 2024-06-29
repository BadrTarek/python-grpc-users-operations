from concurrent import futures
import grpc
from grpc_user_ops.app.grpc.grpc_servicer import GRPCUserOPSServicer
from protobufs.user_ops_api_pb2_grpc import add_UserOpsApiServicer_to_server
from grpc_user_ops.config import data_settings


def generate_grpc_test_server() -> grpc.Server:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=data_settings.MAX_WORKERS))
        
    add_UserOpsApiServicer_to_server(GRPCUserOPSServicer(), server)

    server.add_insecure_port(f"[::]:{str(data_settings.GRPC_SERVER_PORT)}")
    
    return server 







