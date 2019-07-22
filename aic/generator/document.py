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
    __input_file: click.Path
    __output_file: click.Path
    __paper: Paper

    def __init__(self):
        super().__init__()

    @property
    def label_type(self) -> Label:
        """
        Avery Zweckform label type.

        :return: Label
        """
        return self.__label_type

    @label_type.setter
    def label_type(self, value: int):
        self.__label_type = Label(value)

    @property
    def pages(self) -> int:
        """
        Number of pages to generate.

        :return: int
        """
        return self.__pages

    @pages.setter
    def pages(self, value: int):
        self.__pages = value

    @property
    def paper(self) -> Paper:
        """
        Type of paper to generate.

        :return: Paper
        """
        return self.__paper

    @paper.setter
    def paper(self, value: str):
        if value.upper() in PaperFormat.__members__:
            self.__paper = Paper(PaperFormat[value.upper()])
        else:
            raise TypeError("The given paper type is not valid.")

    @property
    def input_file(self) -> click.Path:
        """
        Path of the input image to print.

        :return: click.Path
        """
        return self.__input_file

    @input_file.setter
    def input_file(self, value: click.Path):
        self.__input_file = value

    @property
    def output_file(self) -> click.Path:
        """
        Path of the output PDF file.

        :return: click.Path
        """
        return self.__output_file

    @output_file.setter
    def output_file(self, value: click.Path):
        self.__output_file = value

    def build(self):
        """
        Build function with progress bar.
        """
        pdf = FPDF(orientation='L', unit='mm', format=self.paper.format.value)
        pdf.set_xy(0, 0)
        pdf.set_font('Arial', '', 14)
        for page in tqdm(range(self.pages)):
            pdf.add_page()
            pdf.write(5, str(page + 1))
        pdf.output(str(self.output_file), 'F')
