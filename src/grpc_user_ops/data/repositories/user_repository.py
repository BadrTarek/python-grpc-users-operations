from grpc_user_ops.domain.entities.user import User
from grpc_user_ops.domain.interfaces.repositories.user_repository_interface import IUserRepository
from grpc_user_ops.data.database.models import UserDal
from grpc_user_ops.domain.interfaces.unit_of_work_interface import IUnitOfWork
from sqlalchemy import select, update,delete
from typing import List
import uuid
from sqlalchemy import Result

class UserRepository(IUserRepository):
    
    def __init__(self, uow:IUnitOfWork) -> None:
        self.uow = uow
        super().__init__()
    
    
    async def create(self, user:User, auto_refresh_and_flush = True) -> User:
        user_dal =  UserDal(**user.__dict__)
        self.uow.add(user_dal)
        if auto_refresh_and_flush:
            await self.uow.flush_and_refresh( user_dal )
        user =  User.model_construct(**user_dal.__dict__)
        return user


    async def list(self) -> List[User]:
        stmt = select(UserDal).order_by(UserDal.created_at)
        result:Result = await self.uow.execute(stmt)
        return [User(**user_dal.__dict__) for user_dal in result.scalars().all()]
    
    
    async def get(self, user_id:uuid.UUID) -> User:
        stmt = select(UserDal).filter_by(id = user_id)
        result:Result = await self.uow.execute(stmt)
        return User(**result.scalars().one().__dict__)
    
    
    async def update(self,user:User) -> None:        
        query = update(UserDal).where(UserDal.id ==user.id).values(
            name = user.name,   
            phone = user.phone,
            email = user.email
        )
        await self.uow.execute(query)
    
    
    async def delete(self, user_id:uuid.UUID) -> None:        
        query = delete(UserDal).where(UserDal.id ==user_id)
        await self.uow.execute(query)