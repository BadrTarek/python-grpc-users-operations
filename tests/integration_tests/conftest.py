import pytest
import sqlalchemy
from grpc_user_ops.data.database import models 
from sqlalchemy.orm.session import close_all_sessions
import psycopg2
from grpc_user_ops.config.data_settings import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
)

from concurrent import futures
import grpc
from grpc_user_ops.app.grpc.grpc_servicer import GRPCUserOPSServicer
from protobufs.user_ops_api_pb2_grpc import add_UserOpsApiServicer_to_server
from grpc_user_ops.config import data_settings



@pytest.fixture(scope='session', autouse=True)
def handle_test_database_per_session():
    # Connect to the default 'postgres' database to create a new database for testing
    conn = psycopg2.connect(
        dbname='postgres',
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Create gRPC server for testing
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=data_settings.MAX_WORKERS))
    add_UserOpsApiServicer_to_server(GRPCUserOPSServicer(), server)
    server.add_insecure_port(f"[::]:{str(data_settings.GRPC_SERVER_PORT)}")
    
    # Execute SQL command to create a new database for testing
    cursor.execute(f"CREATE DATABASE {DB_NAME}")
    
    # Start gRPC server
    server.start()
    
    yield conn, server
    
    # Stop gRPC server
    server.stop(grace=None)
    
    # Terminate all connections to the testing database
    cursor.execute(
        f"""SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE datname = '{DB_NAME}'
        AND pid <> pg_backend_pid();
        """
    )
    
    # Drop testing database 
    cursor.execute(fr"DROP DATABASE IF EXISTS {DB_NAME}")


@pytest.fixture(scope='function', autouse=True)
def handle_test_database_tables_per_test_case():
    # Connect to the testing database
    engine = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername = "postgresql+psycopg2",
            username= DB_USER,
            password= DB_PASSWORD,
            database= DB_NAME, 
            port = DB_PORT,
            host  = DB_HOST
        )
    )
    
    # create tables before each testcase
    models.load_all_models()
    models.base.AsyncBase.metadata.create_all(engine)
    
    yield engine
    
    # drop tables after each testcase
    models.base.AsyncBase.metadata.drop_all(engine)
    close_all_sessions()

