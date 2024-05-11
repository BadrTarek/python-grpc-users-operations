from pydantic import BaseModel
import uuid





class GetUserUseCaseRequest(BaseModel):
    id:uuid.UUID