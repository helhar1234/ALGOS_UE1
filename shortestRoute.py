class ShortestRoutes:
    def __init__(self):
        self.routes = {}

    def add_station(self, station):
        self.routes[station] = {}

    def add_connection(self, station1, station2, distance, line):
        self.routes[station1][station2] = (distance, line)

    def get_route(self, start, end):
        if start in self.routes and end in self.routes[start]:
            return self.routes[start][end]
        else:
            return None

    def add_route(self, start, end, route):
        if start not in self.routes:
            self.routes[start] = {}
        self.routes[start][end] = route


class DijkstraRouter:
    def __init__(self, network):
        self.network = network

    def find_shortest_route(self, start, end):
        shortest_distances = {station: float('inf') for station in self.network.network}
        previous_stations = {station: None for station in self.network.network}
        shortest_distances[start] = 0
        unvisited_stations = self.network.network.copy()

        while unvisited_stations:
            current_station = min(unvisited_stations, key=lambda station: shortest_distances[station])
            if shortest_distances[current_station] == float('inf'):
                break
            for neighbour, (distance, _) in self.network.network[current_station].items():
                if neighbour in unvisited_stations:
                    new_distance = shortest_distances[current_station] + distance
                    if new_distance < shortest_distances[neighbour]:
                        shortest_distances[neighbour] = new_distance
                        previous_stations[neighbour] = (current_station, self.network.network[current_station][neighbour][1], distance)
            unvisited_stations.pop(current_station)

        path = []
        current_station = end
        while current_station is not None:
            path.append((current_station, previous_stations[current_station][1] if previous_stations[current_station] else None, previous_stations[current_station][2] if previous_stations[current_station] else 0))
            current_station = previous_stations[current_station][0] if previous_stations[current_station] else None
        path = path[::-1]

        return path, shortest_distances[end]


def print_route(route, total_time):
    print(f"Die kürzeste Route von {route[0][0]} zu {route[-1][0]} ist:")
    print(f"Startstation ist {route[0][0]}")

    current_line = route[0][1]
    line_route = f"{current_line}: " if current_line is not None else ""

    for i in range(len(route)):
        station, line, time = route[i]
        if i == 0:
            continue
        if line != current_line:
            if current_line is not None:
                print(line_route.rstrip())
                print(f"Steige von Linie {current_line} um auf Linie {line} in der Station {route[i - 1][0]}")
            current_line = line
            line_route = f"{current_line}: {route[i - 1][0]} ({time} min') {station} "
        else:
            line_route += f" ({time} min') {station}"

    print(line_route.rstrip())
    print(f"Zielstation {route[-1][0]} wurde erreicht!")
    print(f"Gesamte Fahrzeit: {total_time} Minuten")
