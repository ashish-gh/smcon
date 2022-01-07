from enum import Enum

from smcon.clients.clients import InstaClient

class ClientUrl(Enum):
    INSTA_URL = "https://www.instagram.com/"
    SPOTIFY_USL = "https://www.spotify.com/np-en/"

class LoginUrl(Enum):
    INSTA_URL = "https://www.instagram.com/"
    SPOTIFY_USL = "https://www.spotify.com/np-en/"


class LoginParams:
    insta = {
            'username': '',
            'password': '',
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }

    def __init__(self, instance) -> None:
        self.instance = instance
        
        ...
        

    Spotify_Params = {
            'username': '',
            'password': '',
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }

