from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Tuple


@dataclass
class User:
    """
    Represents user details
        - username: str
        - password: str

    Properties:
        -
    """

    username: str = ""
    password: str = ""

    # @property
    # def username(self) -> str:
    #     return self.username

    # @username.setter
    # def username(self, username) -> None:
    #     self.username = username

    # @property
    # def password(self) -> str:
    #     return self.password

    # @password.setter
    # def password(self, password) -> None:
    #     self.password = password

    def to_tuple(self) -> Tuple[str, str]:
        return tuple([self.username, self.password])

    def __iter__(self) -> Iterator[str]:
        yield from [self.username, self.password]

    def copy(self) -> User:
        return User(username=self.username, password=self.password)

    def __hash__(self) -> int:
        return hash(tuple(self.__dict__.items()))
