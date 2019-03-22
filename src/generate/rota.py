from argparse import ArgumentParser
from datetime import datetime


def parse_args():
    current_year = datetime.now().year

    parser = ArgumentParser()

    parser.add_argument('-f', '--file_name', help="file name to store rota output", default='rota.xlsx')
    parser.add_argument('-y', '--year', help="Desired year for rota", type=int, default=current_year)
    parser.add_argument('-m', '--month_name', help="Name of the month desired for rota", required=True)
    parser.add_argument('-d', '--day_names', help="Names of days desired for rota", required=True, nargs='+')

    return parser.parse_args()


class Rota:
    def __init__(self, calender, spreadsheet):
        self.calender = calender
        self.spreadsheet = spreadsheet
        self.args = parse_args()

    def generate(self):
        month = self.calender.get_days_in_month(self.args.year, self.args.month_name, self.args.day_names)
        grid = self.spreadsheet.get_grid(month)
        self.spreadsheet.write(self.args.file_name, self.args.month_name, grid)
