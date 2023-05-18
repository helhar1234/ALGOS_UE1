class Graph:
    def __init__(self, stations):
        self.stations = stations
        self.graph = {station: {} for station in stations}

    def add_route(self, station1, station2, weight=1, line=None):
        self.graph[station1][station2] = (weight, line)
        self.graph[station2][station1] = (weight, line)

    def station_exists(self, station):
        return station in self.stations

    def find_shortest_route(self, start, end):
        # Initialisiere die kürzesten Distanzen und vorherigen Stationen
        shortest_distances = {station: float('inf') for station in self.stations}
        previous_stations = {station: None for station in self.stations}
        previous_line = {station: None for station in self.stations}

        shortest_distances[start] = 0  # Setze die kürzeste Distanz zur Startstation auf 0

        unvisited = set(self.stations)

        while len(unvisited) > 0:
            current_node = min(unvisited, key=lambda node: shortest_distances[
                node])  # Nimm die nächste unbesuchte Station mit der geringsten Distanz

            unvisited.remove(current_node)

            if current_node == end:
                break

            for neighbor, (weight, line) in self.graph[current_node].items():  # Schaue alle Nachbarn des aktuellen Knotens an
                new_distance = shortest_distances[current_node] + weight
                if new_distance < shortest_distances[neighbor]:  # Wenn ein kürzerer Weg gefunden wird, aktualisiere die kürzeste Distanz und setze die vorherige Station
                    shortest_distances[neighbor] = new_distance
                    previous_stations[neighbor] = current_node
                    previous_line[neighbor] = line

        # Bauen Sie die Route rückwärts auf
        shortest_route = []
        current_node = end
        while current_node is not None:
            shortest_route.append((current_node, previous_line[current_node], shortest_distances[current_node]))
            current_node = previous_stations[current_node]
        shortest_route.reverse()

        return shortest_route, shortest_distances[end]
