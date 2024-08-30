from sqlalchemy import DateTime,Column
import datetime


class Mixin:
    created_at = Column(DateTime, nullable=False,default=datetime.datetime.now() )
    updated_at = Column(DateTime, nullable=True )