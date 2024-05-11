from typing import Union, Any, Dict



class AbstractException(Exception):

    def __init__(
        self,
        message: Union[str , list , dict],
        **kwargs,
    ):
        self.messages = [message] if isinstance(message, (str, bytes)) else message
        self.kwargs = kwargs
        super().__init__(message)


    @property
    def messages_dict(self) -> Dict[str,Any]:
        if not isinstance(self.messages, dict):
            return {
                "errors": self.messages,
            }

        return self.messages