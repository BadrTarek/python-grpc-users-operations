install:
	pip install -r requirements.txt
	pip install -e src/ 

start:
	python src/run_grpc_server.py

install-test: install
	pip install -r requirements-test.txt

unit-test: install-test
	pytest -s tests/unit_tests/

integration-test: install-test
	pytest -s tests/integration_tests/

test: install
	$(MAKE) unit-test
	$(MAKE) integration-test

migrations:
	alembic -c .\src\grpc_user_ops\config\alembic.ini revision --autogenerate -m "$(migration_name)"

migrate: 
	alembic -c .\src\grpc_user_ops\config\alembic.ini upgrade head

generate-protos:
	python -m grpc_tools.protoc -I src/grpc_user_ops/data/ --python_out=src/ --grpc_python_out=src/ src/grpc_user_ops/data/protobufs/user_ops_api.proto src/grpc_user_ops/data/protobufs/protobufs_models/user.proto 