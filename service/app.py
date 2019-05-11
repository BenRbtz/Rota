from service.business_logic.calender import Month
from service.infrastructure.formatter import TableFormatter
from service.infrastructure.output import Spreadsheet
from service.infrastructure.user_input import ArgUserInput
from service.ports.rota import Rota

if __name__ == '__main__':
    Rota(user_input=ArgUserInput(), data_generator=Month(), formatter=TableFormatter(),
         output=Spreadsheet()).generate()
