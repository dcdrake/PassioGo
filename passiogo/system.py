from ._client import BASE_URL, send_api_request, to_int_incl_none
from .alert import SystemAlert
from .route import Route
from .stop import Stop
from .vehicle import Vehicle


class TransportationSystem:
    def __init__(
        self,
        id: int,
        name: str = None,
        username: str = None,
        go_agency_name: str = None,
        email: str = None,
        go_test_mode: bool = None,
        name2: bool = None,
        homepage: str = None,
        logo: bool = None,
        go_route_planner_enabled: bool = None,
        go_color: str = None,
        go_support_email: str = None,
        go_shared_code: int = None,
        go_authentication_type: bool = None,
    ):
        self.id = id
        self.name = name
        self.username = username
        self.go_agency_name = go_agency_name
        self.email = email
        self.go_test_mode = go_test_mode
        self.name2 = name2
        self.homepage = homepage
        self.logo = logo
        self.go_route_planner_enabled = go_route_planner_enabled
        self.go_color = go_color
        self.go_support_email = go_support_email
        self.go_shared_code = go_shared_code
        self.go_authentication_type = go_authentication_type

        self._check_types()

    def _check_types(self):
        assert isinstance(self.id, int), f"'id' parameter must be an int not {type(self.id)}"
        assert self.name is None or isinstance(self.name, str), (
            f"'name' parameter must be a str not {type(self.name)}"
        )
        assert self.username is None or isinstance(self.username, str), (
            f"'username' parameter must be a str not {type(self.username)}"
        )
        assert self.go_agency_name is None or isinstance(self.go_agency_name, str), (
            f"'go_agency_name' parameter must be a str not {type(self.go_agency_name)}"
        )
        assert self.email is None or isinstance(self.email, str), (
            f"'email' parameter must be a str not {type(self.email)}"
        )
        assert self.go_test_mode is None or isinstance(self.go_test_mode, bool), (
            f"'go_test_mode' parameter must be a bool not {type(self.go_test_mode)}"
        )
        assert self.name2 is None or isinstance(self.name2, bool), (
            f"'name2' parameter must be a bool not {type(self.name2)}"
        )
        assert self.homepage is None or isinstance(self.homepage, str), (
            f"'homepage' parameter must be a str not {type(self.homepage)}"
        )
        assert self.logo is None or isinstance(self.logo, bool), (
            f"'logo' parameter must be a bool not {type(self.logo)}"
        )
        assert self.go_route_planner_enabled is None or isinstance(
            self.go_route_planner_enabled, bool
        ), (
            f"'go_route_planner_enabled' parameter must be a bool not "
            f"{type(self.go_route_planner_enabled)}"
        )
        assert self.go_color is None or isinstance(self.go_color, str), (
            f"'go_color' parameter must be a str not {type(self.go_color)}"
        )
        assert self.go_support_email is None or isinstance(self.go_support_email, str), (
            f"'go_support_email' parameter must be a str not {type(self.go_support_email)}"
        )
        assert self.go_shared_code is None or isinstance(self.go_shared_code, int), (
            f"'go_shared_code' parameter must be an int not {type(self.go_shared_code)}"
        )
        assert self.go_authentication_type is None or isinstance(
            self.go_authentication_type, bool
        ), (
            f"'go_authentication_type' parameter must be a bool not "
            f"{type(self.go_authentication_type)}"
        )

    def get_routes(self, app_version=1, amount=1) -> list[Route]:
        url = BASE_URL + f"/mapGetData.php?getRoutes={app_version}"
        body = {"systemSelected0": str(self.id), "amount": amount}
        routes = send_api_request(url, body)

        if routes is None:
            return None

        if "all" in routes:
            routes = routes["all"]

        possible_keys = [
            "id",
            "groupId",
            "groupColor",
            "name",
            "shortName",
            "nameOrig",
            "fullname",
            "myid",
            "mapApp",
            "archive",
            "goPrefixRouteName",
            "goShowSchedule",
            "outdated",
            "distance",
            "latitude",
            "longitude",
            "timezone",
            "serviceTime",
            "serviceTimeShort",
        ]

        all_routes = []
        for route in routes:
            for key in possible_keys:
                if key not in route:
                    route[key] = None

            all_routes.append(
                Route(
                    id=route["id"],
                    group_id=route["groupId"],
                    group_color=route["groupColor"],
                    name=route["name"],
                    short_name=route["shortName"],
                    name_orig=route["nameOrig"],
                    fullname=route["fullname"],
                    myid=route["myid"],
                    map_app=route["mapApp"],
                    archive=route["archive"],
                    go_prefix_route_name=route["goPrefixRouteName"],
                    go_show_schedule=route["goShowSchedule"],
                    outdated=route["outdated"],
                    distance=route["distance"],
                    latitude=route["latitude"],
                    longitude=route["longitude"],
                    timezone=route["timezone"],
                    service_time=route["serviceTime"],
                    service_time_short=route["serviceTimeShort"],
                    system_id=int(route["userId"]),
                    system=self,
                )
            )

        return all_routes

    def get_stops(self, app_version=2, s_a=1, raw=False) -> list[Stop]:
        url = BASE_URL + "/mapGetData.php?getStops=" + str(app_version)
        body = {"s0": str(self.id), "sA": s_a}
        stops = send_api_request(url, body)

        if raw:
            return stops

        if stops is None:
            return None

        if stops["routes"] == []:
            stops["routes"] = {}

        if stops["stops"] == []:
            stops["stops"] = {}

        routes_and_stops = {}
        for route_id, route in stops["routes"].items():
            routes_and_stops[route_id] = []
            for stop in route[2:]:
                if stop == 0:
                    continue
                routes_and_stops[route_id].append(stop[1])

        all_stops = []
        for _id, stop in stops["stops"].items():
            routes_and_positions = {}
            for route_id in routes_and_stops:
                if stop["id"] not in routes_and_stops[route_id]:
                    continue
                routes_and_positions[route_id] = [
                    i for i, x in enumerate(routes_and_stops[route_id]) if x == stop["id"]
                ]

            for key in ["userId", "radius"]:
                if key not in stop:
                    stop[key] = None

            all_stops.append(
                Stop(
                    id=stop["id"],
                    routes_and_positions=routes_and_positions,
                    system_id=None if stop["userId"] is None else int(stop["userId"]),
                    name=stop["name"],
                    latitude=stop["latitude"],
                    longitude=stop["longitude"],
                    radius=stop["radius"],
                    system=self,
                )
            )

        return all_stops

    def get_system_alerts(self, app_version=1, amount=1, routes_amount=0) -> list[SystemAlert]:
        url = BASE_URL + f"/goServices.php?getAlertMessages={app_version}"
        body = {
            "systemSelected0": str(self.id),
            "amount": amount,
            "routesAmount": routes_amount,
        }
        error_msgs = send_api_request(url, body)

        if error_msgs is None:
            return None

        all_alerts = []
        for msg in error_msgs["msgs"]:
            all_alerts.append(
                SystemAlert(
                    id=msg["id"],
                    system_id=msg["userId"],
                    system=self,
                    route_id=msg["routeId"],
                    name=msg["name"],
                    html=msg["html"],
                    archive=msg["archive"],
                    important=msg["important"],
                    date_time_created=msg["created"],
                    date_time_from=msg["from"],
                    date_time_to=msg["to"],
                    as_push=msg["asPush"],
                    gtfs=msg["gtfs"],
                    gtfs_alert_cause_id=msg["gtfsAlertCauseId"],
                    gtfs_alert_effect_id=msg["gtfsAlertEffectId"],
                    gtfs_alert_url=msg["gtfsAlertUrl"],
                    gtfs_alert_header_text=msg["gtfsAlertHeaderText"],
                    gtfs_alert_description_text=msg["gtfsAlertDescriptionText"],
                    route_group_id=msg["routeGroupId"],
                    created_utc=msg["createdUtc"],
                    author_id=msg["authorId"],
                    author=msg["author"],
                    updated=msg["updated"],
                    update_author_id=msg["updateAuthorId"],
                    update_author=msg["updateAuthor"],
                    created_f=msg["createdF"],
                    from_f=msg["fromF"],
                    from_ok=msg["fromOk"],
                    to_ok=msg["toOk"],
                )
            )

        return all_alerts

    def get_vehicles(self, app_version=2) -> list[Vehicle]:
        url = BASE_URL + "/mapGetData.php?getBuses=" + str(app_version)
        body = {"s0": str(self.id), "sA": 1}
        vehicles = send_api_request(url, body)

        if vehicles is None:
            return None

        all_vehicles = []
        for vehicle_id, vehicle in vehicles["buses"].items():
            if vehicle_id == "-1":
                continue

            vehicle = vehicle[0]

            for key in [
                "busId",
                "busName",
                "busType",
                "calculatedCourse",
                "routeId",
                "route",
                "color",
                "created",
                "latitude",
                "longitude",
                "speed",
                "paxLoad100",
                "outOfService",
                "more",
                "tripId",
            ]:
                if key not in vehicle:
                    vehicle[key] = None

            all_vehicles.append(
                Vehicle(
                    id=vehicle["busId"],
                    name=vehicle["busName"],
                    type=vehicle["busType"],
                    system=self,
                    calculated_course=vehicle["calculatedCourse"],
                    route_id=vehicle["routeId"],
                    route_name=vehicle["route"],
                    color=vehicle["color"],
                    created=vehicle["created"],
                    latitude=vehicle["latitude"],
                    longitude=vehicle["longitude"],
                    speed=vehicle["speed"],
                    pax_load=vehicle["paxLoad100"],
                    out_of_service=vehicle["outOfService"],
                    more=vehicle["more"],
                    trip_id=vehicle["tripId"],
                )
            )

        return all_vehicles


