from __future__ import annotations

from abc import abstractmethod
from typing import Dict
from loguru import logger

from ..structures import ParamsFactory, UrlFactory, User


class Client(User):
    """
    Property
        - CLIENT
        - url
        - login_params
        - login_url
        - classname
    
    Methods
        - connect : @abstactmethod
        - call_api: @abstractmethod
        - format_response: @abstractmethod
    """
    
    CLIENT = ""

    @property
    def url(self) -> str:
        return self.url

    @url.setter
    def url(self, url: str) -> None:
        if not isinstance(url, str):
            raise ValueError(f"Expected url to be str. Got type : {str(type(url))}")
        self.url = url

    @abstractmethod
    def login(self):
        raise NotImplementedError

    @property
    def login_params(self, client: str = "") -> dict:        
        if not client:
            client = self.CLIENT
        return ParamsFactory.get_params(client=client)

    @property
    def login_url(self, client: str ="") -> str:
        if not client:
            client = self.CLIENT
        return UrlFactory.get_url(client=client)

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def call_api(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def format_response(self, response: Dict) -> Dict:
        raise NotImplementedError
    
    @property
    def classname(self) -> str:
        return str(self.__class__.__name__)



def main():
    pass


if __name__ == "__main__":
    main()
