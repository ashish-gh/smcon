from enum import Enum
from typing import Dict


class ClientUrl(Enum):
    INSTA_URL = "https://www.instagram.com/"
    SPOTIFY_URL = "https://www.spotify.com/np-en/"


class UrlFactory:
    @property
    def url(self):
        return {
            "insta": "https://www.instagram.com/",
            "spotify": "https://www.spotify.com/np-en/",
        }

    def get_url(self, client: str = "") -> str:
        if not client:
            return ""
        if not isinstance(client, str):
            raise TypeError(
                f"Expected type to be `str`. Instead got :{str(type(client))}"
            )
        if client not in list(self.url.values()):
            raise NotImplementedError(f"{client} urls is not implemented.")
        return self.url.get(client)


class ParamsFactory:
    @property
    def params(self):
        return {
            "insta": {
                "username": "",
                "password": "",
                "queryParams": {},
                "optIntoOneTap": "false",
            },
            "spotify": {
                "username": "",
                "password": "",
                "queryParams": {},
                "optIntoOneTap": "false",
            },
        }

    def get_params(self, client: str = "") -> Dict[str, Dict]:
        if not client:
            return None
        if not isinstance(client, str):
            raise TypeError(
                f"Expected type to be `str`. Instead got :{str(type(client))}"
            )
        if client not in list(self.params.values()):
            raise NotImplementedError(f"{client} params is not implemented.")
        return self.params.get(client)
