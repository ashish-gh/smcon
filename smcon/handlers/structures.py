from __future__ import __annotations__
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class AbstractHandlers(metaclass=ABCMeta):
    @property
    def __classname__(self):
        return self.__class__.__name__

    @abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplementedError
    
    def __str__(self):
        return f"{self.__class__.__name__} || {self.__dict__}"
    
    def __repr__(self) -> str:
        return str(self)
    

@dataclass
class LoginResponseDTO:
    message: str = ""
    status_code: int = 200 
    data: dict = {}
    meatadata: dict = {}