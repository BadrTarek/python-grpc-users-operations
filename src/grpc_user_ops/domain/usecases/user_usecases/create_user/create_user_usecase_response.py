from pydantic import BaseModel
from grpc_user_ops.domain.entities.user import User



class CreateUserUseCaseResponse(BaseModel):
    user:User