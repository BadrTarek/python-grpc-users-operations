from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase import GetUserUseCase
from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase_request import GetUserUseCaseRequest
from grpc_user_ops.domain.usecases.user_usecases.get_user.get_user_usecase_response import GetUserUseCaseResponse
from typing import Optional
from grpc_user_ops.domain.interfaces.service_interface import IService



class GetUserService(IService):

    async def process(self,request:Optional[dict]) -> Optional[dict] :
        response = None
        async with self.uow:
            usecase = GetUserUseCase(self.uow)
            response:GetUserUseCaseResponse = await usecase.execute(GetUserUseCaseRequest(**request))
            await self.uow.commit()
        return response.user.model_dump()



