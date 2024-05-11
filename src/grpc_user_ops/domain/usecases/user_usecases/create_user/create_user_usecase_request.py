from pydantic import BaseModel,field_validator,ValidationError
import uuid
from grpc_user_ops.domain.utils import mail_regex,phone_number_regex
import re




class CreateUserUseCaseRequest(BaseModel, use_enum_values=True):
    name:str
    phone:str
    email:str
    
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, email: str) -> str:
        
        if(re.fullmatch(mail_regex, email)):
            return email
    
        raise ValueError("Invalid mail")
    
    
    @field_validator('phone')
    @classmethod
    def validate_phone(cls, phone: int) -> int:
        
        if(re.fullmatch(phone_number_regex, phone)):
            return phone

        raise ValueError("Invalid phone")