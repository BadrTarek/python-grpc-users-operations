run:
	py .\src\grpc_user_ops\run_grpc_server.py

unit-test: 
	coverage run -m pytest -s .\tests\unit_tests\

migrations:
	alembic revision --autogenerate -m "$(migration_name)"

migrate: 
	alembic upgrade head

generate-protos:
	python -m grpc_tools.protoc -I src/grpc_user_ops/data/protos/ --python_out=src/grpc_user_ops/ --grpc_python_out=src/grpc_user_ops/ src/grpc_user_ops/data/protos/user_ops_api.proto src/grpc_user_ops/data/protos/protos_models/user.proto 