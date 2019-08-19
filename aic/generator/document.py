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
        self.__label_type = Label.load_type(str(value))

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
        print('Rows: {}\nColumns: {}\nOffset h: {}\nOffset w: {}\nOffset between labels: {}\n'.format(
            str(self.label_type.rows),
            str(self.label_type.columns),
            str(self.label_type.offset_height),
            str(self.label_type.offset_width),
            str(self.label_type.offset_between_label)
        ))
        for page in tqdm(range(self.pages)):
            pdf.add_page()
            x_offset: float = 0
            y_offset: float = 0

            for label_count in range(self.label_type.rows * self.label_type.columns):
                pdf.image(
                    name=self.input_file,
                    x=self.label_type.offset_height + x_offset,
                    y=self.label_type.offset_width + y_offset,
                    w=self.label_type.width,
                    h=self.label_type.height,
                    type='PNG')
                if label_count == self.label_type.rows - 1:
                    x_offset = 0
                    y_offset += self.label_type.height + self.label_type.offset_between_label
                else:
                    x_offset += self.label_type.width
        pdf.output(str(self.output_file), 'F')
