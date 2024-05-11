from grpc_user_ops.domain.usecases.user_usecases.create_user.create_user_usecase_request import CreateUserUseCaseRequest
from grpc_user_ops.domain.usecases.user_usecases.create_user.create_user_usecase_response import CreateUserUseCaseResponse
from grpc_user_ops.domain.interfaces.usecase_interface import IUseCase
from grpc_user_ops.domain.entities.user import User
from pydantic import validate_call




class CreateUserUseCase(IUseCase):
    
    @validate_call
    async def execute(self, usecase_request: CreateUserUseCaseRequest) -> CreateUserUseCaseResponse:
        user = User.model_construct(**usecase_request.__dict__)
        user = await self.uow.user_repository.create(user)
        return CreateUserUseCaseResponse(user=user)







