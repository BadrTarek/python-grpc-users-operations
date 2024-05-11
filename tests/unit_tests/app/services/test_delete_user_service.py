from unittest import IsolatedAsyncioTestCase
from grpc_user_ops.app.services.user_services.delete_user_service import DeleteUserService
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)
import pytest


class TestDeleteUserService(IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_user = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)

    @pytest.mark.asyncio
    async def test_process_delete_success(self):
        mock_request = {
            "id":self.mock_user.id,
        }
        service = DeleteUserService(self.mock_uow)
        response = await service.process(mock_request)
        self.assertIsNone(response)