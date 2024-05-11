from abc import ABC, abstractmethod



class ILoggerInterface(ABC):
    
    @abstractmethod
    def info(self,message):
        raise NotImplementedError

    @abstractmethod
    def debug(self,message):
        raise NotImplementedError
    
    @abstractmethod
    def warning(self,message):
        raise NotImplementedError

    @abstractmethod
    def error(self,message):
        raise NotImplementedError
    
    @abstractmethod
    def critical(self,message):
        raise NotImplementedError