def get_systems(app_version=2, sort_mode=1) -> list[TransportationSystem]:
    url = f"{BASE_URL}/mapGetData.php?getSystems={app_version}&sortMode={sort_mode}&credentials=1"
    systems = send_api_request(url, None)

    if systems is None:
        return []

    all_systems = []
    for system in systems["all"]:
        for parameter in list(system.keys()):
            if system[parameter] == "":
                system[parameter] = None

        for key in [
            "goAgencyName",
            "email",
            "goTestMode",
            "name2",
            "homepage",
            "logo",
            "goRoutePlannerEnabled",
            "goColor",
            "goSupportEmail",
            "goSharedCode",
            "goAuthenticationType",
        ]:
            if key not in system:
                system[key] = None

        all_systems.append(
            TransportationSystem(
                id=int(system["id"]),
                name=system["fullname"],
                username=system["username"],
                go_agency_name=system["goAgencyName"],
                email=system["email"],
                go_test_mode=bool(int(system["goTestMode"])),
                name2=bool(int(system["name2"])),
                homepage=system["homepage"],
                logo=bool(int(system["logo"])),
                go_route_planner_enabled=bool(int(system["goRoutePlannerEnabled"])),
                go_color=system["goColor"],
                go_support_email=system["goSupportEmail"],
                go_shared_code=to_int_incl_none(system["goSharedCode"]),
                go_authentication_type=bool(int(system["goAuthenticationType"])),
            )
        )

    return all_systems


def get_system_from_id(id: int, app_version=2, sort_mode=1) -> TransportationSystem:
    assert isinstance(id, int), "`id` must be of type int"
    assert isinstance(app_version, int), "`app_version` must be of type int"
    assert isinstance(sort_mode, int), "`sort_mode` must be of type int"

    systems = get_systems(app_version, sort_mode)

    for system in systems:
        if system.id == id:
            return system
    return None


def print_all_systems_md(include_html_breaks=True):
    systems = get_systems()

    for system in systems:
        print(f"- {system.name} (#{system.id}){'<br/>' if include_html_breaks else ''}")
