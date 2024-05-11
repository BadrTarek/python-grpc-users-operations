import logging
import sys
from grpc_user_ops.domain.interfaces.logger_interface import ILoggerInterface



class DefaultLogger(ILoggerInterface):

    def __init__(self) -> None:     
        # Create and configure logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        # Create file handler and set level to debug
        file_handler = logging.FileHandler('grpc-user-ops.log')
        file_handler.setLevel(logging.DEBUG)

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