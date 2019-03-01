from collections import OrderedDict

import pytest

from generate.spreadsheet import Spreadsheet


class TestSpreadsheet:
    @pytest.fixture()
    def generate(self):
        return Spreadsheet()

    def test_get_grid(self, generate, mocker):
        header = ['', 'monday', '', 'tuesday']
        suffixed_dates = [
            ['1st', '7th'],
            ['2nd', '8th']
        ]
        mocker.patch.object(generate, '_get_header', return_value=header)
        mocker.patch.object(generate, '_get_suffixed_day_dates', return_value=suffixed_dates)

        expected = [
            ['', 'monday', '', 'tuesday'],
            ['1st', '', '2nd', ''],
            ['7th', '', '8th', '']
        ]
        actual = generate.get_grid([])
        assert expected == actual

    def test_get_header(self, generate):
        month = OrderedDict({
            1: {'day_name': 'monday'},
            2: {'day_name': 'tuesday'}
        })

        expected = ['', 'monday', '', 'tuesday']
        actual = generate._get_header(month)

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
    def test_get_suffixed_day_dates(self, generate, month, expected):
        actual = generate._get_suffixed_day_dates(month)
        assert expected == actual

    def test_format_date_with_suffix(self, generate):
        expected = ['1st', '2nd', '3rd', '4th', '30th']
        input_list = [1, 2, 3, 4, 30]
        actual = generate._format_dates_with_suffix(input_list)
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
    def test_get_day_with_suffix(self, generate, day_num, expected):
        actual = generate._get_day_with_suffix(day_num)
        assert expected == actual

    def test_write_to_xlsm(self):
        pass
