import argparse
import datetime

from generate import calender, spreadsheet, rota

current_year = datetime.datetime.now().year

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file_name', help="file name to store rota output", default='rota.xlsx')
parser.add_argument('-y', '--year', help="Desired year for rota", type=int, default=current_year)
parser.add_argument('-m', '--month_name', help="Name of the month desired for rota", required=True)
parser.add_argument('-d', '--day_names', help="Names of days desired for rota", required=True, nargs='+')

args = parser.parse_args()

my_spreadsheet = spreadsheet.Spreadsheet()
my_calender = calender.Calender()
my_rota = rota.Rota(my_calender, my_spreadsheet)

my_rota.run(args.file_name, args.year, args.month_name, args.day_names)
