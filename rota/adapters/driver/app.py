from rota.adapters.driven.formatter import MonthTableFormatter
from rota.adapters.driven.generator import MonthGenerator
from rota.adapters.driven.output import Spreadsheet
from rota.adapters.driven.user_input import UserInputArg
from rota.domain.rota import Rota

rota = Rota(user_input=UserInputArg(), date_generator=MonthGenerator(), formatter=MonthTableFormatter(),
            output=Spreadsheet())

if __name__ == '__main__':
    rota.generate()
