from concurrent import futures
import grpc
from grpc_user_ops.app.grpc.grpc_servicer import GRPCUserOPSServicer
from grpc_user_ops.user_ops_api_pb2_grpc import add_UserOpsApiServicer_to_server
from grpc_user_ops import user_ops_api_pb2
from grpc_reflection.v1alpha import reflection
from grpc_user_ops.config import data_settings


def serve():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=data_settings.MAX_WORKERS))
    
    add_UserOpsApiServicer_to_server(GRPCUserOPSServicer(), server)

    if data_settings.SERVE_INSECURE:
        server.add_insecure_port(f"[::]:{str(data_settings.GRPC_SERVER_PORT)}")
    else:
        server_credentials= grpc.ssl_server_credentials()
        server.add_secure_port(f"[::]:{str(data_settings.GRPC_SERVER_PORT)}", server_credentials)

    # Use server reflection
    SERVICE_NAMES = (
        user_ops_api_pb2.DESCRIPTOR.services_by_name["UserOpsApi"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    
    server.start()
    
    print(f"\ngRPC Server started on port: { data_settings.GRPC_SERVER_PORT } ........",)

    server.wait_for_termination()

if __name__ == "__main__":
    serve()
