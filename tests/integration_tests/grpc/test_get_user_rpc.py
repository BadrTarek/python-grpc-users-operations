import grpc
from grpc_user_ops.data.database.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from protobufs.user_ops_api_pb2_grpc import UserOpsApiStub
from grpc_user_ops.config import data_settings
import unittest
from protobufs.protobufs_models.user_pb2 import (
    User
)
from grpc_user_ops.data.logger.default_logger import DefaultLogger
import pytest
from tests.integration_tests.test_helper import generate_grpc_test_server   
from grpc_user_ops.domain.entities.user import User as UserEntity
from protobufs.user_ops_api_pb2  import GetUserRequest


class RPCGetUserTest(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self):
        self.server = generate_grpc_test_server()
        
        self.logger = DefaultLogger()
        
        self.uow = SqlAlchemyUnitOfWork(self.logger)
        
        self.server.start()


    def tearDown(self):
        self.server.stop(None)

    @pytest.mark.asyncio
    async def test_success_get_user(self):
        created_user_in_db:UserEntity = None
        
        async with self.uow:
            created_user_in_db = await self.uow.user_repository.create(
                UserEntity.model_construct(
                    name = "Test",
                    email = "test@mail.com",
                    phone = "+2011111111"
                )
            )
            await self.uow.commit()
            
        
        with grpc.insecure_channel(f'localhost:{data_settings.GRPC_SERVER_PORT}') as channel:
            stub = UserOpsApiStub(channel)
            user:User = stub.GetUser(GetUserRequest(
                id= str(created_user_in_db.id)
            ))
            self.assertEqual(user.id, str(created_user_in_db.id))
            self.assertEqual(user.name, created_user_in_db.name)
            self.assertEqual(user.email, created_user_in_db.email)
            self.assertEqual(user.phone, created_user_in_db.phone)
