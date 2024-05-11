from abc import ABC, abstractmethod
from typing import Optional
from grpc_user_ops.domain.interfaces.unit_of_work_interface import IUnitOfWork



class IService(ABC):
    
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow
    
    @abstractmethod
    async def process(self,request:Optional[dict]) -> Optional[dict] :
        raise NotImplementedError