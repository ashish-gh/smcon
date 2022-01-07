
class BaseConfig:
    URL = ""
    BASE_URL =""


class InstaConfig(BaseConfig):
    URL = 'https://www.instagram.com/accounts/login/ajax/'
    BASE_URL = "https://www.instagram.com/"
    LOGIN_URL = 'https://www.instagram.com/accounts/login/'

    @staticmethod
    def login_params(self):
        return {
            'username': '',
            'password': '',
            'queryParams': {},
            'optIntoOneTap': 'false'            
        }


