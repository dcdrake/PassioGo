def test_get_all_stops(system):
    stops = system.get_stops()
    assert isinstance(stops, list)
