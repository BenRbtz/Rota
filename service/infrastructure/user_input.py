from argparse import ArgumentParser, Namespace
from datetime import datetime

from service.ports.ports import UserInputPort


class ArgUserInput(UserInputPort):

    def get(self) -> UserInputPort.RotaInput:
        args = self.arg_parse()
        file_name = args.file_name
        year = args.year
        month_name = args.month_name
        day_names = args.day_names

        return UserInputPort.RotaInput(file_name=file_name, year=year, month_name=month_name, day_names=day_names)

    @staticmethod
    def arg_parse() -> Namespace:
        current_year = datetime.now().year

        parser = ArgumentParser()

        parser.add_argument('-f', '--file_name', help="file name to store rota output", default='rota.xlsx')
        parser.add_argument('-y', '--year', help="Desired year for rota", type=int, default=current_year)
        parser.add_argument('-m', '--month_name', help="Name of the month desired for rota", required=True)
        parser.add_argument('-d', '--day_names', help="Names of days desired for rota", required=True, nargs='+')

        return parser.parse_args()
