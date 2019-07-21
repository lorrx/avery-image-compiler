"""
Document module to prepare Avery labels and positioning.
"""
import click
from fpdf import FPDF
from labels.label import Label


class Document(FPDF):
    """
    Document class definition.
    """
    __label_type: Label
    __pages: int
    __input_file: click.File
    __output_file: click.File

    def __init__(self):
        super().__init__()

    @property
    def label_type(self) -> Label:
        return self.__label_type

    @label_type.setter
    def label_type(self, value: int):
        self.__label_type = Label(value)

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, value: int):
        self.pages = value

    @property
    def input_file(self) -> click.File:
        return self.__input_file

    @input_file.setter
    def input_file(self, value: click.File):
        self.__input_file = value

    @property
    def output_file(self) -> click.File:
        return self.__output_file

    @output_file.setter
    def output_file(self, value: click.File):
        self.output_file = value
