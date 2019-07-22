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

    _label_dimensions: list = [0, 0]

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
