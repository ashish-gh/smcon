# import json
# import requests
# from datetime import datetime

from smcon.clients.clients import Client, InstaClient, Spotify
from smcon.main import SocailMediaConnector

# Implementing new client
# class Fb(Client):
#     def __init__(self, username: str, password: str) -> None:
#         self.username = username
#         self.password = password
#     def login(self):
#         # the user will have to write the login logic
#         ...
#     def connect():
#         return "connect"

username = "asfd"
password = "asfd"
SocailMediaConnector().connect(InstaClient(username=username, password=password))

# SocailMediaConnector().connect(Spotify(username="as", password="asf"))
# SocailMediaConnector().connect((username="as", password="asf"))
