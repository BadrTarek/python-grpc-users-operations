import unittest
from unittest.mock import AsyncMock
from grpc_user_ops.app.grpc.views.user_views.delete_user_grpc_view import DeleteUserGrpcView
from protobufs.user_ops_api_pb2 import Empty, DeleteUserRequest
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)
from unittest import mock


class TestDeleteUserGrpcView(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        cls.mock_user_entity = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user_entity)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)
        cls.view = DeleteUserGrpcView(cls.mock_uow)
        
    
    @mock.patch("grpc_user_ops.app.grpc.views.user_views.delete_user_grpc_view.DeleteUserService.process",new_callable=AsyncMock)
    def test_dispatch_delete_user_grpc_view(self, mock_service_process):
        
        mock_service_process.return_value = None
        
        user_protos_request = DeleteUserRequest( 
            id = str(self.mock_user_entity.id),
        )
        
        response = self.view.dispatch(user_protos_request)
        
        self.assertIsInstance(response, Empty)
