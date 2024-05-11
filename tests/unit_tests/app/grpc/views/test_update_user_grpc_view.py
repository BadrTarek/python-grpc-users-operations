import unittest
from unittest.mock import AsyncMock
from grpc_user_ops.app.grpc.views.user_views.update_user_grpc_view import UpdateUserGrpcView
from grpc_user_ops.user_ops_api_pb2 import Empty
from grpc_user_ops.protos_models.user_pb2 import (
    User
)
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)
from unittest import mock


class TestUpdateUserGrpcView(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        cls.mock_user_entity = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user_entity)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)
        cls.view = UpdateUserGrpcView(cls.mock_uow)
        
    
    @mock.patch("grpc_user_ops.app.grpc.views.user_views.update_user_grpc_view.UpdateUserService.process",new_callable=AsyncMock)
    def test_dispatch_update_user_grpc_view(self, mock_service_process):
        
        mock_service_process.return_value = None
        
        user_protos_request = User( 
            id = str(self.mock_user_entity.id),
            name=self.mock_user_entity.name,
            email=self.mock_user_entity.email,
            phone=self.mock_user_entity.phone
        )
        
        response = self.view.dispatch(user_protos_request)
        
        self.assertIsInstance(response, Empty)
