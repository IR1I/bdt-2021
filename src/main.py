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

def get_totalAverage(file: str) -> None:
    with open(file, "r") as f:
        raw_stations = json.load(f)
        station = [Station.from_repr(raw_station) for raw_station in raw_stations]
    nb_bikes = 0
    nb_slots = 0
    for i in range(len(station)):
        nb_bikes= nb_bikes + station[i].bikes
        nb_slots= nb_slots + station[i].slots
    bikes= nb_bikes/len(station)
    parking=nb_slots/len(station)
    print(bikes)
    print(parking)
station_manager = StationManager()

trento_stations = get_stations_for_trento()
rovereto_stations = get_stations_for_rovereto()

stations = trento_stations + rovereto_stations
get_totalAverage(stations)

def get_totalAverage(station: Station) -> None:
    with open(file, "r") as f:
        raw_stations = json.load(f)
        station = [Station.from_repr(raw_station) for raw_station in raw_stations]
    nb_bikes = 0
    nb_slots = 0
    for i in range(len(station)):
        nb_bikes= nb_bikes + station[i].bikes
        nb_slots= nb_slots + station[i].slots
    bikes= nb_bikes/len(station)
    parking=nb_slots/len(station)
    print(bikes)
    print(parking)
station_manager = StationManager()

trento_stations = get_stations_for_trento()
rovereto_stations = get_stations_for_rovereto()

stations = trento_stations + rovereto_stations
get_totalAverage(stations)


def get_totalAveragecity(station: Station, city:str) -> None:
    with open(file, "r") as f:
        raw_stations = json.load(f)
        station = [Station.from_repr(raw_station) for raw_station in raw_stations]
    nb_bikes = 0
    nb_slots = 0
    for i in range(len(station)):
        if city==stations[i].city:
            nb_bikes= nb_bikes + station[i].bikes
            nb_slots= nb_slots + station[i].slots
    bikes= nb_bikes/len(station)
    parking=nb_slots/len(station)
    print(bikes)
    print(parking)
station_manager = StationManager()

trento_stations = get_stations_for_trento()
rovereto_stations = get_stations_for_rovereto()

stations = trento_stations + rovereto_stations
get_totalAveragecity(stations,"Trento")

def get_totalAveragestation(station: Station,name:str) -> None:
    with open(file, "r") as f:
        raw_stations = json.load(f)
        station = [Station.from_repr(raw_station) for raw_station in raw_stations]
    nb_bikes = 0
    nb_slots = 0
    for i in range(len(station)):
        if name==stations[i].name:
            nb_bikes= nb_bikes + station[i].bikes
            nb_slots= nb_slots + station[i].slots
    bikes= nb_bikes/len(station)
    parking=nb_slots/len(station)
    print(bikes)
    print(parking)
station_manager = StationManager()

trento_stations = get_stations_for_trento()
rovereto_stations = get_stations_for_rovereto()

stations = trento_stations + rovereto_stations
get_totalAveragestation(stations,"Piazza di Centa")









"""

while True:

    trento_stations = get_stations_for_trento()
    rovereto_stations = get_stations_for_rovereto()

    stations = trento_stations + rovereto_stations

    print(len(stations))

    station_manager.save(stations)

    print("data updated!")

    time.sleep(60)


def averagebikeavaialability(database):
  emptylist=[]
  for i in range(len(database)):
    emptylist.append(database[i]["bikes"])
  return sum(emptylist)/len(emptylist)

def averageslotsavaialability(database):
  emptylist=[]
  for i in range(len(database)):
    emptylist.append(database[i]["slots"])
  return sum(emptylist)/len(emptylist)

"""