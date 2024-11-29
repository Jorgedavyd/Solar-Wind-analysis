from starstream import DataDownloading, WIND
from datetime import datetime
from typing import List, Tuple

solar_wind_events: List[Tuple[datetime, datetime]] = [
    (datetime(2003, 10, 28), datetime(2003, 10, 30)),  # Halloween storm
    (
        datetime(2012, 7, 22),
        datetime(2012, 7, 24),
    ),  # Carrington-class CME narrowly missed Earth
    (datetime(2015, 3, 17), datetime(2015, 3, 19)),  # St. Patrick's Day storm
    (datetime(2021, 11, 3), datetime(2021, 11, 5)),  # CME-related geomagnetic storm
    (datetime(2022, 3, 30), datetime(2022, 4, 1)),  # High-speed solar wind stream
]


if __name__ == "__main__":
    DataDownloading(WIND.TDP_PM(root="/data/SW/"), solar_wind_events)
