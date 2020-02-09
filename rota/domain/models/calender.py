from datetime import date, timedelta
from operator import attrgetter
from typing import List


class Day:
    map = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6,
    }

    def __init__(self, name: str):
        self.name = name.lower()

        if self.name not in self.map:
            raise ValueError(f'\'{self.name}\' is not a valid day')

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def value(self) -> int:
        return self.map[self.name]

    def dates(self, year: int, month_value: int) -> List[int]:
        d = date(year=year, month=month_value, day=1)
        d += timedelta(days=self.value - d.weekday())

        if d.month != month_value:
            d += timedelta(days=7)

        dates: List[int] = []
        while d.month == month_value:
            dates.append(d.day)
            d += timedelta(days=7)

        return dates


class Days:
    def __init__(self, names: List[str]):
        new_days: List[Day] = []
        for name in names:
            new_days.append(Day(name=name))

        self.days = sorted(set(new_days), key=attrgetter('value'))

    def __iter__(self) -> iter:
        return iter(self.days)

    @property
    def names(self) -> List[str]:
        names: List[str] = []
        for day in self.days:
            names.append(day.name)
        return names

    def dates(self, year: int, month_value: int) -> List[List[int]]:
        dates: List[List[int]] = []
        for day in self.days:
            day_dates = day.dates(year=year, month_value=month_value)
            dates.append(day_dates)
        return dates


class Month:
    map = {
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

    def __init__(self, year: int, name: str, days: Days):
        self.year = year
        self.name = name.lower()
        self.days = days

        if self.name not in self.map:
            raise ValueError(f'\'{self.name}\' is not a valid month')

    def __iter__(self) -> iter:
        return iter(self.days)

    @property
    def value(self) -> int:
        return self.map[self.name]
