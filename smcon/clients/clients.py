from __future__ import annotations
import typing
import requests
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
    def __init__(self, username: str, password: str= "", **kwargs) -> None:
        self.username = username
        self.password = password
        self.csrf = kwargs.get('csrf', '')    
        # logging to insta client
        self.login()
    
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
        if not (self.username and self.password):
            # raise ClientLoginError()
            raise ClientLoginError(message="login required", code=400)                
        # pre_login_ = 
        # to get the cookie 
        url = 'https://www.instagram.com/accounts/login/'
        pre_login_response = self._call_api(
            url=url,
            type="get"
        )
        csrf = self.get_csrf_token(pre_login_response)
        print(f"CSRF : {csrf}")

        
        # login url
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        login_params = {
            'username': self.username,
            'password': self.password,
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }
        login_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
        }
        login_response = self._call_api(
            url = login_url, 
            params= login_params, 
            headers= login_headers,
            type="post"
            )
        logger.debug(f"Login Response : {str(login_response)}")
    

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


def main():
    pass


if __name__ == "__main__":
    main()

username ="gh_ashish"
password = "AAashishghimire0102#"
payload = {
    'username': '<USERNAME HERE>',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',  # <-- note the '0' - that means we want to use plain passwords
    'queryParams': {},
    'optIntoOneTap': 'false'
}
