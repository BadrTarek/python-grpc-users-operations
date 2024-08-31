import grpc
from grpc_user_ops.data.database.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from protobufs.user_ops_api_pb2_grpc import  UserOpsApiStub
from grpc_user_ops.config import data_settings
import unittest
from protobufs.user_ops_api_pb2 import (
    DeleteUserRequest,
    Empty
)
from grpc_user_ops.data.logger.default_logger import DefaultLogger
import pytest
from grpc_user_ops.domain.entities.user import User as UserEntity


class RPCDeleteUserTest(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self):
        self.logger = DefaultLogger()
        self.uow = SqlAlchemyUnitOfWork(self.logger)

    @pytest.mark.asyncio
    async def test_success_delete_user(self):
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
        
        deleted_user_protos = DeleteUserRequest(
            id = str(created_user_in_db.id),
        )
        
        with grpc.insecure_channel(f'localhost:{data_settings.GRPC_SERVER_PORT}') as channel:
            stub = UserOpsApiStub(channel)
            
            response = stub.DeleteUser(
                DeleteUserRequest(
                    id = str(created_user_in_db.id),
                )
            )
            
            self.assertIsInstance(response,Empty)
        
        
        
        async with self.uow:
            deleted_user_entity = await self.uow.user_repository.get(deleted_user_protos.id)
            self.assertIsNone(deleted_user_entity)