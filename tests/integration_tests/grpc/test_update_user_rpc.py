import grpc
from grpc_user_ops.data.database.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from protobufs.user_ops_api_pb2_grpc import  UserOpsApiStub
from grpc_user_ops.config import data_settings
import unittest
from protobufs.protobufs_models.user_pb2 import (
    User
)
from grpc_user_ops.data.logger.default_logger import DefaultLogger
import pytest
from grpc_user_ops.domain.entities.user import User as UserEntity
from protobufs.user_ops_api_pb2 import Empty


class RPCUpdateUserTest(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self):
        self.logger = DefaultLogger()
        self.uow = SqlAlchemyUnitOfWork(self.logger)


    @pytest.mark.asyncio
    async def test_success_update_user(self):
        created_user_in_db = None
        
        async with self.uow:
            created_user_in_db = await self.uow.user_repository.create(
                UserEntity.model_construct(
                    name = "Test",
                    email = "test@mail.com",
                    phone = "+2011111111"
                )
            )
            await self.uow.commit()
        
        updated_user_protos = User(
            id = str(created_user_in_db.id),
            name='Updated Test',
            email = "test-update@mail.com",
            phone = "+2011111111"
        )
        
        with grpc.insecure_channel(f'localhost:{data_settings.GRPC_SERVER_PORT}') as channel:
            stub = UserOpsApiStub(channel)
            
            response = stub.UpdateUser(
                User(
                    id = str(created_user_in_db.id),
                    name='Updated Test',
                    email = "test-update@mail.com",
                    phone = "+2011111111"
                )
            )
            
            self.assertIsInstance(response,Empty)
        
        
        
        async with self.uow:
            updated_user_entity = await self.uow.user_repository.get(updated_user_protos.id)
        
            self.assertEqual(str(updated_user_entity.id), updated_user_protos.id)
            self.assertEqual(updated_user_entity.name, updated_user_protos.name)
            self.assertEqual(updated_user_entity.email, updated_user_protos.email)