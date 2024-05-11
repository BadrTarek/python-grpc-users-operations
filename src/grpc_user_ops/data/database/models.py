import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from grpc_user_ops.data.database.mixin import Mixin
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs



class Base(AsyncAttrs,DeclarativeBase):
    """ Async Base class for all models
    """
    pass


class UserDal(Base,Mixin):
    
    __tablename__ = "userops_users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,index=True,unique=True,default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(80), nullable=False )
    phone: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False)



















