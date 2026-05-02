def test_get_system_alerts(system):
    alerts = system.get_system_alerts()
    assert isinstance(alerts, list)
