from collections import OrderedDict
from unittest.mock import Mock

import pytest

from service.business_logic import calender


class TestMonth:
    @pytest.fixture()
    def month(self):
        return calender.Month()

    @pytest.mark.parametrize('expected', [
        (calender.DataGeneratorPort.Table(columns={'tuesday', 'friday'},
                                          rows={1: {'dates:': {}, 'month_name_value': 1, 'year': 2018}})),
        (calender.DataGeneratorPort.Table(columns={'tuesday', 'friday'},
                                          rows={1: {'dates:': {}, 'month_name_value': 1, 'year': 2018}})),
        (calender.DataGeneratorPort.Table(columns={'tuesday', 'friday'},
                                          rows={1: {'dates:': {}, 'month_name_value': 1, 'year': 2018}})),
    ])
    def test_generate(self, monkeypatch, month, expected):
        get_valid_day_names = Mock(return_value=expected.columns)
        mock_get_mapped_day_names = Mock(return_value=expected.rows)

        monkeypatch.setattr(target=calender, name='get_valid_day_names', value=get_valid_day_names)
        monkeypatch.setattr(target=calender, name='get_mapped_day_names', value=mock_get_mapped_day_names)

        actual = month.generate(year=2018, month_name='January', day_names=['tuesday', 'friday'])

        assert actual == expected


@pytest.mark.parametrize('day_names, expected', [
    (['tuesday', 'friday'], {'tuesday', 'friday'}),
    (['Friday', 'tuesday', 'friday'], {'tuesday', 'friday'}),
])
def test_get_valid_day_names(day_names, expected):
    actual = calender.get_valid_day_names(day_names=day_names)
    assert actual == expected


def test_get_mapped_day_names():
    year = 2019
    month_name = 'February'
    day_names = ['Tuesday', 'Friday']
    expected = OrderedDict({
        1: {
            'dates': [5, 12, 19, 26],
            'month_name_value': 2,
            'year': 2019
        },
        4: {
            'dates': [1, 8, 15, 22],
            'month_name_value': 2,
            'year': 2019
        }
    })
    actual = calender.get_mapped_day_names(year=year, month_name=month_name, day_names=day_names)
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
def test_get_day_name_value(expected, day_name):
    actual = calender.get_day_name_value(day_name)
    assert expected == actual


def test_get_day_name_value_when_invalid():
    with pytest.raises(ValueError) as err_info:
        calender.get_day_name_value('wrong_val')
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
def test_get_month_name_value(expected, day_name):
    actual = calender.get_month_name_value(day_name)
    assert expected == actual


def test_get_month_name_value_when_invalid():
    with pytest.raises(ValueError) as err_info:
        calender.get_month_name_value('wrong_val')
    expected = "Month name 'wrong_val' not valid"
    assert expected == str(err_info.value)


def test_get_dates():
    expected = [6, 13, 20, 27]
    actual = calender.get_dates(2018, 11, 8)
    assert expected == actual
