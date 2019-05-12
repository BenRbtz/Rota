from service.business_logic.calender import MonthGenerator
from service.infrastructure.formatter import MonthTableFormatter
from service.infrastructure.output import Spreadsheet
from service.infrastructure.user_input import ArgUserInput
from service.ports.rota import Rota

if __name__ == '__main__':
    Rota(user_input=ArgUserInput(), data_generator=MonthGenerator(), formatter=MonthTableFormatter(),
         output=Spreadsheet()).generate()
