class Graph:
    def __init__(self):
        self.network = {}

    def add_station(self, station):
        if station not in self.network:
            self.network[station] = []

    def add_route(self, station1, station2, weight=1, line=None):
        self.add_station(station1)
        self.add_station(station2)
        self.network[station1].append((station2, weight, line))
        self.network[station2].append((station1, weight, line))

    def show_network(self):
        for station in self.network:
            print(station, "->", self.network[station])

    def station_exists(self, station):
        return station in self.network
