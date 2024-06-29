import unittest
from unittest.mock import patch
from grpc_user_ops.data.logger.default_logger import DefaultLogger



class TestDefaultLogger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = DefaultLogger()
    
    def test_info(self):
        message = "This is an info message"
        with patch('logging.Logger.info') as mock_info:
            self.logger.info(message)
            mock_info.assert_called_once_with(message)

    def test_debug(self):
        message = "This is a debug message"
        with patch('logging.Logger.debug') as mock_debug:
            self.logger.debug(message)
            mock_debug.assert_called_once_with(message)

    def test_warning(self):
        message = "This is a warning message"
        with patch('logging.Logger.warning') as mock_warning:
            self.logger.warning(message)
            mock_warning.assert_called_once_with(message)

    def test_error(self):
        message = "This is an error message"
        with patch('logging.Logger.error') as mock_error:
            self.logger.error(message)
            mock_error.assert_called_once_with(message)

    def test_critical(self):
        message = "This is a critical message"
        with patch('logging.Logger.critical') as mock_critical:
            self.logger.critical(message)
            mock_critical.assert_called_once_with(message)