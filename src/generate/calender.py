from collections import OrderedDict
from datetime import date, timedelta


class Calender:
    day_map = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6,
    }

    month_map = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12,
    }

    def get_days_in_month(self, year: int, month_name: str, day_names: list):
        # NOTE make values unique
        day_names = set([day_name.lower() for day_name in day_names])
        month_name_value = self._get_month_name_value(month_name)

        month = self._get_mapped_day_names(day_names, year, month_name_value)

        return month

    def _get_mapped_day_names(self, day_names, year, month_name_value):
        mapped_day_names = {}
        for day_name in day_names:
            day_name_value = self._get_day_name_value(day_name)
            day_dates = self._get_dates(year, month=month_name_value, day_of_week=day_name_value)

            mapped_day_names[day_name_value] = {
                'day_name': day_name.capitalize(),
                'dates': day_dates,
                'month_name_value': month_name_value,
                'year': year
            }

        sorted_mapped_day_names = OrderedDict(sorted(mapped_day_names.items()))

        return sorted_mapped_day_names

    def _get_day_name_value(self, day_name):
        day_name = day_name.lower()
        if day_name not in self.day_map:
            raise ValueError(f"Day name '{day_name}' not valid")
        return self.day_map[day_name]

    def _get_month_name_value(self, month_name):
        month_name = month_name.lower()
        if month_name not in self.month_map:
            raise ValueError(f"Month name '{month_name}' not valid")
        return self.month_map[month_name]

    @staticmethod
    def _get_dates(year, month, day_of_week):
        d = date(year, month, 1)
        d += timedelta(days=day_of_week - d.weekday())

        if d.month < month:
            d += timedelta(days=7)

        dates = []
        while d.month == month:
            dates.append(d.day)
            d += timedelta(days=7)

        return dates
