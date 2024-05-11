from pydantic import BaseModel
import uuid
import datetime

class User(BaseModel, use_enum_values=True):
    id:uuid.UUID
    name:str
    phone:str
    email:str
    created_at:datetime.datetime