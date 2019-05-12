from unittest.mock import Mock

import pytest

from service.business_logic import calender


class TestDay:
    def test__init_when_invalid(self):
        with pytest.raises(ValueError) as error_info:
            calender.Day(name='Fakeday')
        assert '\'fakeday\' is not a valid day' in str(error_info.value)

    def test__eq_when_equal(self):
        day1 = calender.Day(name='Monday')
        day2 = calender.Day(name='Monday')
        assert day1 == day2

    def test__eq_when_not_equal(self):
        day1 = calender.Day(name='Monday')
        day2 = calender.Day(name='Tuesday')
        assert day1 != day2

    def test_support_hash(self):
        day1 = calender.Day(name='Monday')
        day2 = calender.Day(name='Monday')
        days = {day1, day2}
        assert days == {day1}

    def test_name(self):
        assert calender.Day(name='Monday').name == 'monday'

    @pytest.mark.parametrize('name, expected', [
        ('Monday', 0),
        ('Tuesday', 1),
        ('Wednesday', 2),
        ('Thursday', 3),
        ('Friday', 4),
        ('Saturday', 5),
        ('Sunday', 6),
    ])
    def test_value(self, name, expected):
        assert calender.Day(name=name).value == expected

    @pytest.mark.parametrize('year, month_value, day_name, expected', [
        (2019, 1, 'Monday', [7, 14, 21, 28]),
        (2019, 1, 'Tuesday', [1, 8, 15, 22, 29]),
        (2019, 2, 'Tuesday', [5, 12, 19, 26]),
    ])
    def test_dates(self, year, month_value, day_name, expected):
        assert calender.Day(name=day_name).dates(year=year, month_value=month_value) == expected


class TestDays:
    def test_init_when_string_list_given(self):
        calender.Days(names=['Monday', 'Tuesday'])

    def test_iter(self):
        expected = ['tuesday', 'monday']
        days = calender.Days(names=expected)
        assert hasattr(days, '__iter__')
        for day in days:
            assert day.name == expected.pop()

        assert not expected

    def test_names(self):
        expected = ['monday', 'tuesday']
        assert calender.Days(names=['Tuesday', 'Monday']).names == expected

    def test_dates(self):
        expected = [
            [7, 14, 21, 28],
            [1, 8, 15, 22, 29]
        ]
        assert calender.Days(names=['Tuesday', 'Monday']).dates(year=2019, month_value=1) == expected


class TestMonth:
    def test_init_when_invalid_month(self):
        with pytest.raises(ValueError) as error_info:
            calender.Month(year=2019, name='FakeMonth', days=Mock())
        assert '\'fakemonth\' is not a valid month' in str(error_info.value)

    def test_iter(self):
        expected = ['tuesday', 'monday']
        days = calender.Month(year=2019, name='January', days=calender.Days(names=['Tuesday', 'Monday']))
        assert hasattr(days, '__iter__')
        for day in days:
            assert day.name == expected.pop()

        assert not expected

    def test_name(self):
        expected = 'january'
        assert calender.Month(year=2019, name='January', days=Mock()).name == expected

    @pytest.mark.parametrize('name, expected', [
        ('January', 1),
        ('February', 2),
        ('March', 3),
        ('April', 4),
        ('May', 5),
        ('June', 6),
        ('July', 7),
        ('August', 8),
        ('September', 9),
        ('October', 10),
        ('November', 11),
        ('December', 12),
    ])
    def test_value(self, name, expected):
        calender.Month(year=2019, name=name, days=Mock())


class TestMonthGenerator:
    @pytest.fixture()
    def month(self):
        return calender.MonthGenerator()

    def test_generate(self, month):
        day_names = ['tuesday', 'friday']
        month = month.generate(year=2018, month_name='January', day_names=day_names)
        assert type(month) is calender.DataGeneratorPort.Table
        assert month.columns == day_names
        assert month.rows.name == 'january'
        assert month.rows.year == 2018
