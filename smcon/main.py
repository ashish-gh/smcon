from loguru import logger

from .clients.client import Client


class SocailMediaConnector:
    """
    Parent class from where we connect to all the applicaiton.

    """

    def connect(self, client: Client):
        """
        Base method to connect to all the clients.
        All connection derives from this method
        """
        if not isinstance(client, Client):
            raise TypeError(f"Expected to be type.... got type {str(client)}")

        # whatever the client is it logins to the client just have to pass the instance of the client
        logger.info(f"Connecting to the client . . . {str(client.__class__.__name__)}")

        # Connection logic for each of the client is dependent on it. The parent class is not dependent on it.
        # The parent class only cares to login. not how, in which url it connects to
        res = client.login()
        print(res)
