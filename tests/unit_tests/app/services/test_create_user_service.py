from unittest import IsolatedAsyncioTestCase
from grpc_user_ops.app.services.user_services.create_user_service import CreateUserService
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)
import pytest


class TestCreateUserService(IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_user = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)

    @pytest.mark.asyncio
    async def test_process_create_success(self):
        mock_request = {
            "name":self.mock_user.name,
            "email":self.mock_user.email,
            "phone":self.mock_user.phone
        }
        service = CreateUserService(self.mock_uow)
        response = await service.process(mock_request)
        self.assertEqual(response["id"], self.mock_user.id)
        self.assertEqual(response["name"], self.mock_user.name)
        self.assertEqual(response["phone"], self.mock_user.phone)
        self.assertEqual(response["email"], self.mock_user.email)