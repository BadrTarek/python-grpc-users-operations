from pydantic import ValidationError
import grpc
from grpc_user_ops.domain.interfaces.logger_interface import ILoggerInterface
from grpc_user_ops.domain.errors.not_found import NotFound

def map_exceptions_to_grpc_abort(func):
    def wrapper(*args, **kwargs):
        logger:ILoggerInterface = args[0].logger
        try:
            return func(*args, **kwargs)
        except ValidationError as exc:            
            logger.error(f"ValidationError: {str(exc)}")
            context:grpc.ServicerContext = args[2]
            context.abort(grpc.StatusCode.INVALID_ARGUMENT,str(exc))
        except NotFound as exc:            
            logger.error(f"NotFoundError: {str(exc)}")
            context:grpc.ServicerContext = args[2]
            context.abort(grpc.StatusCode.NOT_FOUND,str(exc))
        except Exception as exc:            
            logger.error(f"UnhandledError: {str(exc)}")
            context:grpc.ServicerContext = args[2]
            context.abort(grpc.StatusCode.INTERNAL)
    
    return wrapper


# Decorator to wrap all methods of a class
def exceptions_handler_middleware(cls):
    for name, method in vars(cls).items():
        if callable(method):
            setattr(cls, name, map_exceptions_to_grpc_abort(method))
    return cls

