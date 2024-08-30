from importlib import import_module

__all__ = {
    "AsyncBase": "grpc_user_ops.data.database.models.base",
    "Mixin": "grpc_user_ops.data.database.models.mixin",
    "UserDal": "grpc_user_ops.data.database.models.user_dal"
}


def load_all_models():
    
    for class_name, module_path in __all__.items():
        module = import_module(module_path)        
        globals()[class_name] = getattr(module, class_name)

