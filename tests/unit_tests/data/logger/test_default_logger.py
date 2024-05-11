import unittest
from unittest.mock import patch
from grpc_user_ops.data.logger.default_logger import DefaultLogger

class TestDefaultLogger(unittest.TestCase):

    
    def test_info(self):
        logger = DefaultLogger()
        message = "This is an info message"
        with patch('logging.Logger.info') as mock_info:
            logger.info(message)
            mock_info.assert_called_once_with(message)

    def test_debug(self):
        logger = DefaultLogger()
        message = "This is a debug message"
        with patch('logging.Logger.debug') as mock_debug:
            logger.debug(message)
            mock_debug.assert_called_once_with(message)

    def test_warning(self):
        logger = DefaultLogger()
        message = "This is a warning message"
        with patch('logging.Logger.warning') as mock_warning:
            logger.warning(message)
            mock_warning.assert_called_once_with(message)

    def test_error(self):
        logger = DefaultLogger()
        message = "This is an error message"
        with patch('logging.Logger.error') as mock_error:
            logger.error(message)
            mock_error.assert_called_once_with(message)

    def test_critical(self):
        logger = DefaultLogger()
        message = "This is a critical message"
        with patch('logging.Logger.critical') as mock_critical:
            logger.critical(message)
            mock_critical.assert_called_once_with(message)