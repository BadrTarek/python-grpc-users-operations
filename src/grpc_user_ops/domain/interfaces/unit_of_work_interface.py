from abc import ABC, abstractmethod
from sqlalchemy.orm import  Session
from typing_extensions import Self, Any


# Repositories
from grpc_user_ops.domain.interfaces.repositories.user_repository_interface import IUserRepository



class IUnitOfWork(ABC):
    
    db_session:Session    
    
    # Repositories
    user_repository:IUserRepository


    async def __aenter__(self) -> Self:
        raise NotImplementedError


    async def __aexit__(self, *args) -> Self:
        raise NotImplementedError


    @abstractmethod
    async def start_database_connection(self):
        raise NotImplementedError


    @abstractmethod
    def add(self,instance:object):
        raise NotImplementedError


    @abstractmethod
    async def commit(self):
        raise NotImplementedError


    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


    @abstractmethod
    async def flush_and_refresh(self, instance:object):
        raise NotImplementedError


    @abstractmethod
    async def execute(self, stmt:object) -> Any:
        raise NotImplementedError