import pytest

from service.business_logic.person import Instructor
from service.ports.generator import NamesGenerator, MonthGenerator
from service.ports.ports import DateGeneratorPort


class TestMonthGenerator:
    @pytest.fixture()
    def month(self):
        return MonthGenerator()

    def test_generate(self, month):
        day_names = ['tuesday', 'friday']
        month = month.generate(year=2018, month_name='January', day_names=day_names)
        assert type(month) is DateGeneratorPort.Table
        assert month.columns == day_names
        assert month.rows.name == 'january'
        assert month.rows.year == 2018


class TestNamesGenerator:
    def test_get_names(self, tmp_path):
        file = tmp_path / 'test.csv'
        content = 'name,preferred_days,teach\nname1,tuesday,\nname2,monday;friday,1'
        file.write_text(content)

        expected = [Instructor(name='name1', preferred_days=['tuesday'], teach=None),
                    Instructor(name='name2', preferred_days=['monday', 'friday'], teach=1)]
        assert NamesGenerator().generate(instructor_names_file_path=str(file)) == expected

    def test_get_names_with_wrong_csv_field_names(self, tmp_path):
        file = tmp_path / 'test.csv'
        content = 'name,teach\nname1,tuesday,\nname2,monday;friday,1'
        file.write_text(content)

        with pytest.raises(KeyError) as error_info:
            NamesGenerator().generate(instructor_names_file_path=str(file))

        assert 'CSV fieldnames not match expected fieldnames' in str(error_info.value)
