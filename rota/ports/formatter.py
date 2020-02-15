from rota.domain.models.calender import Month


class RotaFormatPort:
    def format_column_names(self, column_names: list) -> list:
        pass

    def format_columns(self, rows: Month) -> list:
        pass
