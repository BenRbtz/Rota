import pytest

from rota.adapters.driven.generator import MonthGenerator
from rota.ports.data_generator import Table


class TestMonthGenerator:
    @pytest.fixture()
    def month(self):
        return MonthGenerator()

    def test_generate(self, month):
        day_names = ['tuesday', 'friday']
        month = month.generate(year=2018, month_name='January', day_names=day_names)
        assert type(month) is Table
        assert month.columns == day_names
        assert month.rows.name == 'january'
        assert month.rows.year == 2018
