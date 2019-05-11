from collections import OrderedDict
from typing import List
from unittest.mock import Mock

import pytest

from service.infrastructure.formatter import TableFormatter


class TestTableFormatter:
    @pytest.fixture()
    def formatter(self):
        return TableFormatter()

    def test_format_column_names(self, formatter):
        expected: List[str] = ['', 'Tuesday', '', 'Friday']
        actual = formatter.format_column_names(['tuesday', 'friday'])
        assert actual == expected

    def test_format_columns(self, monkeypatch, formatter):
        mock_get_suffixed_day_dates = Mock(return_value=[
            ['1st', '7th'],
            ['2nd', '8th']
        ])
        monkeypatch.setattr(target=formatter, name='_get_suffixed_day_dates', value=mock_get_suffixed_day_dates)

        expected = (
            [
                ['1st', '', '2nd', ''],
                ['7th', '', '8th', '']
            ]
        )
        actual = formatter.format_columns([])
        assert expected == actual

    @pytest.mark.parametrize('month, expected', [
        (OrderedDict({
            1: {
                'dates': [5, 12, 19, 26],
                'day_name': 'Tuesday',
                'month_name_value': 2,
                'suffixed_day_dates': ['5th', '12th', '19th', '26th'],
                'year': 2019
            },
            4: {
                'dates': [1, 8, 15, 22],
                'day_name': 'Friday',
                'month_name_value': 2,
                'suffixed_day_dates': ['1st', '8th', '15th', '22nd'],
                'year': 2019
            }
        }), [
             ['', '5th', '12th', '19th', '26th'],
             ['1st', '8th', '15th', '22nd', '']
         ]),
        (OrderedDict({
            1: {
                'dates': [1, 8, 15, 22, 29],
                'day_name': 'Tuesday',
                'month_name_value': 2,
                'suffixed_day_dates': ['1st', '8th', '15th', '22nd', '29th'],
                'year': 2019
            },
        }), [
             ['1st', '8th', '15th', '22nd', '29th']
         ]),
    ])
    def test_get_suffixed_day_dates(self, formatter, month, expected):
        actual = formatter._get_suffixed_day_dates(month)
        assert expected == actual

    @pytest.mark.parametrize('year, month_name_value, dates, expected', [
        (2019, 2, [5, 12, 19, 26], True),
        (2019, 2, [1, 8, 15, 22, 29], False)
    ])
    def test_should_pad_start_of_date_range(self, formatter, year, month_name_value, dates, expected):
        actual = formatter._should_pad_start_of_date_range(year=year, month_name_value=month_name_value, dates=dates)
        assert actual == expected

    def test_format_date_with_suffix(self, formatter):
        expected = ['1st', '2nd', '3rd', '4th', '30th']
        input_list = [1, 2, 3, 4, 30]
        actual = formatter._format_dates_with_suffix(input_list)
        assert expected == actual

    @pytest.mark.parametrize('day_num, expected', [
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
        (5, '5th'),
        (6, '6th'),
        (7, '7th'),
        (8, '8th'),
        (9, '9th'),
        (10, '10th'),
        (11, '11th'),
        (12, '12th'),
        (13, '13th'),
        (14, '14th'),
        (15, '15th'),
        (16, '16th'),
        (17, '17th'),
        (18, '18th'),
        (19, '19th'),
        (20, '20th'),
        (21, '21st'),
        (22, '22nd'),
        (23, '23rd'),
        (24, '24th'),
    ])
    def test_get_day_with_suffix(self, formatter, day_num, expected):
        actual = formatter._get_day_with_suffix(day_num)
        assert expected == actual
