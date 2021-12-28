from __future__ import annotations
from abc import abstractmethod
from typing import Dict

from .errors import ClientLoginError
from ..connector import BaseConnector
from ..structures import User, ClientUrl

from loguru import logger



class Client(User):
    
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
       
    def get_client_url(self, client: str) -> str:
        if isinstance(client, str):
            client = client.lower()
            if client in ["insta", "instagaram"]:
                client_url = ClientUrl.INSTA_URL
            elif client in ["spotify"]:
                client_url = ClientUrl.SPOTIFY
            else:
                raise ValueError(f"Expected type to be ['instagram', 'spotify']. Got type {str(type(client))}")
        return client_url
                
    @abstractmethod
    def connect(self):
        raise NotImplementedError
    
    def call_api(
        self,
        params: Dict = None,
        query: Dict = None,
        version: str = "v1"        
        ) -> Dict:
        """
        Calls client api
        Args:
        Returns:        
        """
        raise NotImplementedError
    
    def format_response(self, 
        response: Dict
    ) -> Dict:
        raise NotImplementedError




class InstaClient(Client, BaseConnector):
    """
    All operations to insta are derived from this base class.
    """
    
    def __init__(self, username: str, password: str= "", **kwargs) -> None:
        self.username = username
        self.password = password    
        # logging to insta client
        self.login()
    
    def login(self):
        """
        Login to insta client        
        """
        if not (self.username and self.password):
            # raise ClientLoginError()
            raise ClientLoginError(message="login required", code=400)        
        response = self.call_api()
        logger.debug(f"Response : {str(response)}")
        # CLIENTS_URL = self.get_client_url(self)    



    def call_api(self, 
        params: Dict = None, 
        query: Dict = None, 
        version: str = "v1"
        ) -> Dict:
        
        logger.info(f"Connecting to {self.__class__.__name__}")
        response = {
            "username": self.username,
            "password": self.password
            }
        return self.format_response(response)

    def format_response(self, response: Dict) -> Dict:
        return response
    

    def make_connection(self) -> None:
        logger.info(f"Making secure connecting using ssh/apikey or others")

    def connect(self, username: str, password: str) -> None:
        """
        Connect to instagram using username and password.
        Args:
            `username`:
            `password`:
        """
        if not isinstance(username, str):
            raise ValueError(
                f"Expected value of username to be str. Got {type(username)}"
            )

        if not isinstance(password, str):
            raise ValueError(
                f"Expected value of password to be str. Got {type(password)}"
            )
        try:
            self.make_connection()
        except:
            logger.error(f"Exception in making connection . . . .")
        logger.debug(
            f"Connecting to instagram using username : {username} and password :{password}"
        )

    def __classname__(self) -> InstaClient:
        return self.__class__.__name__


def main():
    pass


if __name__ == "__main__":
    main()
