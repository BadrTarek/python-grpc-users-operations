install:
	pip install -r requirements.txt
	pip install -e src/ 

run:
	py src/run_grpc_server.py

unit-test: 
	pytest -s tests/unit_tests/

integration-test: 
	pytest -s tests/integration_tests/

test: install
	pip install -r requirements-test.txt
	$(MAKE) unit-test
	$(MAKE) integration-test

migrations:
	alembic -c .\src\grpc_user_ops\config\alembic.ini revision --autogenerate -m "$(migration_name)"

migrate: 
	alembic -c .\src\grpc_user_ops\config\alembic.ini upgrade head

generate-protos:
	python -m grpc_tools.protoc -I src/grpc_user_ops/data/ --python_out=src/ --grpc_python_out=src/ src/grpc_user_ops/data/protobufs/user_ops_api.proto src/grpc_user_ops/data/protobufs/protobufs_models/user.proto 