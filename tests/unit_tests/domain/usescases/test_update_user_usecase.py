from unittest import IsolatedAsyncioTestCase
from grpc_user_ops.domain.usecases.user_usecases.update_user.update_user_usecase_request import UpdateUserUseCaseRequest
from grpc_user_ops.domain.usecases.user_usecases.update_user.update_user_usecase import UpdateUserUseCase
from unittest.mock import MagicMock
from pydantic import ValidationError
import pytest
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)


class TestUpdateUserUseCase(IsolatedAsyncioTestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_user = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)
    
    
    @pytest.mark.asyncio
    async def test_success_update_user_usecase(self):
        
        usecase_request = UpdateUserUseCaseRequest(
            id = self.mock_user.id,
            name="Test",
            email="test.mail@testmail.com",
            phone="+201111111111"
        )
        usecase = UpdateUserUseCase( self.mock_uow )
        response = await usecase.execute(usecase_request)

        self.assertIsNone( response )


    def test_failed_update_user_usecase_request(self):
        with self.assertRaises(ValidationError):
            UpdateUserUseCaseRequest(
                id = self.mock_user.id,
                name="Test",
                email="invalid_email",
                phone="invalid_phone_number"
            )

        with self.assertRaises(ValidationError):
            UpdateUserUseCaseRequest()
    
    
    @pytest.mark.asyncio
    async def test_failed_update_user_usecase(self):
        
        with self.assertRaises(ValidationError):
            usecase_request = MagicMock(
                id = self.mock_user.id,
                name="Test",
                email="test.mail@testmail.com",
                phone="+201111111111"
            )
            
            usecase = UpdateUserUseCase( self.mock_uow )
            await usecase.execute(usecase_request)