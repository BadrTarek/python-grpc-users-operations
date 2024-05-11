from unittest import IsolatedAsyncioTestCase
from grpc_user_ops.domain.usecases.user_usecases.create_user.create_user_usecase_request import CreateUserUseCaseRequest
from grpc_user_ops.domain.usecases.user_usecases.create_user.create_user_usecase import CreateUserUseCase
from grpc_user_ops.domain.usecases.user_usecases.create_user.create_user_usecase_response import CreateUserUseCaseResponse
from unittest.mock import MagicMock
from pydantic import ValidationError
import pytest
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)


class TestCreateUserUseCase(IsolatedAsyncioTestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_user = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)
    
    
    @pytest.mark.asyncio
    async def test_success_create_user_usecase(self):
        
        usecase_request = CreateUserUseCaseRequest(
            name="Test",
            email="test.mail@testmail.com",
            phone="+201111111111"
        )
        usecase = CreateUserUseCase( self.mock_uow )
        response = await usecase.execute(usecase_request)

        self.assertIsInstance( response,  CreateUserUseCaseResponse)
        self.assertEqual(response.user.id, self.mock_user.id)


    def test_failed_create_user_usecase_request(self):
        with self.assertRaises(ValidationError):
            CreateUserUseCaseRequest(
                name="Test",
                email="invalid_email",
                phone="invalid_phone_number"
            )

        with self.assertRaises(ValidationError):
            CreateUserUseCaseRequest()
    
    
    @pytest.mark.asyncio
    async def test_failed_create_user_usecase(self):
        
        with self.assertRaises(ValidationError):
            usecase_request = MagicMock(
                name="Test",
                email="test.mail@testmail.com",
                phone="+201111111111"
            )
            
            usecase = CreateUserUseCase( self.mock_uow )
            await usecase.execute(usecase_request)