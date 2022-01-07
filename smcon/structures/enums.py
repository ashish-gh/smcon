from enum import Enum

class ClientUrl(Enum):
    INSTA_URL = "https://www.instagram.com/"
    SPOTIFY_USL = "https://www.spotify.com/np-en/"

class LoginUrl(Enum):
    INSTA_URL = "https://www.instagram.com/"
    SPOTIFY_USL = "https://www.spotify.com/np-en/"


class LoginParams(Enum):
    Insta_Params = {
            'username': '',
            'password': '',
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }

    Spotify_Params = {
            'username': '',
            'password': '',
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }

