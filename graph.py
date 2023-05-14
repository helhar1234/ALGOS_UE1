class Graph:
    def __init__(self):
        self.network = {}

    def add_station(self, station):
        if station not in self.network:
            self.network[station] = {}

    def add_route(self, station1, station2, weight=1, line=None):
        self.add_station(station1)
        self.add_station(station2)
        self.network[station1][station2] = (weight, line)
        self.network[station2][station1] = (weight, line)

    def show_network(self):
        for station in self.network:
            print(station, "->", self.network[station])

    def station_exists(self, station):
        return station in self.network

    def get_matrix(self):
        stations = list(self.network.keys())
        matrix = [[0 for _ in range(len(stations))] for _ in range(len(stations))]
        for i, station1 in enumerate(stations):
            for j, station2 in enumerate(stations):
                if station2 in self.network[station1]:
                    matrix[i][j] = self.network[station1][station2][0]
        return matrix
