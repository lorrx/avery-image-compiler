"""
Main function of the Avery Image Compiler commandline tool.
"""
import click
from generator.document import Document


@click.command()
@click.option(
    '--input-file',
    '-i',
    type=click.File('r'),
    required=True,
    help='Path of the image to print as a Avery label. Improve, that the dimensions are correctly set.'
)
@click.option(
    '--label-type',
    '-t',
    type=int,
    required=True,
    help='The Avery Zweckform label number to print.'
)
@click.option(
    '--pages',
    '-p',
    type=int,
    default=1,
    help='Number of pages to generate.'
)
@click.option(
    '--output-file',
    '-o',
    type=click.File('w'),
    default='./output.pdf',
    help='Path of the generated output PDF file.'
)
def main(input_file: click.File, pages: int, label_type: int, output_file: click.File):
    pdf = Document()
    pdf.pages = pages
    pdf.label_type = label_type
    pdf.input_file = input_file
    pdf.output_file = output_file
    pdf.build()


if __name__ == '__main__':
    main()
    exit(0)
