from enum import Enum



class ClientUrl(Enum):
    INSTA_URL = "https://www.instagram.com/"
    SPOTIFY_USL = "https://www.spotify.com/np-en/"

class LoginUrl:
    INSTA_URL = "https://www.instagram.com/accounts/login/ajax/"
    SPOTIFY_URL = "https://www.spotify.com/np-en/"


    def __init__(self, instance) -> None:
        self.instance = instance
        self.get_url()
    

    def get_url(self):
        """
        """
        # TODO
        # Optimal method to do this
        client = self.instance.CLIENT
        if client in ["insta"]:
            return LoginUrl.INSTA_URL
        elif client in ["spotify"]:
            return LoginUrl.SPOTIFY_URL
        return ""

    



class LoginParams:
    """
    For each client you only have to add login params.
    """    
    insta = {
            'username': '',
            'password': '',
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }
    
    # soptify params
    spotify = {
            'username': '',
            'password': '',
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }


    def __init__(self, instance) -> None:
        self.instance = instance
        self.get_params()
    

    def get_params(self):
        """
        """
        # TODO
        # Optimal method to do this
        client = self.instance.CLIENT
        if client in ["insta"]:
            return LoginParams.insta
        elif client in ["spotify"]:
            return LoginParams.spotify
        return {}


        


