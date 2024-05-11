from grpc_user_ops.domain.usecases.user_usecases.delete_user.delete_user_usecase_request import DeleteUserUseCaseRequest
from grpc_user_ops.domain.interfaces.usecase_interface import IUseCase
from grpc_user_ops.domain.entities.user import User
from pydantic import validate_call




class DeleteUserUseCase(IUseCase):
    
    @validate_call
    async def execute(self, usecase_request: DeleteUserUseCaseRequest) -> None:
        await self.uow.user_repository.delete(usecase_request.id)







