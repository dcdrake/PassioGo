def test_get_all_routes(system):
    routes = system.get_routes()
    assert isinstance(routes, list)
