import pytest

import passiogo


def pytest_generate_tests(metafunc):
    if "system" in metafunc.fixturenames:
        all_systems = passiogo.get_systems()
        ids = [f"{s.name} (#{s.id})" for s in all_systems]
        metafunc.parametrize("system", all_systems, ids=ids)


@pytest.fixture(scope="session")
def all_systems():
    return passiogo.get_systems()
