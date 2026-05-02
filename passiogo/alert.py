from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .system import TransportationSystem


class SystemAlert:
    def __init__(
        self,
        id: int,
        system_id: int = None,
        system: TransportationSystem = None,
        route_id: int = None,
        name: str = None,
        html: str = None,
        archive: bool = None,
        important: bool = None,
        date_time_created: str = None,
        date_time_from: str = None,
        date_time_to: str = None,
        as_push: bool = None,
        gtfs: bool = None,
        gtfs_alert_cause_id: int = None,
        gtfs_alert_effect_id: int = None,
        gtfs_alert_url: str = None,
        gtfs_alert_header_text: str = None,
        gtfs_alert_description_text: str = None,
        route_group_id: int = None,
        created_utc: str = None,
        author_id: int = None,
        author: str = None,
        updated: str = None,
        update_author_id: int = None,
        update_author: str = None,
        created_f: str = None,
        from_f: str = None,
        from_ok: bool = None,
        to_ok: bool = None,
    ):
        self.id = id
        self.system_id = system_id
        self.system = system
        self.route_id = route_id
        self.name = name
        self.html = html
        self.archive = archive
        self.important = important
        self.date_time_created = date_time_created
        self.date_time_from = date_time_from
        self.date_time_to = date_time_to
        self.as_push = as_push
        self.gtfs = gtfs
        self.gtfs_alert_cause_id = gtfs_alert_cause_id
        self.gtfs_alert_effect_id = gtfs_alert_effect_id
        self.gtfs_alert_url = gtfs_alert_url
        self.gtfs_alert_header_text = gtfs_alert_header_text
        self.gtfs_alert_description_text = gtfs_alert_description_text
        self.route_group_id = route_group_id
        self.created_utc = created_utc
        self.author_id = author_id
        self.author = author
        self.updated = updated
        self.update_author_id = update_author_id
        self.update_author = update_author
        self.created_f = created_f
        self.from_f = from_f
        self.from_ok = from_ok
        self.to_ok = to_ok
