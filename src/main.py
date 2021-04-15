from __future__ import absolute_import, annotations

import time
from datetime import datetime
from typing import List

import requests

from station import Station, StationManager


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

    station_list = [Station.from_repr(raw_data, city=city, dt=datetime.now()) for raw_data in stations]

    return station_list


station_manager = StationManager()

while True:

    trento_stations = get_stations_for_trento()
    rovereto_stations = get_stations_for_rovereto()

    stations = trento_stations + rovereto_stations

    print(len(stations))

    station_manager.save(stations)

    print("data updated!")

    time.sleep(10)
