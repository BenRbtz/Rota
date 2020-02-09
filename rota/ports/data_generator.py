from collections import namedtuple

Table = namedtuple('Table', 'columns rows')


class DateGeneratorPort:
    def generate(self, *args, **kwargs) -> Table:
        pass
