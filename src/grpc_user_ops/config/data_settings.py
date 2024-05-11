import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv(".env",raise_error_if_not_found=False))


# Database Configuration
DB_DRIVER = os.environ.get("DB_DRIVER","postgresql+asyncpg")
DB_HOST = os.environ.get("DB_HOST","localhost")
DB_PORT = os.environ.get("DB_PORT","5432")
DB_NAME = os.environ.get("DB_NAME","grpc-user-ops-db")
DB_USER = os.environ.get("DB_USER","postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD","")


# gRPC Server Configuration
MAX_WORKERS = int(os.environ.get("MAX_WORKERS","10"))
GRPC_SERVER_PORT = int(os.environ.get("GRPC_SERVER_PORT","50051"))
SERVE_INSECURE = bool(os.environ.get("SERVE_INSECURE", "1"))

