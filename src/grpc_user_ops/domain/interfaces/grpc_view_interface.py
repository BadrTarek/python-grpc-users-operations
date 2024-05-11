from abc import ABC, abstractmethod
from typing import Any
from grpc_user_ops.domain.interfaces.unit_of_work_interface import IUnitOfWork
import asyncio


class IgRPCView(ABC):
    
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow
        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)
    
    @abstractmethod
    def dispatch(self,request:Any) -> Any :
        raise NotImplementedError