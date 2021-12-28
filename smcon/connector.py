from abc import ABCMeta, abstractmethod


class BaseConnector(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        """
        A base function to connect to the client. Not authenticate but to connect to client
        """
        raise NotImplementedError
