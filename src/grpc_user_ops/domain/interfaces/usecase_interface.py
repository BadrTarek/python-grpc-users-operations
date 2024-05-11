from abc import ABC, abstractmethod
from grpc_user_ops.domain.interfaces.unit_of_work_interface import IUnitOfWork


class IUseCase(ABC):
    
    def __init__(self,uow:IUnitOfWork) -> None:
        self.uow = uow
    
    
    @abstractmethod
    async def execute(self):
        raise NotImplementedError