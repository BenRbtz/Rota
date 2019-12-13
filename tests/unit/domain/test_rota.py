import pytest

from rota.domain.rota import Rota


class TestRota:
    @pytest.fixture()
    def rota(self):
        return Rota

    def test_generate(self, rota):
        pass
