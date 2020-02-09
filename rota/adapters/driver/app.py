from adapters.driven.formatter import MonthTableFormatter
from adapters.driven.generator import MonthGenerator
from adapters.driven.output import Spreadsheet
from adapters.driven.user_input import UserInputArg
from rota.domain.rota import Rota

rota = Rota(user_input=UserInputArg(), date_generator=MonthGenerator(), formatter=MonthTableFormatter(),
            output=Spreadsheet())

if __name__ == '__main__':
    rota.generate()
