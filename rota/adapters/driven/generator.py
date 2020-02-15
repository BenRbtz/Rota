from typing import List

from rota.ports.data_generator import DateGeneratorPort, Table
from rota.domain.models.calender import Days, Month


class MonthGenerator(DateGeneratorPort):
    def generate(self, year: int, month_name: str, day_names: List[str]) -> Table:
        days = Days(names=day_names)
        month = Month(year=year, name=month_name, days=days)

        return Table(columns=days.names, rows=month)
