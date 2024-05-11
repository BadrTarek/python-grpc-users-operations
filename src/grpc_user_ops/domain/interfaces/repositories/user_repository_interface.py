from abc import ABC, abstractmethod
from typing import List
import uuid
from grpc_user_ops.domain.entities.user import User



class IUserRepository(ABC):
    
    @abstractmethod
    async def create(self, user:User,auto_refresh_and_flush = True) -> User:
        raise NotImplementedError
    
    
    @abstractmethod
    async def get(self, user_id:uuid.UUID) -> User:
        raise NotImplementedError
    
    
    @abstractmethod
    async def update(self,user:User) -> None:       
        raise NotImplementedError
    
    
    @abstractmethod
    async def delete(self, user_id:uuid.UUID) -> None:      
        raise NotImplementedError
    