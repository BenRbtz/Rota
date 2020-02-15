from datetime import date, timedelta
from typing import List

from rota.ports.formatter import RotaFormatPort
from rota.domain.models.calender import Month


class MonthTableFormatter(RotaFormatPort):
    def format_column_names(self, column_names: list, *args, **kwargs) -> list:
        formatted_column_names: List[List[str]] = []
        for column_name in column_names:
            formatted_column_names.append([''])
            formatted_column_names.append([column_name.capitalize()])

        return formatted_column_names

    def format_columns(self, rows: Month, *args, **kwargs) -> list:
        suffixed_day_dates = self._get_suffixed_day_dates(month=rows)
        month = zip(*suffixed_day_dates)

        formatted_columns: List[List[str]] = []
        for days in month:
            formatted_row: List[str] = []
            for day in days:
                formatted_row.append(day)
                formatted_row.append('')
            formatted_columns.append(formatted_row)
        return formatted_columns

    def _get_suffixed_day_dates(self, month: Month) -> List[List[str]]:
        max_specific_day_in_month = 5

        suffixed_day_dates: List[List[str]] = []
        for days in month:
            dates = days.dates(year=month.year, month_value=month.value)
            suffixed_day_date = self._format_dates_with_suffix(dates)

            if len(dates) == max_specific_day_in_month:
                suffixed_day_dates.append(suffixed_day_date)
                continue

            if self._should_pad_start_of_date_range(year=month.year, month_name_value=month.value, dates=dates):
                suffixed_day_date.insert(0, '')
            else:
                suffixed_day_date.append('')

            suffixed_day_dates.append(suffixed_day_date)

        return suffixed_day_dates

    @staticmethod
    def _should_pad_start_of_date_range(year: int, month_name_value: int, dates: list) -> bool:
        d = date(year, month_name_value, 1)
        first_date_from_date_range, *_ = dates
        last_day_of_first_week_in_month = timedelta(days=6 - d.weekday()).days
        if last_day_of_first_week_in_month == 0:
            last_day_of_first_week_in_month = 30
        return first_date_from_date_range > last_day_of_first_week_in_month

    def _format_dates_with_suffix(self, dates: List[int]) -> List[str]:
        formatted_dates: List[str] = []
        for a_date in dates:
            suffixed_date = str(self._get_day_with_suffix(a_date))
            formatted_dates.append(suffixed_date)
        return formatted_dates

    @staticmethod
    def _get_day_with_suffix(day: int) -> str:
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        return f'{day}{suffix}'
