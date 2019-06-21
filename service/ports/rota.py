from service.ports.ports import UserInputPort, DateGeneratorPort, RotaFormatPort, OutputPort


class Rota:
    def __init__(self, user_input: UserInputPort, date_generator: DateGeneratorPort, formatter: RotaFormatPort,
                 output: OutputPort):
        self.user_input = user_input
        self.date_generator = date_generator
        self.formatter = formatter
        self.output = output

    def generate(self, *args, **kwargs):
        user_input = self.user_input.get()

        dates = self.date_generator.generate(year=user_input.year, month_name=user_input.month_name,
                                             day_names=user_input.day_names, user_input=user_input, *args, **kwargs)

        formatted_columns = self.formatter.format_column_names(column_names=dates.columns, user_input=user_input,
                                                               *args, **kwargs)
        formatted_rows = self.formatter.format_columns(columns=dates.columns, rows=dates.rows, user_input=user_input,
                                                       *args, **kwargs)

        self.output.create(title=user_input.month_name, column_names=formatted_columns, rows=formatted_rows,
                           user_input=user_input, *args, **kwargs)
