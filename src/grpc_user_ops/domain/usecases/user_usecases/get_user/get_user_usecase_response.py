from pydantic import BaseModel
from grpc_user_ops.domain.entities.user import User



class GetUserUseCaseResponse(BaseModel):
    user:User