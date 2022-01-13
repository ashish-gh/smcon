from __future__ import annotations
import time
import typing
import json
import requests
from abc import abstractmethod
from typing import Dict

from smcon.structures.enums import ParamsFactory

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
    def login_params(self, client: str ="") -> dict:
        return ParamsFactory.get_params(client=client)
    

    @property
    def login_url(self) -> str:
        return self.get_login_url()
    
    def get_login_url(self):
        logger.info(f"Getting login url for {self.__class__.__name__}")
        # TODO
        # validate the url : str, instance and all        
        return LoginUrl(self).get_url()
                
    @abstractmethod
    def connect(self):
        raise NotImplementedError
    
    @abstractmethod
    def call_api(self) -> dict:
        raise NotImplementedError
    
    @abstractmethod
    def format_response(self, 
        response: Dict
    ) -> Dict:
        raise NotImplementedError
    



class InstaClient(Client, BaseConnector):
    """
    All operations to insta are derived from this base class.
    """    

    CLIENT = "insta"

    def __init__(self, username: str, password: str, **kwargs) -> None:
        self.username = username
        self.password = password
        self.csrf = kwargs.get('csrf', '')    

    @property    
    def client(self) -> str:        
        client = self.CLIENT
        if not client:
            # TODO
            # raise error using ErrorClass
            logger.debug(f"Client not set for {str(self.__class__.__name__)}")
            return ""
        if not isinstance(client, str):
            raise TypeError(f"Expected type of clinet to be `str`. Got : {str(type(client))}")        
        return client            
        
    @property
    def headers(self):
        return {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": self.get_csrf()
        }    
    
    @property
    def payload(self):
        return {
           'username': self.username,
           'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{self.password}',
           'queryParams': {},
           'optIntoOneTap': 'false'
        }
        
    

    def call_api(
        self,
        url: str = "",
        payload: Dict = None,
        headers: Dict = None,
        version: str = "v1",
        type: str = "",
        message: str = ""
        ) -> Dict:        
        """
        Base method to make connection to all the api endpoints
        """
        
        logger.info(f"Calling {str(self.__class__.__name__)} api for {str(message)}")
        # TODO
        # make exception on response
        try:
            response = requests.post(url, data = payload, headers = headers)
        except:
            logger.error(f"Error on making post request on {str(self.__class__.__name__)}")
            return {}
        try:
            data = json.loads(response.text)
        except Exception as e:
            logger.error(f"Exception on parsing error : {str(e)}")
            return {}
        return data
        


    def get_csrf(self):        
        logger.info(f"Getting csfr token for : {self.__class__.__name__}")
        link = 'https://www.instagram.com/accounts/login/'
        # TODO 
        # generate some error if problem in connection
        response = requests.get(link)
        # TODO
        # Raise error if not cookies make 
        # abort or something 
        logger.info(f"Cookies : {response.cookies}")
        return response.cookies.get('csrftoken')


    def login(self):
        """
        Login to insta client        
        *All the steps required for login for each of client is performed here.
        Some client might require more operation to connect to client while some might require less 
        and it all depends on clinet*
        
        """

        # check if username and password is provided
        if not (self.username and self.password):
            raise ClientLoginError(message="login required", code=400)                        
        # 
        login_params = self.login_params
        if (not login_params) or  (not isinstance(login_params, dict)):
            # TODO
            # raise some error implement it
            return {}
        
        # Next steps are to get token and to get and to check other     
        client = self.client
        # connect to client to get cookie
        login_url = self.login_url
        print(f"Login url  : {str(login_url)}")
        # call the api
        res = self.call_api(
            url=login_url,
            payload=self.payload, 
            headers=self.headers,
            message="login"
            )
        return res


        






    def format_response(self, response: Dict) -> Dict:
        return response
        
    def connect(self, username: str, password: str) -> None:
        ...

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
