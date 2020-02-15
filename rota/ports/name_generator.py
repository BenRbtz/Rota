from typing import List

from rota.domain.models.person import Instructor


class NameGeneratorPort:
    def generate(self, *args, **kwargs) -> List[Instructor]:
        pass
