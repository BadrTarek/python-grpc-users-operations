from grpc_user_ops.domain.interfaces.logger_interface import ILoggerInterface
from grpc_user_ops.domain.interfaces.unit_of_work_interface import IUnitOfWork
import sqlalchemy
from grpc_user_ops.config.data_settings import (
        DB_NAME,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_USER,
        DB_DRIVER
) 
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
import asyncio 
from sqlalchemy import Result

# Repositories
from grpc_user_ops.data.repositories.user_repository import UserRepository





class SqlAlchemyUnitOfWork(IUnitOfWork):
    
    def __init__(self,logger:ILoggerInterface) -> None:
        self.logger:ILoggerInterface = logger 
        super().__init__()
    
    
    async def start_database_connection(self):
        
        self.logger.info('Starting database connection')
        
        self.async_engine = create_async_engine(
            sqlalchemy.engine.url.URL.create(
                drivername = DB_DRIVER ,
                username=DB_USER,
                password= DB_PASSWORD,
                database= DB_NAME, 
                port = DB_PORT,
                host  = DB_HOST
            ),
            pool_size = 5
        )
        
        self.__async_session = async_sessionmaker(
            bind = self.async_engine,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False
        )


    async def __aenter__(self):
        await self.start_database_connection()
        self.construct_repositories()
        async with self.__async_session.begin() as session:
            self.db_session = session


    def construct_repositories(self):
        self.user_repository = UserRepository(self)
    
    
    def add(self, instance:object):
        self.db_session.add(instance)


    async def commit(self):
        await self.db_session.commit()

    
    async def rollback(self):
        await self.db_session.rollback()


    async def flush_and_refresh(self, instance:object):        
        await self.db_session.flush()
        await self.db_session.refresh(instance)
    
    
    async def execute(self, stmt:object) -> Result:
        return await self.db_session.execute(stmt)
    
    async def __aexit__(self, *args):
        self.logger.info('Closing database connection')
        await asyncio.shield(self.db_session.close_all())
        await asyncio.shield(self.async_engine.dispose())
