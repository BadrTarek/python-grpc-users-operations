from grpc_user_ops.domain.errors.not_found import NotFound
from grpc_user_ops.domain.usecases.user_usecases.delete_user.delete_user_usecase_request import DeleteUserUseCaseRequest
from grpc_user_ops.domain.interfaces.usecase_interface import IUseCase
from pydantic import validate_call




class DeleteUserUseCase(IUseCase):
    
    @validate_call
    async def execute(self, usecase_request: DeleteUserUseCaseRequest) -> None:
        deleted_rows = await self.uow.user_repository.delete(usecase_request.id)
        if deleted_rows == 0:
            raise NotFound(f"The user with id = {usecase_request.id} you are trying to delete does not exist.")






