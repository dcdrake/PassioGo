from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .system import TransportationSystem


class Vehicle:
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
        system: TransportationSystem = None,
        calculated_course: int = None,
        route_id: str = None,
        route_name: str = None,
        color: str = None,
        created: str = None,
        latitude: float = None,
        longitude: float = None,
        speed: float = None,
        pax_load: float = None,
        out_of_service: bool = None,
        more: str = None,
        trip_id: str = None,
    ):
        self.id = id
        self.name = name
        self.type = type
        self.system = system
        self.calculated_course = calculated_course
        self.route_id = route_id
        self.route_name = route_name
        self.color = color
        self.created = created
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.pax_load = pax_load
        self.out_of_service = out_of_service
        self.more = more
        self.trip_id = trip_id
