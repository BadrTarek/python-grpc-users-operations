from concurrent import futures
import grpc
from grpc_user_ops.app.grpc.grpc_servicer import GRPCUserOPSServicer
from grpc_user_ops.data.database.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from grpc_user_ops.user_ops_api_pb2_grpc import add_UserOpsApiServicer_to_server, UserOpsApiStub
from grpc_user_ops.config import data_settings
import unittest
from grpc_user_ops.protos_models.user_pb2 import (
    User
)
from grpc_user_ops.data.logger.default_logger import DefaultLogger
import pytest


class RPCGreeterServerTest(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=data_settings.MAX_WORKERS))
        
        add_UserOpsApiServicer_to_server(GRPCUserOPSServicer(), self.server)

        self.server.add_insecure_port(f"[::]:{str(data_settings.GRPC_SERVER_PORT)}")
        
        self.server.start()
        
        self.logger = DefaultLogger()
        
        self.uow = SqlAlchemyUnitOfWork(self.logger) 


    def tearDown(self):
        self.server.stop(None)

    @pytest.mark.asyncio
    async def test_success_create_user(self):
        created_user_protos = None
        
        with grpc.insecure_channel(f'localhost:{data_settings.GRPC_SERVER_PORT}') as channel:
            stub = UserOpsApiStub(channel)
            created_user_protos = stub.CreateUser(User(
                name='Jack',
                email = "test@mail.com",
                phone = "+2011111111"
            ))
            self.assertIsNotNone(created_user_protos)
        
        
        created_user_entity = None
        
        async with self.uow:
            created_user_entity = await self.uow.user_repository.get(created_user_protos.id)
        
        self.assertEqual(str(created_user_entity.id), created_user_protos.id)
        self.assertEqual(created_user_entity.name, created_user_protos.name)
        self.assertEqual(created_user_entity.email, created_user_protos.email)