from __future__ import annotations
import time
import typing
import requests
from abc import abstractmethod
from typing import Dict

from .errors import ClientLoginError
from ..connector import BaseConnector
from ..structures import User, ClientUrl, LoginUrl, LoginParams

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
    
    @property
    def login_url(self, client: str = "") -> str:
        """
        For each client get its login url        
        """                
        if not isinstance(client, str):
            raise ValueError(f"Expected type to be `str`. Got type {str(type(client))}")
        client = client.lower()
        if client in ["insta", "instagaram"]:
            client_url = LoginUrl.INSTA_URL
        elif client in ["spotify"]:
            client_url = LoginUrl.SPOTIFY
        else:
            raise ValueError(f"Expected type to be ['instagram', 'spotify']. Got type {str(type(client))}")
        return client_url
    

    def get_login_prarams(self):
        return LoginParams(self)
       
    @property
    def login_params(self, client: str ="") -> dict:
        return self.get_login_prarams()
        # This is not efficient way to do things

        # if not isinstance(client, str):
        #     raise ValueError(f"Expected type to be `str`. Got type {str(type(client))}")
        # client = client.lower()
        # if client in ["insta", "instagaram"]:
        #     login_params = LoginParams.Insta_Params
        # elif client in ["spotify"]:
        #     client_url = LoginUrl.SPOTIFY
        # else:
        #     raise ValueError(f"Expected type to be ['instagram', 'spotify']. Got type {str(type(client))}")
        # return client_url

    
    def get_client_url(self, client: str = "") -> str:
        """
        For each client get its login url        
        """                
        if not isinstance(client, str):
            raise ValueError(f"Expected type to be `str`. Got type {str(type(client))}")
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
    
    # def call_api(
    #     self,
    #     params: Dict = None,
    #     query: Dict = None,
    #     version: str = "v1"        
    #     ) -> Dict:
    #     """
    #     Calls client api
    #     Args:
    #     Returns:        
    #     """
    #     raise NotImplementedError
    
    def format_response(self, 
        response: Dict
    ) -> Dict:
        raise NotImplementedError




class InstaClient(Client, BaseConnector):
    """
    All operations to insta are derived from this base class.
    """    

    CLIENT = "insta"

    def __init__(self, username: str, password: str= "", **kwargs) -> None:
        self.username = username
        self.password = password
        self.csrf = kwargs.get('csrf', '')    
        # logging to insta client
    
    def get_client(self):
        ...
    
    def __classname__(self):
        return self.__class__.__name__
    
    def get_csrf_token(self, response):
        print(response.cookies)
        return response.cookies.get('csrftoken','')
        
    # @property
    # def csrf_token(self)-> str:
    #     return self.response.cookie.get('csrftoken','')
    
    # @csrf_token.setter
    # def csrf_token(serlf, response: Dict) -> str:
    #     self.response = response
    
    @property
    def headers(self):
        return {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": self.csrf
        }    

    def login(self):
        """
        Login to insta client        
        """
        
        # client = self.CLIENT
        # url = self.get_client_url(client=client)
        # if not (self.username and self.password):
        #     raise ClientLoginError(message="login required", code=400)                

        # # to get the cookie 
        # pre_login_response = self._call_api(
        #     url=url,
        #     type="get"
        # )
        # csrf = self.get_csrf_token(pre_login_response)
        # print(f"CSRF : {csrf}")
        
        # # get login url
        # login_url = self.login_url(client=client)

        # login_headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        # "X-Requested-With": "XMLHttpRequest",
        # "Referer": "https://www.instagram.com/accounts/login/",
        # "x-csrftoken": csrf
        # }
        # login_response = self._call_api(
        #     url = login_url, 
        #     params= self.login_params(client=client) , 
        #     headers= login_headers,
        #     type="post"
        #     )
        logger.debug(f"Login Response : -----------------------")
    

    def _call_api(
        self,
        url: str = "",
        params: Dict = None,
        headers: Dict = None,
        version: str = "v1",
        type: str = ""
        ) -> Dict:        
        
        logger.info(f"Connecting to {self.__class__.__name__}")
        if not type:
            return {}
        if type == "get":
            response = requests.get(url)
        elif type == "post":
            response = requests.post(url, data = params, headers = headers)
        return response






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


class Spotify(Client):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    
    def login(self):
        logger.debug(f"Login for {self.__class__.__name__}")

def main():
    pass


if __name__ == "__main__":
    main()

username ="gh_ashish"
password = ""
payload = {
    'username': '<USERNAME HERE>',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',  # <-- note the '0' - that means we want to use plain passwords
    'queryParams': {},
    'optIntoOneTap': 'false'
}
