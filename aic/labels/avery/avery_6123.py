"""
Avery Zweckform label 6123.

https://www.avery-zweckform.com/produkt/universal-etiketten-6123
"""
from generator.paper import PaperFormat
from labels.label import Label


class Avery6123(Label):
    """
    Avery 6123 class definition.
    """
    _label_dimensions: list = [42.3, 97]

    def __init__(self):
        super().__init__()
        self.format = PaperFormat.A4
