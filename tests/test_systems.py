import passiogo


def test_get_all_systems(all_systems):
    assert isinstance(all_systems, list)
    assert len(all_systems) > 0


def test_print_all_systems(all_systems):
    passiogo.print_all_systems_md()


def test_get_system_from_id():
    system = passiogo.get_system_from_id(1068)
    assert system is not None
    assert system.id == 1068
