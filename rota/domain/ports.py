from collections import namedtuple
from typing import List

from rota.domain.models.calender import Month
from rota.domain.models.person import Instructor


class UserInputPort:
    RotaInput = namedtuple('RotaInput', 'file_name year month_name day_names')

    def get(self, *args, **kwargs) -> RotaInput:
        pass


class DateGeneratorPort:
    Table = namedtuple('Table', 'columns rows')

    def generate(self, *args, **kwargs) -> Table:
        pass


class NameGeneratorPort:
    def generate(self, *args, **kwargs) -> List[Instructor]:
        pass


class RotaFormatPort:
    def format_column_names(self, columns: list, *args, **kwargs) -> list:
        pass

    def format_columns(self, month: Month, instructors: List[Instructor], *args, **kwargs) -> list:
        pass


class OutputPort:
    def create(self, title: str, column_names: list, rows: list, *args, **kwargs):
        pass
