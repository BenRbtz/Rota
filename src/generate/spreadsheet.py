from collections import OrderedDict
from datetime import date, timedelta

import xlsxwriter


class Spreadsheet:
    column_map = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
    }

    def get_grid(self, month):
        header = self._get_header(month)

        suffixed_day_dates = self._get_suffixed_day_dates(month)
        weeks = zip(*suffixed_day_dates)

        grid = [header]
        for days in weeks:
            row = []
            for day in days:
                row.append(day)
                row.append('')
            grid.append(row)

        return grid

    @staticmethod
    def _get_header(month):
        header = []
        for day in month.values():
            header.append('')
            header.append(day['day_name'])
        return header

    def _get_suffixed_day_dates(self, month: OrderedDict):
        suffixed_day_dates = []
        for day in month.values():
            suffixed_day_date = self._format_dates_with_suffix(day['dates'])

            if len(day['dates']) == 5:
                suffixed_day_dates.append(suffixed_day_date)
                continue

            year = day['year']
            month_name_value = day['month_name_value']

            # Check if first date is after the first week
            d = date(year, month_name_value, 1)
            last_day_of_first_week = timedelta(days=6 - d.weekday()).days
            if day['dates'][0] > last_day_of_first_week:
                suffixed_day_date.insert(0, '')
            else:
                suffixed_day_date.append('')

            suffixed_day_dates.append(suffixed_day_date)

        return suffixed_day_dates

    def _format_dates_with_suffix(self, dates):
        formatted_dates = []
        for one_date in dates:
            suffixed_date = str(self._get_day_with_suffix(one_date))
            formatted_dates.append(suffixed_date)
        return formatted_dates

    @staticmethod
    def _get_day_with_suffix(day):
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        return f'{day}{suffix}'

    def write(self, file_name, month_name, grid):
        with xlsxwriter.Workbook(file_name) as workbook:
            worksheet = workbook.add_worksheet()

            header_column_count = len(grid[0])
            merge_format = workbook.add_format({'align': 'center', 'border': 6})
            worksheet.merge_range(f"A1:{self.column_map[header_column_count]}1", month_name, merge_format)

            column_offset = 1
            for col, row in enumerate(grid):
                worksheet.write_row(col + column_offset, 0, row, merge_format)
