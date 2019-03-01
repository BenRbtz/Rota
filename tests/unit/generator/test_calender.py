from collections import OrderedDict

import pytest

from generate.calender import Calender


class TestCalender:
    @pytest.fixture()
    def generate(self):
        return Calender()

    @pytest.mark.parametrize('year, month_name, day_names, expected', [
        (2018, 'January', ['tuesday', 'friday'], [
            {'tuesday', 'friday'},
            2018,
            1
        ]),
        (2018, 'november', ['tuesday', 'friday', 'Friday'], [
            {'tuesday', 'friday'},
            2018,
            11
        ]),
        (2019, 'february', ['friday', 'tuesday'], [
            {'friday', 'tuesday'},
            2019,
            2
        ]),
    ])
    def test_get_days_in_month(self, generate, mocker, year, month_name, day_names, expected):
        mocker.patch.object(generate, '_get_mapped_day_names')
        generate.get_days_in_month(year, month_name, day_names)
        generate._get_mapped_day_names.assert_called_once_with(*expected)

    def test_get_mapped_day_names(self, generate):
        year = 2019
        month_value = 2
        day_names = ['Tuesday', 'Friday']
        expected = OrderedDict({
            1: {
                'dates': [5, 12, 19, 26],
                'day_name': 'Tuesday',
                'month_name_value': 2,
                'year': 2019
            },
            4: {
                'dates': [1, 8, 15, 22],
                'day_name': 'Friday',
                'month_name_value': 2,
                'year': 2019
            }
        })
        actual = generate._get_mapped_day_names(day_names, year, month_value)
        assert expected == actual

    @pytest.mark.parametrize('expected, day_name', [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ])
    def test_get_day_name_value(self, generate, expected, day_name):
        actual = generate._get_day_name_value(day_name)
        assert expected == actual

    def test_get_day_name_value_when_invalid(self, generate):
        with pytest.raises(ValueError) as err_info:
            generate._get_day_name_value('wrong_val')
        expected = "Day name 'wrong_val' not valid"
        assert expected == str(err_info.value)

    @pytest.mark.parametrize('expected, day_name', [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ])
    def test_get_month_name_value(self, generate, expected, day_name):
        actual = generate._get_month_name_value(day_name)
        assert expected == actual

    def test_get_month_name_value_when_invalid(self, generate):
        with pytest.raises(ValueError) as err_info:
            generate._get_month_name_value('wrong_val')
        expected = "Month name 'wrong_val' not valid"
        assert expected == str(err_info.value)

    def test_get_dates(self, generate):
        expected = [6, 13, 20, 27]
        actual = generate._get_dates(2018, 11, 8)
        assert expected == actual
