from unittest.mock import MagicMock,AsyncMock
from grpc_user_ops.domain.entities.user import User
from datetime import datetime
import uuid
from grpc_user_ops.domain.interfaces.unit_of_work_interface import IUnitOfWork
from grpc_user_ops.domain.interfaces.repositories.user_repository_interface import IUserRepository
from grpc_user_ops.domain.interfaces.logger_interface import ILoggerInterface
from sqlalchemy import Result


def generate_mock_user_entity() -> MagicMock:
    mock_user = MagicMock(User)
    mock_user.id = uuid.uuid4()
    mock_user.name = "Test name"
    mock_user.email = "test.mail@testmail.com"
    mock_user.phone = "+201111111111"
    mock_user.created_at = datetime.now()
    mock_user.model_dump.return_value = {
        "id": mock_user.id,
        "name":mock_user.name,
        "email": mock_user.email,
        "phone": mock_user.phone,
        "created_at":mock_user.created_at
    } 
    return mock_user


def generate_mock_user_repository(mocked_user) -> AsyncMock:
    user_repository = AsyncMock( IUserRepository ) 
    user_repository.create.return_value = mocked_user 
    user_repository.get.return_value = mocked_user 
    user_repository.update.return_value = None 
    user_repository.delete.return_value = None 
    return user_repository


def generate_mock_logger() -> AsyncMock:
    logger = MagicMock( ILoggerInterface ) 
    logger.info.return_value = None 
    logger.debug.return_value = None 
    logger.error.return_value = None 
    logger.critical.return_value = None 
    logger.warning.return_value = None 
    return logger


def generate_mock_unit_of_work(mocked_user_repository:MagicMock) -> AsyncMock:
    mock_uow = AsyncMock(IUnitOfWork)
    mock_uow.logger = generate_mock_logger()
    mock_uow.start_database_connection.return_value = None
    mock_uow.user_repository = mocked_user_repository
    mock_uow.commit.return_value = None
    mock_uow.add.return_value = None
    mock_uow.flush_and_refresh.return_value = None
    mock_uow.execute.return_value = MagicMock(Result)
    mock_uow.__aenter__.return_value = None
    mock_uow.__aexit__.return_value = None
    return mock_uow

