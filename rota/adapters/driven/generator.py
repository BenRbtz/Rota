from csv import DictReader
from typing import List

from ports.data_generator import DateGeneratorPort, Table
from ports.name_generator import NameGeneratorPort
from rota.domain.models.calender import Days, Month
from rota.domain.models.person import Instructor


class NamesGenerator(NameGeneratorPort):
    fields = {'name', 'preferred_days', 'teach'}

    def generate(self, *args, **kwargs) -> List[Instructor]:
        file_path: str = kwargs['instructor_names_file_path']
        instructors = self._get_instructors(file_path=file_path)
        return instructors

    def _get_instructors(self, file_path) -> List[Instructor]:
        with open(file=file_path, mode='r') as csv_file:
            csv = DictReader(csv_file, delimiter=',', quotechar='|')

            if not self.fields.issubset(set(csv.fieldnames)):
                raise KeyError('CSV fieldnames not match expected fieldnames')

            instructors: List[Instructor] = []
            for row in csv:
                days = row['preferred_days'].split(';')
                teach = row['teach']

                if teach:
                    teach = int(teach)
                else:
                    teach = None

                instructors.append(Instructor(name=row['name'], preferred_days=days,
                                              teach=teach))
        return instructors


class MonthGenerator(DateGeneratorPort):
    def generate(self, *args, **kwargs) -> Table:
        year = kwargs['year']
        month_name = kwargs['month_name']
        day_names = kwargs['day_names']

        days = Days(names=day_names)
        month = Month(year=year, name=month_name, days=days)

        return Table(columns=days.names, rows=month)
