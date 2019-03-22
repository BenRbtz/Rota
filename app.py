from generate.calender import Calender
from generate.rota import Rota
from generate.spreadsheet import Spreadsheet

Rota(Calender(), Spreadsheet()).generate()
