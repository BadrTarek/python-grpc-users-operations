import logging
import sys
from grpc_user_ops.domain.interfaces.logger_interface import ILoggerInterface
from grpc_user_ops.config.data_settings import LOGGING_FILE, LOGGING_LEVEL


class DefaultLogger(ILoggerInterface):

    def __init__(self) -> None:     
        # Create and configure logger
        self.logger = logging.getLogger()
        self.logger.setLevel(LOGGING_LEVEL)

        # Create console handler and set level to debug
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(LOGGING_LEVEL)

        # Create file handler and set level to debug
        file_handler = logging.FileHandler(LOGGING_FILE)
        file_handler.setLevel(LOGGING_LEVEL)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add formatter to handlers
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)


    def info(self,message):
        self.logger.info(message)


    def debug(self,message):
        self.logger.debug(message)
    

    def warning(self,message):
        self.logger.warning(message)


    def error(self,message):
        self.logger.error(message)


    def critical(self,message):
        self.logger.critical(message)