import pytest
import sqlalchemy
from grpc_user_ops.data.database.models import Base
from sqlalchemy.orm.session import close_all_sessions
import psycopg2
from grpc_user_ops.config.data_settings import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
)


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

    try:
        # Execute SQL command to create a new database for testing
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        yield conn
    except:
        yield conn
    finally:
        try:
            # Drop Deactivating sessions in  testing database 
            cursor.execute(
                f"""SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE datname = '{DB_NAME}'
                AND pid <> pg_backend_pid();
                """
            )
            # Drop testing database 
            cursor.execute(fr"DROP DATABASE IF EXISTS {DB_NAME}")
        except Exception as e:
            print(f"Error dropping database: {e}")



@pytest.fixture(scope='function', autouse=True)
def handle_test_database_tables_per_test_case():
    
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
    Base.metadata.create_all(engine)
    
    yield engine
    
    # drop tables after each testcase
    Base.metadata.drop_all(engine)
    close_all_sessions()