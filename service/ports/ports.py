from collections import namedtuple
from typing import List

from service.business_logic.calender import Month
from service.business_logic.person import Instructor


class UserInputPort:
    RotaInput = namedtuple('RotaInput', 'file_name year month_name day_names')

    def get(self, *args, **kwargs) -> RotaInput:
        pass


class DateGeneratorPort:
    Table = namedtuple('Table', 'columns rows')

    def generate(self, *args, **kwargs) -> Table:
        pass


class TableFormatPort:
    def format_column_names(self, columns: list, *args, **kwargs) -> list:
        pass

    def format_columns(self, month: Month, instructors: List[Instructor], *args, **kwargs) -> list:
        pass


class OutputPort:
    def create(self, title: str, column_names: list, rows: list, *args, **kwargs):
        pass
