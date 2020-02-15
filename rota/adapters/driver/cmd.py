from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import datetime
from typing import List

from rota.adapters.driven.formatter import MonthTableFormatter
from rota.adapters.driven.generator import MonthGenerator
from rota.adapters.driven.storage import Spreadsheet
from rota.domain.rota import Rota


@dataclass(frozen=True)
class AppConfig:
    file_name: str
    year: int
    month_name: str
    day_names: List[str]

    @classmethod
    def read_environment(cls):
        parser = ArgumentParser()

        parser.add_argument('-f', '--file_name', help="file name to store rota output",
                            default='rota.xlsx')
        parser.add_argument('-y', '--year', help="Desired year for rota", type=int,
                            default=datetime.now().year)
        parser.add_argument('-m', '--month_name', help="Name of the month desired for rota",
                            required=True)
        parser.add_argument('-d', '--day_names', help="Names of days desired for rota",
                            required=True, nargs='+')

        args = parser.parse_args()

        return cls(
            file_name=args.file_name,
            year=args.year,
            month_name=args.month_name,
            day_names=args.day_names,
        )


if __name__ == '__main__':
    config = AppConfig.read_environment()

    Rota(
        date_generator=MonthGenerator(),
        formatter=MonthTableFormatter(),
        storage=Spreadsheet()
    ).generate(file_name=config.file_name, year=config.year, month_name=config.month_name,
               day_names=config.day_names)
