from collections import OrderedDict
from datetime import date, timedelta

from service.ports.ports import DataGeneratorPort

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


class Month(DataGeneratorPort):
    def generate(self, *args, **kwargs) -> DataGeneratorPort.Table:
        year = kwargs['year']
        month_name = kwargs['month_name']
        day_names = kwargs['day_names']

        day_names = get_valid_day_names(day_names=day_names)

        month = get_mapped_day_names(year=year, month_name=month_name, day_names=day_names)

        return DataGeneratorPort.Table(columns=day_names, rows=month)


def get_valid_day_names(day_names):
    return set([day_name.lower() for day_name in day_names])


def get_mapped_day_names(year, month_name, day_names):
    month_name_value = get_month_name_value(month_name)

    mapped_day_names = {}
    for day_name in day_names:
        day_name_value = get_day_name_value(day_name)
        day_dates = get_dates(year, month=month_name_value, day_of_week=day_name_value)

        mapped_day_names[day_name_value] = {
            'dates': day_dates,
            'month_name_value': month_name_value,
            'year': year
        }

    sorted_mapped_day_names = OrderedDict(sorted(mapped_day_names.items()))

    return sorted_mapped_day_names


def get_month_name_value(month_name):
    month_name = month_name.lower()
    if month_name not in month_map:
        raise ValueError(f"Month name '{month_name}' not valid")
    return month_map[month_name]


def get_day_name_value(day_name):
    day_name = day_name.lower()
    if day_name not in day_map:
        raise ValueError(f"Day name '{day_name}' not valid")
    return day_map[day_name]


def get_dates(year, month, day_of_week):
    d = date(year, month, 1)
    d += timedelta(days=day_of_week - d.weekday())

    if d.month < month:
        d += timedelta(days=7)

    dates = []
    while d.month == month:
        dates.append(d.day)
        d += timedelta(days=7)

    return dates
