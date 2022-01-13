from loguru import logger


class ClientErrorCodes:
    """
    Http error codes
    """

    INERNAL_SERVER_ERROR = 500
    BAD_REQUEST = 400
    NOT_FOUND = 404


class ClientError(Exception):
    """
    Generic error class
    """

    def __init__(
        self, message: str = "", code: int = None, error_response: str = ""
    ) -> None:
        if not isinstance(message, str):
            raise TypeError(
                f"Expected type of error message to be str. Got {type(message)}"
            )

        self.code = code
        self.error_message = error_response
        super(ClientError, self).__init__(message)

    @property
    def message(self):
        return self.args[0]


class ClientLoginError(ClientError):
    """
    Raises when client login fails
    """

    pass
