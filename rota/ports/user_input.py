from collections import namedtuple

RotaInput = namedtuple('RotaInput', 'file_name year month_name day_names')


class UserInputPort:
    def get(self, *args, **kwargs) -> RotaInput:
        """
        Get input from user
        """
