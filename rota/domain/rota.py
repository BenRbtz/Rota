from typing import List

from rota.ports.data_generator import DateGeneratorPort
from rota.ports.formatter import RotaFormatPort
from rota.ports.storage import StoragePort


class Rota:
    def __init__(self, date_generator: DateGeneratorPort, formatter: RotaFormatPort,
                 storage: StoragePort):
        self._date_generator = date_generator
        self._formatter = formatter
        self._storage = storage

    def generate(self, file_name: str, year: int, month_name: str, day_names: List[str]) -> None:
        dates = self._date_generator.generate(year=year, month_name=month_name, day_names=day_names)
        formatted_columns = self._formatter.format_column_names(column_names=dates.columns)
        formatted_rows = self._formatter.format_columns(rows=dates.rows)
        self._storage.save(file_name=file_name, title=month_name, column_names=formatted_columns,
                           rows=formatted_rows)
