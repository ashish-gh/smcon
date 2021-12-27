from abc import ABC, abstractmethod

class BaseClass(metaclass=ABC):
    """
    A base class from which we derive all the classes.    
    """
    @abstractmethod
    def connect(self):
        raise NotImplementedError

    