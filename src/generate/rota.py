class Rota:
    def __init__(self, calender, spreadsheet):
        self.calender = calender
        self.spreadsheet = spreadsheet

    def run(self, file_path, year, month_name, day_names):
        month = self.calender.get_days_in_month(year, month_name, day_names)
        grid = self.spreadsheet.get_grid(month)
        self.spreadsheet.write(file_path, month_name, grid)
