import pytest

from generate.calender import Calender


class TestCalender:
    @pytest.fixture()
    def generate(self):
        return Calender()

    @pytest.mark.parametrize('month_name, expected', [
        ('January', [
            ('2nd', '5th'),
            ('9th', '12th'),
            ('16th', '19th'),
            ('23rd', '26th'),
            ('30th', '')
        ]),
        ('november', [
            ('', '2nd'),
            ('6th', '9th'),
            ('13th', '16th'),
            ('20th', '23rd'),
            ('27th', '30th')
        ]),
    ])
    def test_get_days_in_month(self, generate, month_name, expected):
        actual = list(generate.get_days_in_month(2018, month_name, 'tuesday', 'friday'))
        assert expected == actual

    def test_get_days_in_month_when_day_names_in_wrong_order(self, generate):
        with pytest.raises(ValueError) as err_info:
            generate.get_days_in_month(2018, 'January', 'tuesday', 'monday')
        expected = 'First day provided must be before the second day.'
        assert expected == str(err_info.value)

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
        actual = generate.get_day_name_value(day_name)
        assert expected == actual

    def test_get_day_name_value_when_invalid(self, generate):
        with pytest.raises(ValueError) as err_info:
            generate.get_day_name_value('wrong_val')
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
        actual = generate.get_month_name_value(day_name)
        assert expected == actual

    def test_get_month_name_value_when_invalid(self, generate):
        with pytest.raises(ValueError) as err_info:
            generate.get_month_name_value('wrong_val')
        expected = "Month name 'wrong_val' not valid"
        assert expected == str(err_info.value)

    def test_get_date(self, generate):
        expected = ['6th', '13th', '20th', '27th']
        actual = generate.get_date(2018, 11, 8)
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
        actual = generate.get_day_with_suffix(day_num)
        assert expected == actual
