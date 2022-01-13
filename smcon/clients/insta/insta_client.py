import os
import re
import time
import requests
from socket import timeout, error as SOCKET_ERROR
from typing import  Dict

from loguru import logger

from .clients import Client
from ..utils import load_response
from ...connector import BaseConnector
from ...structures import ParamsFactory, UrlFactory, User
from ..errors import ClientLoginError, ClientConnectionError


class InstaClient(Client, BaseConnector):
    """
    All operations to insta are derived from this base class.

    Property: 
        - client
        - headers
        - payload
        - 

    Method

    """

    CLIENT = "insta"

    def __init__(self, username: str, password: str, **kwargs) -> None:
        self.username = username
        self.password = password
        self.csrf = kwargs.get("csrf", "")

    @property
    def client(self) -> str:
        client = self.CLIENT
        if not client:
            logger.debug(f"Client not set for {str(self.classname)}")
            return ""
        if not isinstance(client, str):
            raise TypeError(
                f"Expected type of clinet to be `str`. Got : {str(type(client))}"
            )
        return client

    @property
    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": self.get_csrf(),
        }

    @property
    def payload(self):
        return {
            "username": self.username,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time}:{self.password}",
            "queryParams": {},
            "optIntoOneTap": "false",
        }

    def call_api(
        self,
        url: str = "",
        payload: Dict = None,
        headers: Dict = None,
        version: str = "v1",
        type: str = "",
        message: str = "",
    ) -> Dict:
        """
        Base method to make connection to all the api endpoints
        """
        logger.info(f"Calling {str(self.classname)} api for {str(message)}")
        try:
            response = requests.post(url, data=payload, headers=headers)
        except (timeout, SOCKET_ERROR) as connection_error :
            raise ClientConnectionError(
                message=f"connection error for {self.classname}", 
                error_response= str(connection_error), 
                code=502)
        data = load_response(response)
        return data


    def get_csrf(self):
        logger.info(f"Getting csfr token for : {self.classname}")
        link = "https://www.instagram.com/accounts/login/"
        try:
            response = requests.get(link)
        except (timeout, SOCKET_ERROR) as connection_error:
            raise ClientConnectionError(
                message=f"connection error for {self.classname}", 
                error_response= str(connection_error), 
                code=502)
        # TODO 
        # Implement method to get values from cookie just pass the parameter
        # get_cookie_value() for more details
        return response.cookies.get("csrftoken")
    
    def get_cookie_value(self, key: str ="") -> str:
        pass

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
        login_params = self.login_params(self.CLIENT)
        if (not login_params) or (not isinstance(login_params, dict)):
            return {}

        # Next steps are to get token and to get and to check other
        client = self.client
        # connect to client to get cookie
        login_url = self.login_url
        print(f"Login url  : {str(login_url)}")
        # call the api
        res = self.call_api(
            url=login_url, payload=self.payload, headers=self.headers, message="login"
        )
        return res

    def format_response(self, response: Dict) -> Dict[str, Dict]:
        return response

    def connect(self, username: str, password: str) -> None:
        ...

    def classname(self) -> str:
        return str(self.__class__.__name__)
