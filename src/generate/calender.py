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

    def get_days_in_month(self, year, month_name, day_name1, day_name2):
        day_name_value1 = self.get_day_name_value(day_name1)
        day_name_value2 = self.get_day_name_value(day_name2)

        if day_name_value1 >= day_name_value2:
            raise ValueError(f'First day provided must be before the second day.')

        month_name_value = self.get_month_name_value(month_name)

        day_dates1 = self.get_date(year, month=month_name_value, day_of_week=day_name_value1)
        day_dates2 = self.get_date(year, month=month_name_value, day_of_week=day_name_value2)

        day_num1 = len(day_dates1)
        day_num2 = len(day_dates2)

        if day_num1 < day_num2:
            day_dates1.insert(0, '')

        if day_num1 > day_num2:
            day_dates2.append('')

        weeks = (zip(day_dates1, day_dates2))

        return weeks

    def get_day_name_value(self, day_name):
        day_name = day_name.lower()
        if day_name in self.day_map:
            return self.day_map[day_name]
        else:
            raise ValueError(f"Day name '{day_name}' not valid")

    def get_month_name_value(self, month_name):
        month_name = month_name.lower()
        if month_name not in self.month_map:
            raise ValueError(f"Month name '{month_name}' not valid")
        return self.month_map[month_name]

    def get_date(self, year, month, day_of_week):
        d = date(year, month, 1)
        d += timedelta(days=day_of_week - d.weekday())

        if d.month < month:
            d += timedelta(days=7)

        dates = []
        while d.month == month:
            formatted_day = str(self.get_day_with_suffix(d.day))
            dates.append(formatted_day)
            d += timedelta(days=7)

        return dates

    @staticmethod
    def get_day_with_suffix(day):
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        return f'{day}{suffix}'
