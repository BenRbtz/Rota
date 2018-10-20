import xlsxwriter


class Spreadsheet:
    @staticmethod
    def get_grid(day_name1, day_name2, weeks):
        grid = [['', day_name1, '', day_name2]]
        for day1, day2 in weeks:
            grid.append([day1, '', day2, ''])
        return grid

    @staticmethod
    def write(file_name, month_name, grid):
        with xlsxwriter.Workbook(file_name) as workbook:
            worksheet = workbook.add_worksheet()

            merge_format = workbook.add_format({'align': 'center', 'border': 6})
            worksheet.merge_range('A1:D1', month_name, merge_format)

            column_offset = 1
            for col, row in enumerate(grid):
                worksheet.write_row(col + column_offset, 0, row, merge_format)
