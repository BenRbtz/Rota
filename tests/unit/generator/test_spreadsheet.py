import pytest

from generate.spreadsheet import Spreadsheet


class TestSpreadsheet:
    @pytest.fixture()
    def generate(self):
        return Spreadsheet

    def test_get_grid(self, generate):
        expected = [
            ['', 'Tuesday', '', 'Friday'],
            ['1', '', '2', ''],
            ['3', '', '4', '']
        ]
        actual = generate.get_grid('Tuesday', 'Friday', [('1', '2'), ('3', '4')])
        assert expected == actual

    def test_write_to_xlsm(self):
        pass
