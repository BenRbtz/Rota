from dataclasses import dataclass

from service.ports.ports import UserInputPort, DataGeneratorPort, TableFormatPort, OutputPort


@dataclass
class Rota:
    user_input: UserInputPort
    data_generator: DataGeneratorPort
    formatter: TableFormatPort
    output: OutputPort

    def generate(self, *args, **kwargs):
        user_input = self.user_input.get()

        data = self.data_generator.generate(year=user_input.year, month_name=user_input.month_name,
                                            day_names=user_input.day_names, user_input=user_input, *args, **kwargs)

        formatted_columns = self.formatter.format_column_names(column_names=data.columns, user_input=user_input,
                                                               *args, **kwargs)
        formatted_rows = self.formatter.format_columns(columns=data.columns, rows=data.rows, user_input=user_input,
                                                       *args, **kwargs)

        self.output.create(title=user_input.month_name, column_names=formatted_columns, rows=formatted_rows,
                           user_input=user_input, *args, **kwargs)
