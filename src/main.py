from __future__ import absolute_import, annotations

import json
import time
from datetime import datetime
from typing import List

import requests

from src.analysis import station_manager
from station import Station, StationManager, Average
import pandas as pd


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


def get_totalAverage(file: str) -> None:
    station = pd.read_json(file)
    delta= pd.Timedelta(hours=1)
    stationHour= station[station["timestamp"] > datetime.now()-delta]
    #print(stationHour["timestamp"])
    get_Average(stationHour)

def get_Average(station: Station):
    nb_bikes = 0
    nb_slots = 0
    for i in station["bikes"]:
        nb_bikes = nb_bikes + i
    for j in station["slots"]:
        nb_slots = nb_slots + j
    bikes = nb_bikes / len(station)
    parking = nb_slots / len(station)
    print(bikes)
    print(parking)


def get_totalAverageCity(file: str, city: str):
    dataframe = pd.read_json(file)
    stationCity = dataframe[dataframe['city'] == city]
    delta = pd.Timedelta(hours=1)
    stationCityHour = stationCity[stationCity["timestamp"] > datetime.now() - delta]
    get_Average(stationCityHour)


def get_totalAverageStation(file: str, station: str):
    dataframe = pd.read_json(file)
    stationStation = dataframe[dataframe['name'] == station]
    delta = pd.Timedelta(hours=1)
    stationStationHour = stationStation[stationStation["timestamp"] > datetime.now() - delta]
    get_Average(stationStationHour)


i=0
while True:
    trento_stations = get_stations_for_trento()
    rovereto_stations = get_stations_for_rovereto()

    stations = trento_stations + rovereto_stations

    print(len(stations))

    station_manager.save(stations)

    print("data updated!")
    i = i+1
    if i==60:
        get_totalAverage("stations.json")
        get_totalAverageCity("stations.json", "Trento")
        get_totalAverageStation("stations.json", "Sacco")
        i=0
    time.sleep(60)
