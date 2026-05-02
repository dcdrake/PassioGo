from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .system import TransportationSystem


class Route:
    def __init__(
        self,
        id: int,
        group_id: int = None,
        group_color: str = None,
        name: str = None,
        short_name: str = None,
        name_orig: str = None,
        fullname: str = None,
        myid: int = None,
        map_app: bool = None,
        archive: bool = None,
        go_prefix_route_name: bool = None,
        go_show_schedule: bool = None,
        outdated: bool = None,
        distance: int = None,
        latitude: float = None,
        longitude: float = None,
        timezone: str = None,
        service_time: str = None,
        service_time_short: str = None,
        system_id: int = None,
        system: TransportationSystem = None,
    ):
        self.id = id
        self.group_id = group_id
        self.group_color = group_color
        self.name = name
        self.short_name = short_name
        self.name_orig = name_orig
        self.fullname = fullname
        self.myid = myid
        self.map_app = map_app
        self.archive = archive
        self.go_prefix_route_name = go_prefix_route_name
        self.go_show_schedule = go_show_schedule
        self.outdated = outdated
        self.distance = distance
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.service_time = service_time
        self.service_time_short = service_time_short
        self.system_id = system_id
        self.system = system

    def get_stops(self):
        stops_for_route = []
        all_stops = self.system.get_stops()

        for stop in all_stops:
            if (
                self.myid in list(stop.routes_and_positions.keys())
                or self.id in list(stop.routes_and_positions.keys())
                or self.group_id in list(stop.routes_and_positions.keys())
            ):
                stops_for_route.append(stop)

        return stops_for_route
