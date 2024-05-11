from grpc_user_ops.domain.interfaces.unit_of_work_interface import IUnitOfWork
from grpc_user_ops.domain.usecases.user_usecases.create_user.create_user_usecase import CreateUserUseCase
from grpc_user_ops.domain.usecases.user_usecases.create_user.create_user_usecase_request import CreateUserUseCaseRequest
from grpc_user_ops.domain.interfaces.logger_interface import ILoggerInterface
from typing import Optional
from grpc_user_ops.domain.interfaces.service_interface import IService



class CreateUserService(IService):

    async def process(self,request:Optional[dict]) -> Optional[dict] :
        response = None
        async with self.uow:
            usecase = CreateUserUseCase(self.uow)
            response = await usecase.execute(CreateUserUseCaseRequest(**request))
            await self.uow.commit()
        return response.user.model_dump()



