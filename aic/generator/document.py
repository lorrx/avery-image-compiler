"""
Document module to prepare Avery labels and positioning.
"""
import click
from fpdf import FPDF
from labels.label import Label
from generator.paper import Paper, PaperFormat
from tqdm import tqdm


class Document:
    """
    Document class definition.
    """
    __label_type: Label
    __pages: int
    __input_file: click.File
    __output_file: click.File
    __paper: Paper

    def __init__(self):
        super().__init__()

    @property
    def label_type(self) -> Label:
        """

        :return:
        """
        return self.__label_type

    @label_type.setter
    def label_type(self, value: int):
        self.__label_type = Label(value)

    @property
    def pages(self) -> int:
        """

        :return:
        """
        return self.__pages

    @pages.setter
    def pages(self, value: int):
        self.__pages = value

    @property
    def paper(self) -> Paper:
        return self.__paper

    @paper.setter
    def paper(self, value: str):
        if value.upper() in PaperFormat.__members__:
            self.__paper = Paper(PaperFormat[value.upper()])
        else:
            raise TypeError("The given paper type is not valid.")

    @property
    def input_file(self) -> click.File:
        """

        :return:
        """
        return self.__input_file

    @input_file.setter
    def input_file(self, value: click.File):
        self.__input_file = value

    @property
    def output_file(self) -> click.File:
        """

        :return:
        """
        return self.__output_file

    @output_file.setter
    def output_file(self, value: click.File):
        self.__output_file = value

    def build(self):
        """

        """
        pdf = FPDF(orientation='P', unit='mm', format=self.paper.format.value)
        for page in tqdm(range(self.pages)):
            pdf.add_page()

        pdf.output(str(self.output_file), 'F')
