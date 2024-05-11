from grpc_user_ops.domain.usecases.user_usecases.update_user.update_user_usecase_request import UpdateUserUseCaseRequest
from grpc_user_ops.domain.interfaces.usecase_interface import IUseCase
from grpc_user_ops.domain.entities.user import User
from pydantic import validate_call




class UpdateUserUseCase(IUseCase):
    
    @validate_call
    async def execute(self, usecase_request: UpdateUserUseCaseRequest) -> None:
        user = User.model_construct(**usecase_request.__dict__)
        user = await self.uow.user_repository.update(user)







