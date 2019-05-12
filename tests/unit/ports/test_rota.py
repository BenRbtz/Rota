import pytest

from service.ports.rota import Rota


class TestRota:
    @pytest.fixture()
    def rota(self):
        return Rota

    def test_generate(self, rota):
        pass
