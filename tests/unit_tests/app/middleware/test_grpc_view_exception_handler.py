from unittest.mock import MagicMock
from grpc_user_ops.app.middleware.grpc_view_exception_handler import map_exceptions_to_grpc_abort
from grpc_user_ops.domain.interfaces.logger_interface import ILoggerInterface
import grpc
from pydantic import  BaseModel



def test_map_exceptions_to_grpc_abort():
    grpc_servicer = MagicMock()
    grpc_servicer.logger = MagicMock(ILoggerInterface)
    grpc_context = MagicMock(grpc.ServicerContext)
    grpc_context.abort = MagicMock()
    grpc_request = None

    class TestModel(BaseModel):
        name: str
    
    @map_exceptions_to_grpc_abort
    def test_pydantic_raised_validation_error(*args, **kwargs):
        TestModel( name = {
            "Invalid name"
        })
    
    
    test_pydantic_raised_validation_error(grpc_servicer, grpc_request,grpc_context)
    grpc_context.abort.assert_called_once()