
from loguru import logger

from .clients import Client



class Spotify(Client):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self):
        logger.debug(f"Login for {self.classname}")
    

