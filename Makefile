run:
	py run_grpc_server.py

unit-test: 
	pytest -s tests/unit_tests/

integration-test: 
	pytest -s tests/integration_tests/

migrations:
	alembic revision --autogenerate -m "$(migration_name)"

migrate: 
	alembic upgrade head

generate-protos:
	python -m grpc_tools.protoc -I src/grpc_user_ops/data/ --python_out=. --grpc_python_out=. src/grpc_user_ops/data/protobufs/user_ops_api.proto src/grpc_user_ops/data/protobufs/protobufs_models/user.proto 