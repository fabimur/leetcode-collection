from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.departures = {}                          # id -> (estación, tiempo)
        self.travel_times = defaultdict(lambda: [0, 0])  # trayecto -> [total, nº viajes]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.departures[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.departures.pop(id)

        travel_name = start_station + "->" + stationName
        travel_time = t - start_time

        self.travel_times[travel_name][0] += travel_time
        self.travel_times[travel_name][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_name = startStation + "->" + endStation
        total, count = self.travel_times[travel_name]

        return total / count