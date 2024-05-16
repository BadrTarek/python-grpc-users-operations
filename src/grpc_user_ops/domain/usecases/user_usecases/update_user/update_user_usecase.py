from grpc_user_ops.domain.usecases.user_usecases.update_user.update_user_usecase_request import UpdateUserUseCaseRequest
from grpc_user_ops.domain.interfaces.usecase_interface import IUseCase
from grpc_user_ops.domain.entities.user import User
from pydantic import validate_call
from grpc_user_ops.domain.errors.not_found import NotFound




class UpdateUserUseCase(IUseCase):
    
    @validate_call
    async def execute(self, usecase_request: UpdateUserUseCaseRequest) -> None:
        user = User.model_construct(**usecase_request.__dict__)
        updated_rows = await self.uow.user_repository.update(user)
        if updated_rows == 0:
            raise NotFound(f"The user with id = {usecase_request.id} you are trying to update does not exist.")







