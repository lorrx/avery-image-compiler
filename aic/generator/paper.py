"""
Paper class to collect and serve the correct paper format.
"""
from enum import Enum


class PaperFormat(Enum):
    A4: str = 'a4'
    A5: str = 'a5'


class Paper:
    __format: PaperFormat

    @property
    def format(self) -> PaperFormat:
        return self.__format

    @format.setter
    def format(self, value: PaperFormat):
        self.__format = value
