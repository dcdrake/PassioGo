from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .system import TransportationSystem


class Stop:
    def __init__(
        self,
        id: str,
        routes_and_positions: dict = None,
        system_id: int = None,
        name: str = None,
        latitude: float = None,
        longitude: float = None,
        radius: int = None,
        system: TransportationSystem = None,
    ):
        if routes_and_positions is None:
            routes_and_positions = {}

        self.id = id
        self.routes_and_positions = routes_and_positions
        self.system_id = system_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.system = system
