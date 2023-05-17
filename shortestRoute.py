# Die Funktion implementiert den Dijkstra-Algorithmus, um den kürzesten Weg zwischen zwei Stationen
# in einem gegebenen Netzwerk von Stationen und Verbindungen zu finden.
def find_shortest_route_with_dijkstra(network, start, end):
    shortest_distances = {station: float('inf') for station in network.network}  # Initialisiere die kürzesten Distanzen zu allen Stationen als unendlich, damit es bei jeder Distanz sofort anschlägt
    previous_stations = {station: None for station in network.network}  # Initialisiere die vorherigen Stationen auf dem kürzesten Pfad als None
    shortest_distances[start] = 0  # Setze die kürzeste Distanz zur Startstation auf 0
    unvisited_stations = network.network.copy()  # Erstelle eine Kopie des Netzwerks, um die unbesuchten Stationen zu verfolgen (alle sind am anfang unbesucht)

    while unvisited_stations:
        current_station = min(unvisited_stations, key=lambda station: shortest_distances[station])  # Wähle die Station mit der kürzesten Distanz als aktuelle Station
        if shortest_distances[current_station] == float('inf'):  # Wenn die kürzeste Distanz zur aktuellen Station unendlich ist (kein Pfad vorhanden)
            break  # Beende die Schleife
        for neighbour, (distance, _) in network.network[current_station].items():  # Für jede Nachbarstation der aktuellen Station
            if neighbour in unvisited_stations:  # Wenn die Nachbarstation noch nicht besucht wurde
                new_distance = shortest_distances[current_station] + distance  # Berechne die neue Distanz zur Nachbarstation
                if new_distance < shortest_distances[neighbour]:  # Wenn die neue Distanz kürzer ist als die bisherige kürzeste Distanz zur Nachbarstation
                    shortest_distances[neighbour] = new_distance  # Aktualisiere die kürzeste Distanz zur Nachbarstation
                    previous_stations[neighbour] = (current_station, network.network[current_station][neighbour][1],distance)  # Aktualisiere die vorherige Station auf dem kürzesten Pfad zur Nachbarstation
        unvisited_stations.pop(current_station)  # Entferne die aktuelle Station aus den unbesuchten Stationen

    path = []  # Initialisiere eine leere Liste für den Pfad
    current_station = end  # Setze die aktuelle Station auf die Endstation
    while current_station is not None:  # Solange die aktuelle Station nicht None ist (d.h. solange wir nicht am Startpunkt sind)

        # Füge die aktuelle Station, die Linie und die Zeit zum Pfad hinzu
        path.append((current_station, previous_stations[current_station][1] if previous_stations[current_station] else None, previous_stations[current_station][2] if previous_stations[current_station] else 0))
        current_station = previous_stations[current_station][0] if previous_stations[current_station] else None  # Setze die aktuelle Station auf die vorherige Station auf dem kürzesten Pfad
    path = path[::-1]  # Kehre die Reihenfolge des Pfads um, um den richtigen Weg vom Start zum Ziel zu erhalten

    return path, shortest_distances[end]  # Gib den Pfad und die kürzeste Distanz zum Ziel zurück


def print_route(route, total_time):
    print(f"Die kürzeste Route von {route[0][0]} zu {route[-1][0]} ist:")
    print(f"Startstation ist {route[0][0]}")

    current_line = route[0][1]
    line_route = f"{current_line}: " if current_line is not None else ""

    for i in range(len(route)):
        station, line, time = route[i]
        if i == 0:  # Skip the first station, as it is the start station
            continue
        if line != current_line:  # If the line changes
            if current_line is not None:  # Only print if the line is not None
                print(line_route.rstrip())
                print(f"Steige von Linie {current_line} um auf Linie {line} in der Station {route[i - 1][0]}")
            current_line = line
            line_route = f"{current_line}: {route[i - 1][0]} ({time} min') {station} ({time} min') "
        else:
            line_route += f"{station} ({time} min') "

    print(line_route.rstrip())  # Print the route for the last line
    print(f"Zielstation {route[-1][0]} wurde erreicht!")
    print(f"Gesamte Fahrzeit: {total_time} Minuten")
