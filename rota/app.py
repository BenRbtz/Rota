from rota.adapters.formatter import MonthTableFormatter
from rota.adapters.generator import MonthGenerator
from rota.adapters.output import Spreadsheet
from rota.adapters.user_input import ArgUserInput
from rota.domain.rota import Rota

rota = Rota(user_input=ArgUserInput(), date_generator=MonthGenerator(), formatter=MonthTableFormatter(),
            output=Spreadsheet())

if __name__ == '__main__':
    rota.generate()
