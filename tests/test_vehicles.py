def test_get_vehicles(system):
    vehicles = system.get_vehicles()
    assert isinstance(vehicles, list)
