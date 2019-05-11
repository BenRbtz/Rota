from collections import OrderedDict
from datetime import date, timedelta

from service.ports.ports import TableFormatPort


class TableFormatter(TableFormatPort):
    def format_column_names(self, column_names, *args, **kwargs) -> list:
        formatted_column_names = []
        for column_name in column_names:
            formatted_column_names.append([''])
            formatted_column_names.append([column_name.capitalize()])

        return formatted_column_names

    def format_columns(self, rows, *args, **kwargs) -> list:
        suffixed_day_dates = self._get_suffixed_day_dates(rows)
        weeks = zip(*suffixed_day_dates)

        formatted_columns = []
        for days in weeks:
            formatted_row = []
            for day in days:
                formatted_row.append(day)
                formatted_row.append('')
            formatted_columns.append(formatted_row)
        return formatted_columns

    def _get_suffixed_day_dates(self, month: OrderedDict):
        max_specific_day_in_month = 5

        suffixed_day_dates = []
        for day in month.values():
            suffixed_day_date = self._format_dates_with_suffix(day['dates'])

            if len(day['dates']) == max_specific_day_in_month:
                suffixed_day_dates.append(suffixed_day_date)
                continue

            if self._should_pad_start_of_date_range(year=day['year'],
                                                    month_name_value=day['month_name_value'],
                                                    dates=day['dates']):
                suffixed_day_date.insert(0, '')
            else:
                suffixed_day_date.append('')

            suffixed_day_dates.append(suffixed_day_date)

        return suffixed_day_dates

    @staticmethod
    def _should_pad_start_of_date_range(year, month_name_value, dates):
        d = date(year, month_name_value, 1)
        first_date_from_date_range, *_ = dates
        last_day_of_first_week_in_month = timedelta(days=6 - d.weekday()).days
        return first_date_from_date_range > last_day_of_first_week_in_month

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
