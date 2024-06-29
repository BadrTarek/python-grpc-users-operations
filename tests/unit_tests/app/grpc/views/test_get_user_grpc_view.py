import unittest
from unittest.mock import AsyncMock
from grpc_user_ops.app.grpc.views.user_views.get_user_grpc_view import GetUserGrpcView
from protobufs.protobufs_models.user_pb2 import User
from tests.unit_tests.tests_helper import (
    generate_mock_user_entity,
    generate_mock_unit_of_work,
    generate_mock_user_repository
)
from unittest import mock


class TestGetUserGrpcView(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        cls.mock_user_entity = generate_mock_user_entity()
        cls.mock_user_repository = generate_mock_user_repository(cls.mock_user_entity)
        cls.mock_uow = generate_mock_unit_of_work(cls.mock_user_repository)
        cls.view = GetUserGrpcView(cls.mock_uow)
        
    
    @mock.patch("grpc_user_ops.app.grpc.views.user_views.get_user_grpc_view.GetUserService.process",new_callable=AsyncMock)
    def test_dispatch_get_user_grpc_view(self, mock_service_process):
        
        mock_service_process.return_value = self.mock_user_entity.model_dump()
        
        user_protos_request = User( 
            id = str(self.mock_user_entity.id),
        )
        
        response = self.view.dispatch(user_protos_request)
        
        self.assertEqual(response.id, str(self.mock_user_entity.id))
        self.assertEqual(response.name, self.mock_user_entity.name)
        self.assertEqual(response.email, self.mock_user_entity.email)
        self.assertEqual(response.phone, self.mock_user_entity.phone)
