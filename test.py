
# import json
# import requests
# from datetime import datetime

from smcon.clients.clients import InstaClient, Spotify, Client
from smcon.main import SocailMediaConnector

# Implementing new client 
class Fb(Client):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    def login(self):
        # the user will have to write the login logic
        ...
    def connect():        
        return "connect"

username ="as"
password = "a"
SocailMediaConnector().connect(InstaClient(username="as", password="asf"))

SocailMediaConnector().connect(Spotify(username="as", password="asf"))

SocailMediaConnector().connect(Fb(username="as", password="asf"))

# SocailMediaConnector().connect((username="as", password="asf"))


# # from smcon.clients.clients import InstaClient
# username = "gh_ashish"
# password = "..."

# InstaClient(username=username, password=password).login()



# link = 'https://www.instagram.com/accounts/login/'
# login_url = 'https://www.instagram.com/accounts/login/ajax/'

# time = int(datetime.now().timestamp())
# response = requests.get(link)
# csrf = response.cookies['csrftoken']

# payload = {
#    'username': username,
#    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
#    'queryParams': {},
#    'optIntoOneTap': 'false'
# }

# login_header = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
#    "X-Requested-With": "XMLHttpRequest",
#    "Referer": "https://www.instagram.com/accounts/login/",
#    "x-csrftoken": csrf
# }

# login_response = requests.post(login_url, data = payload, headers = login_header)
# json_data = json.loads(login_response.text)
# print(json_data)
# if json_data["authenticated"]:
#     print("login successful")
#     cookies = login_response.cookies
#     cookie_jar = cookies.get_dict()
#     csrf_token = cookie_jar['csrftoken']
#     print("csrf_token: ", csrf_token)
#     session_id = cookie_jar['sessionid']
#     print("session_id: ", session_id)
# else :
#    print("login failed ", login_response.text)
