from unittest import IsolatedAsyncioTestCase
from grpc_user_ops.domain.interfaces.repositories.user_repository_interface import IUserRepository
from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase import GetUserUseCase
from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase_request import GetUserUseCaseRequest
from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase_response import GetUserUseCaseResponse
from unittest.mock import AsyncMock, MagicMock
from pydantic import ValidationError
import pytest
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)
from grpc_user_ops.domain.errors.not_found import NotFound



class TestGetUserUseCase(IsolatedAsyncioTestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_user = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)
    
    
    
    @pytest.mark.asyncio
    async def test_success_get_user_usecase(self):
        usecase_request = GetUserUseCaseRequest(
            id = self.mock_user.id
        )
        
        usecase = GetUserUseCase( self.mock_uow )
        response = await usecase.execute(usecase_request)

        self.assertIsInstance( response,  GetUserUseCaseResponse)
        self.assertEqual(response.user.id, self.mock_user.id)


    @pytest.mark.asyncio
    async def test_invalid_get_user_usecase_request(self):
        with self.assertRaises(ValidationError):
            GetUserUseCaseRequest(
                id = "invalid_uuid"
            )

        with self.assertRaises(ValidationError):
            GetUserUseCaseRequest()
    
        with self.assertRaises(ValidationError):
            usecase_request = MagicMock(
                id= self.mock_user.id,
            )
            
            usecase = GetUserUseCase( self.mock_uow )
            await usecase.execute(usecase_request)

    
    @pytest.mark.asyncio
    async def test_failed_to_get_user_usecase(self):
        
        user_repository = AsyncMock( IUserRepository ) 
        user_repository.get.return_value = None 
        
        mock_uow = generate_mock_unit_of_work(user_repository)
        
        with self.assertRaises(NotFound):
            usecase_request = GetUserUseCaseRequest(
                id= self.mock_user.id,
            )
            
            usecase = GetUserUseCase( mock_uow )
            await usecase.execute(usecase_request)