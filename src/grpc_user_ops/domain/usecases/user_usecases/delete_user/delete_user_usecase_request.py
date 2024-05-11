from pydantic import BaseModel
import uuid





class DeleteUserUseCaseRequest(BaseModel):
    id:uuid.UUID