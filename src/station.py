from __future__ import absolute_import, annotations

import json
import os
from datetime import datetime
from typing import Optional, List

class Average:

    def __init__(self, bikes: float, parking: float) -> None:
        self.bikes = bikes
        self.parking = parking

class Position:

    def __init__(self, lat: float, lon: float) -> None:
        self.lat = lat
        self.lon = lon


class Station:

    def __init__(self, station_id: str, name: str, address: str, bikes: int, slots: int, city: str, position: Position, dt: datetime):
        self.id = station_id
        self.name = name
        self.address = address
        self.bikes = bikes
        self.slots = slots
        self.city = city
        self.position = position
        self.dt = dt

    def to_repr(self) -> dict:
        return {
            "name": self.name,
            "id": self.id,
            "address": self.address,
            "bikes": self.bikes,
            "slots": self.slots,
            "totalSlots": self.bikes + self.slots,
            "city": self.city,
            "position": [
                self.position.lat, self.position.lon
            ],
            "timestamp": self.dt.isoformat()
        }

    @staticmethod
    def from_repr(raw_data: dict, city: Optional[str] = None, dt: Optional[datetime] = None) -> Station:

        if not city and "city" not in raw_data:
            raise Exception("Can not build Station model: city information missing")

        if not dt and "timestamp" not in raw_data:
            raise Exception("Can not build Station model: timestamp information is missing")

        return Station(
            raw_data["id"],
            raw_data["name"],
            raw_data["address"],
            raw_data["slots"],
            raw_data["bikes"],
            raw_data["city"] if "city" in raw_data else city,
            Position(
                raw_data["position"][0],
                raw_data["position"][1]
            ),
            datetime.fromisoformat(raw_data["timestamp"]) if "timestamp" in raw_data else dt
        )

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)


class StationManager:

    STATION_FILE = "stations.json"

    def __init__(self) -> None:
        if not os.path.isfile(self.STATION_FILE):
            with open("stations.json", "w") as f:
                json.dump([], f)

    def save(self, stations: List[Station]) -> None:
        old_stations = self.list()
        update_stations = old_stations + stations

        with open("stations.json", "w") as f:
            json.dump(
                [station.to_repr() for station in update_stations],
                f,
                indent=4
            )

    def list(self) -> List[Station]:
        with open("stations.json", "r") as f:
            raw_stations = json.load(f)
            return [Station.from_repr(raw_station) for raw_station in raw_stations]

