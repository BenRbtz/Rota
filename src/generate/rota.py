from datetime import datetime


class Rota:
    current_year = datetime.now().year

    def __init__(self, calender, spreadsheet):
        self.calender = calender
        self.spreadsheet = spreadsheet

    def run(self, file_path, month_name, day_name1, day_name2):
        days_in_month = self.calender.get_days_in_month(self.current_year, month_name, day_name1, day_name2)
        grid = self.spreadsheet.get_grid(day_name1, day_name2, days_in_month)
        self.spreadsheet.write(file_path, month_name, grid)
