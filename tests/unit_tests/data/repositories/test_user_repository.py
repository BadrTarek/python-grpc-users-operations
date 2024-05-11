import pytest
from grpc_user_ops.domain.entities.user import User
from grpc_user_ops.data.repositories.user_repository import UserRepository
import uuid
import unittest
from tests.unit_tests.tests_helper import (
    generate_mock_unit_of_work,
)


class TestUserRepository(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self) -> None:
        self.mock_uow = generate_mock_unit_of_work(None)
        self.user_repository  = UserRepository(uow=self.mock_uow)
    
    
    @pytest.mark.asyncio
    async def test_create(self):
        await self.user_repository.create(User.model_construct(
            phone = "+2011111111",
            email = "test@mail.com",
            name = "Test Name"
        ))
        self.mock_uow.add.assert_called_once()
        self.mock_uow.flush_and_refresh.assert_called_once()


    @pytest.mark.asyncio
    async def test_update(self):
        await self.user_repository.update(User.model_construct(
            id = uuid.uuid4(),
            phone = "+2011111111",
            email = "test@mail.com",
            name = "Test Name"
        ))
        self.mock_uow.execute.assert_called_once()


    @pytest.mark.asyncio
    async def test_delete(self):
        await self.user_repository.delete(uuid.uuid4())
        self.mock_uow.execute.assert_called_once()


    @pytest.mark.asyncio
    async def test_get(self):
        await self.user_repository.get(uuid.uuid4())
        self.mock_uow.execute.assert_called_once()





