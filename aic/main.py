"""
Main function of the Avery Image Compiler commandline tool.
"""
import click
from generator.document import Document


@click.command()
@click.option(
    '--input-file',
    '-i',
    type=click.Path(exists=True),
    required=True,
    help='Path of the image to print as a Avery label. Improve, that the dimensions are correctly '
         'set.'
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
    type=click.Path(exists=False),
    default='./output.pdf',
    help='Path of the generated output PDF file.'
)
@click.option(
    '--page_format',
    '-f',
    type=str,
    default='a4',
    help='The paper format that is used by the Avery label article. [a4 | a5]'
)
def main(input_file: click.Path, pages: int, label_type: int, output_file: click.Path,
         page_format: str):
    """
    The Avery Image Compiler (AIC) allows that images can be prepared as Avery-Zweckform labels
    without loss of quality. \n
    """
    click.echo('Welcome to the Avery Image Compiler\n')
    click.echo('Input file: {}'.format(input_file))
    click.echo('Output file: {}'.format(output_file))
    click.echo('Number of PDF pages: {}'.format(pages))
    click.echo('Avery Label: {}\n'.format(label_type))
    pdf = Document()
    pdf.pages = pages
    pdf.label_type = label_type
    pdf.paper = page_format
    pdf.input_file = input_file
    pdf.output_file = output_file
    pdf.build()


if __name__ == '__main__':
    main()
    exit(0)
