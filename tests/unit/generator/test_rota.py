import pytest

from generate.rota import Rota


class TestRota:
    @pytest.fixture()
    def generate(self):
        return Rota

    def test_run(self):
        pass
