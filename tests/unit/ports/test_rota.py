import pytest

from service.ports.rota import Rota


class TestRota:
    @pytest.fixture()
    def generate(self):
        return Rota

    def test_parse_args(self):
        pass

    def test_generate(self):
        pass
