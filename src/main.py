from __future__ import absolute_import, annotations

from typing import List

import requests


class Position:

    def __init__(self, lat: float, lon: float) -> None:
        self.lat = lat
        self.lon = lon


class Station:

    def __init__(self, station_id: str, name: str, address: str, bikes: int, slots: int, city: str, position: Position):
        self.id = station_id
        self.name = name
        self.address = address
        self.bikes = bikes
        self.slots = slots
        self.city = city
        self.position = position

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
        }

    @staticmethod
    def from_repr(raw_data: dict, city: str) -> Station:
        return Station(
            raw_data["id"],
            raw_data["name"],
            raw_data["address"],
            raw_data["slots"],
            raw_data["bikes"],
            city,
            Position(
                raw_data["position"][0],
                raw_data["position"][1]
            )
        )


def get_stations_for_trento() -> List[Station]:
    stations = get_stations("https://os.smartcommunitylab.it/core.mobility/bikesharing/trento", "Trento")
    return stations


def get_stations_for_rovereto() -> List[Station]:
    stations = get_stations("https://os.smartcommunitylab.it/core.mobility/bikesharing/rovereto", "Rovereto")
    return stations


def get_stations(url: str, city: str) -> List[Station]:
    """
    Get the list of stations for a particular url

    :param str url: this is the url to query stations from
    :return: the list of stations
    """
    resp = requests.get(url)
    stations = resp.json()

    station_list = [Station.from_repr(raw_data, city) for raw_data in stations]

    return station_list


trento_stations = get_stations_for_trento()
rovereto_stations = get_stations_for_rovereto()

stations = trento_stations + rovereto_stations

print(len(stations))

print(len([station for station in stations if station.city == "Trento"]))
print(len([station for station in stations if station.city == "Rovereto"]))

print(sum([station.bikes for station in stations]))
print(sum([station.slots for station in stations]))

names = [station.name for station in stations]
slots = [station.slots for station in stations]
bikes = [station.bikes for station in stations]
