from service.infrastructure.formatter import MonthTableFormatter
from service.infrastructure.output import Spreadsheet
from service.infrastructure.user_input import ArgUserInput
from service.ports.generator import MonthGenerator
from service.ports.rota import Rota

if __name__ == '__main__':
    Rota(user_input=ArgUserInput(), date_generator=MonthGenerator(), formatter=MonthTableFormatter(),
         output=Spreadsheet()).generate()
