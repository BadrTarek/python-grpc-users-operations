from grpc_user_ops.domain.usecases.user_usecases.update_user.update_user_usecase import UpdateUserUseCase
from grpc_user_ops.domain.usecases.user_usecases.update_user.update_user_usecase_request import UpdateUserUseCaseRequest
from typing import Optional
from grpc_user_ops.domain.interfaces.service_interface import IService



class UpdateUserService(IService):

    async def process(self,request:Optional[dict]) -> Optional[dict] :
        async with self.uow:
            usecase = UpdateUserUseCase(self.uow)
            await usecase.execute(UpdateUserUseCaseRequest(**request))
            await self.uow.commit()
        return None



