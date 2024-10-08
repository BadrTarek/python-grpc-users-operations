from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase_request import GetUserUseCaseRequest
from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase_response import GetUserUseCaseResponse
from grpc_user_ops.domain.interfaces.usecase_interface import IUseCase
from pydantic import validate_call
from grpc_user_ops.domain.errors.not_found import NotFound




class GetUserUseCase(IUseCase):
    
    @validate_call
    async def execute(self, usecase_request: GetUserUseCaseRequest) -> GetUserUseCaseResponse:
        user = await self.uow.user_repository.get(usecase_request.id)
        if user is None:
            raise NotFound(f"Undefined user with id = {str(usecase_request.id)}")
        return GetUserUseCaseResponse(user=user)







