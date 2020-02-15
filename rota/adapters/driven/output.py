from xlsxwriter import Workbook

from rota.ports.output import OutputPort


class Spreadsheet(OutputPort):
    def create(self, title: str, column_names: list, rows: list, *args, **kwargs):
        file_name = kwargs['user_input'].file_name
        with Workbook(filename=file_name) as workbook:
            worksheet = workbook.add_worksheet()
            first_row = 0
            last_row = first_row
            first_col = 0
            last_col = len(column_names) - 1
            cell_format = workbook.add_format({'align': 'center', 'border': 6})

            worksheet.merge_range(first_row=first_row, first_col=first_col, last_row=last_row, last_col=last_col,
                                  data=title, cell_format=cell_format)

            row_offset = 1
            column_offset = 0
            for index, column_name in enumerate(column_names):
                worksheet.write_row(row=row_offset, col=column_offset + index, data=column_name,
                                    cell_format=cell_format)

            row_offset = 2
            column_offset = 0
            for index, row in enumerate(rows):
                worksheet.write_row(row=row_offset + index, col=column_offset, data=row,
                                    cell_format=cell_format)
