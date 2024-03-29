class Graph:
    def __init__(self, stations):   # Konstruktor mit allen Stationen
        self.stations = stations    # Dictionary aller Stationen

        # In self.index_to_station wird ein Dictionary erstellt, das die Indizes als Schlüssel
        # und die Stationen als Werte hat. Das bedeutet, dass du durch Zugriff auf
        # self.index_to_station[index] den Stationsnamen für einen bestimmten Index bekommen kannst.
        # Das Gleiche gilt umgekehrt für station_to_index
        self.index_to_station = {index: station for index, station in enumerate(stations)}
        self.station_to_index = {station: index for index, station in enumerate(stations)}

        # Hier wird eine 2D-Matrix erstellt, die die Anzahl der Stationen n in beiden Dimensionen hat -> nxn Matrix
        # vorerst werden alle Matrix-Werte auf None gesetzt, da es zunächst noch keine Verbindungen gibt
        self.graph = [[None] * len(stations) for _ in range(len(stations))]

        # Hauptdiagonale wird auf 0 gesetzt, da die Verbindung zu sich selbst ein Gewicht von 0 hat ist
        for i in range(len(stations)):
            self.graph[i][i] = 0

        # Matrix aller Linen (nxn n-Stationen). Vorerst werden alle Werte auf None gesetzt
        self.lines = [[None] * len(stations) for _ in range(len(stations))]

    def add_route(self, station1, station2, weight=1, line=None):
        # Sucht die Indexe (in der Matrix) der beiden Stationen
        i = self.station_to_index[station1]
        j = self.station_to_index[station2]
        # Fügt die Gewichte in die Matrix an den beiden Werten ein, wo sich die Stationen kreuzen
        self.graph[i][j] = weight
        self.graph[j][i] = weight
        # Fügt das Gleiche in die Matrix für die Lines ein
        self.lines[i][j] = line
        self.lines[j][i] = line

    def station_exists(self, station):
        return station in self.stations  # Station wird im Stationen-Dictionary gesucht
        # Die Laufzeit ist konstant O(1), da nach einem unique Key gesucht wird

    def find_shortest_route(self, start, end):
        # Initialisiere die kürzesten Distanzen und vorherigen Stationen
        shortest_distances = {station: float('inf') for station in self.stations}
        previous_stations = {station: None for station in self.stations}
        previous_line = {station: None for station in self.stations}

        shortest_distances[start] = 0  # Setze die kürzeste Distanz zur Startstation auf 0

        unvisited = set(self.stations)  # Set mit allen unbesuchten Stationen

        # Solange es noch unbesuchte Stationen gibt
        while len(unvisited) > 0:
            current_node = min(unvisited, key=lambda node: shortest_distances[node])  # Nimm die nächste unbesuchte Station mit der geringsten Distanz

            unvisited.remove(current_node)  # Entferne die Station aus den unbesuchten Stationen

            if current_node == end:
                break

            current_index = self.station_to_index[current_node]  # Index des aktuellen Knotens

            for neighbor_index, weight in enumerate(self.graph[current_index]):  # Schaue alle Nachbarn des aktuellen Knotens an
                if weight is not None:  # Es besteht eine Verbindung zu diesem Nachbarn
                    neighbor = self.index_to_station[neighbor_index]  # Station des Nachbarn
                    new_distance = shortest_distances[current_node] + weight  # Berechne die neue Distanz zum Nachbarn (über den aktuellen Knoten)
                    if new_distance < shortest_distances[neighbor]:  # Wenn ein kürzerer Weg gefunden wird,
                        shortest_distances[neighbor] = new_distance  # Aktualisiere die kürzeste Distanz
                        previous_stations[neighbor] = current_node  # Aktualisiere die vorherige Station
                        previous_line[neighbor] = self.lines[current_index][neighbor_index]  # Aktualisiere die vorherige Linie

        shortest_route = []  # Liste für die kürzeste Route
        current_node = end  # Aktuelle Station ist die Endstation
        while current_node is not None:  # Solange es noch eine aktuelle Station gibt
            # Füge die aktuelle Station, die vorherige Linie und die kürzeste Distanz zur Route hinzu
            shortest_route.append((current_node, previous_line[current_node], shortest_distances[current_node])) 
            current_node = previous_stations[current_node]  # Aktuelle Station wird zur vorherigen Station
        shortest_route.reverse()  # Route wird umgedreht, da sie von hinten nach vorne erstellt wurde

        return shortest_route, shortest_distances[end]  # Kürzeste Route und kürzeste Distanz werden zurückgegeben
