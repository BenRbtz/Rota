from collections import namedtuple
from typing import List

Table = namedtuple('Table', 'columns rows')


class DateGeneratorPort:
    def generate(self, year: int, month_name: str, day_names: List[str]) -> Table:
        pass
