from typing import List

from domain.models.person import Instructor


class NameGeneratorPort:
    def generate(self, *args, **kwargs) -> List[Instructor]:
        pass
