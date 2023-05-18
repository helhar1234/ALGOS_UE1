class Graph:
    def __init__(self, stations):
        self.stations = stations
        self.index_to_station = {index: station for index, station in enumerate(stations)}
        self.station_to_index = {station: index for index, station in enumerate(stations)}
        # Erstellen einer Matrix der Größe n*n mit allen Werten auf Unendlich
        self.graph = [[float('inf')] * len(stations) for _ in range(len(stations))]
        # Setzen Sie den Wert der Hauptdiagonale auf 0 (da die Entfernung von einer Station zu sich selbst 0 ist)
        for i in range(len(stations)):
            self.graph[i][i] = 0
        # Zusätzliches Attribut, um die Linieninformationen für jede Kante zu speichern
        self.lines = [[None] * len(stations) for _ in range(len(stations))]

    def add_route(self, station1, station2, weight=1, line=None):
        i = self.station_to_index[station1]
        j = self.station_to_index[station2]
        # Füllen Sie die entsprechenden Zellen in der Matrix
        self.graph[i][j] = weight
        self.graph[j][i] = weight
        # Speichern Sie die Linie für die entsprechende Kante
        self.lines[i][j] = line
        self.lines[j][i] = line


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

            current_index = self.station_to_index[current_node]  # Index des aktuellen Knotens

            for neighbor_index, weight in enumerate(
                    self.graph[current_index]):  # Schaue alle Nachbarn des aktuellen Knotens an
                if weight != float('inf'):  # Es besteht eine Verbindung zu diesem Nachbarn
                    neighbor = self.index_to_station[neighbor_index]  # Station des Nachbarn
                    new_distance = shortest_distances[current_node] + weight
                    if new_distance < shortest_distances[
                        neighbor]:  # Wenn ein kürzerer Weg gefunden wird, aktualisiere die kürzeste Distanz und setze die vorherige Station
                        shortest_distances[neighbor] = new_distance
                        previous_stations[neighbor] = current_node
                        previous_line[neighbor] = self.lines[current_index][neighbor_index]

        # Bauen Sie die Route rückwärts auf
        shortest_route = []
        current_node = end
        while current_node is not None:
            shortest_route.append((current_node, previous_line[current_node], shortest_distances[current_node]))
            current_node = previous_stations[current_node]
        shortest_route.reverse()

        return shortest_route, shortest_distances[end]

