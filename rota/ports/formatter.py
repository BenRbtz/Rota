from typing import List

from rota.domain.models.calender import Month
from rota.domain.models.person import Instructor


class RotaFormatPort:
    def format_column_names(self, columns: list, *args, **kwargs) -> list:
        pass

    def format_columns(self, month: Month, instructors: List[Instructor], *args, **kwargs) -> list:
        pass
