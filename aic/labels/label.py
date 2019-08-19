"""
Parent class for all label types.
"""

from generator.paper import Paper


class Label(Paper):
    """
    Label class definition.
    """
    supported_labels: list = [
        'Avery6123'
    ]

    _label_dimensions: list = [0.0, 0.0]
    _offset_between_columns: float = 0.0

    def __init__(self):
        super().__init__()

    @staticmethod
    def load_type(type_id: str) -> any:
        """
        Loads a supported Avery label type by ID.

        :param type_id: str
        :return: any | avery type class instance.
        """
        class_type_string: str = 'Avery{}'.format(type_id)

        if class_type_string in Label.supported_labels:
            return getattr(
                __import__(
                    'labels.avery.avery_{}'.format(type_id),
                    globals(),
                    locals(),
                    [class_type_string],
                    0
                ),
                class_type_string
            )()
        else:
            raise TypeError('The current label is not supported.')

    @property
    def rows(self) -> int:
        return int(self.page_height / self._label_dimensions[0])

    @property
    def columns(self) -> int:
        return int(self.page_width / self._label_dimensions[1])

    @property
    def offset_height(self) -> float:
        return (self.page_height - (self.rows * self._label_dimensions[0])) / 2

    @property
    def offset_width(self) -> float:
        return (self.page_width - (self.columns * self._label_dimensions[1])) / 2

    @property
    def height(self) -> float:
        return self._label_dimensions[1]

    @property
    def width(self) -> float:
        return self._label_dimensions[0]

    @property
    def offset_between_label(self) -> float:
        return self._offset_between_columns

    @offset_between_label.setter
    def offset_between_label(self, value):
        self._offset_between_columns = value
