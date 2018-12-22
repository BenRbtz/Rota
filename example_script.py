from generate import calender, spreadsheet, rota

my_spreadsheet = spreadsheet.Spreadsheet()
my_calender = calender.Calender()
my_rota = rota.Rota(my_calender, my_spreadsheet)

my_rota.run('rota.xlsx', 2019, 'January', 'Tuesday', 'Friday')
