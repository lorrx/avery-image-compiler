"""
Paper class to collect and serve the correct paper format.
"""
from enum import Enum


class PaperFormat(Enum):
    """
    Paper format
    """
    A4: str = 'a4'
    A5: str = 'a5'


class Paper:
    """
    Paper class definition.
    """
    __format: PaperFormat
    __dimensions: dict = {
        'a4': [210, 297],
        'a5': [148, 210]
    }

    def __init__(self, paper_format: PaperFormat = None):
        if paper_format:
            self.format = paper_format

    @property
    def format(self) -> PaperFormat:
        """

        :return:
        """
        return self.__format

    @format.setter
    def format(self, value: PaperFormat):
        self.__format = value
