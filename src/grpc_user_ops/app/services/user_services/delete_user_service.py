from grpc_user_ops.domain.usecases.user_usecases.delete_user.delete_user_usecase import DeleteUserUseCase
from grpc_user_ops.domain.usecases.user_usecases.delete_user.delete_user_usecase_request import DeleteUserUseCaseRequest
from typing import Optional
from grpc_user_ops.domain.interfaces.service_interface import IService



class DeleteUserService(IService):

    async def process(self,request:Optional[dict]) -> Optional[dict] :
        async with self.uow:
            usecase = DeleteUserUseCase(self.uow)
            await usecase.execute(DeleteUserUseCaseRequest(**request))
            await self.uow.commit()
        return None



