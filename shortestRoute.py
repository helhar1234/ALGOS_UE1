# Die Funktion implementiert den Dijkstra-Algorithmus, um den kürzesten Weg zwischen zwei Stationen
# in einem gegebenen Netzwerk von Stationen und Verbindungen zu finden.
def find_shortest_route_with_dijkstra(network, start, end):
    shortest_distances = {station: float('inf') for station in
                          network.network}  # Initialisiere die kürzesten Distanzen zu allen Stationen als unendlich, damit es bei jeder Distanz sofort anschlägt
    previous_stations = {station: None for station in
                         network.network}  # Initialisiere die vorherigen Stationen auf dem kürzesten Pfad als None
    shortest_distances[start] = 0  # Setze die kürzeste Distanz zur Startstation auf 0
    unvisited_stations = network.network.copy()  # Erstelle eine Kopie des Netzwerks, um die unbesuchten Stationen zu verfolgen (alle sind am anfang unbesucht)

    while unvisited_stations:
        current_station = min(unvisited_stations, key=lambda station: shortest_distances[
            station])  # Wähle die Station mit der kürzesten Distanz als aktuelle Station
        if shortest_distances[current_station] == float(
                'inf'):  # Wenn die kürzeste Distanz zur aktuellen Station unendlich ist (kein Pfad vorhanden)
            break  # Beende die Schleife
        for neighbour, (distance, _) in network.network[
            current_station].items():  # Für jede Nachbarstation der aktuellen Station
            if neighbour in unvisited_stations:  # Wenn die Nachbarstation noch nicht besucht wurde
                new_distance = shortest_distances[
                                   current_station] + distance  # Berechne die neue Distanz zur Nachbarstation
                if new_distance < shortest_distances[
                    neighbour]:  # Wenn die neue Distanz kürzer ist als die bisherige kürzeste Distanz zur Nachbarstation
                    shortest_distances[neighbour] = new_distance  # Aktualisiere die kürzeste Distanz zur Nachbarstation
                    previous_stations[neighbour] = (current_station, network.network[current_station][neighbour][1],
                                                    distance)  # Aktualisiere die vorherige Station auf dem kürzesten Pfad zur Nachbarstation
        unvisited_stations.pop(current_station)  # Entferne die aktuelle Station aus den unbesuchten Stationen

    path = []  # Initialisiere eine leere Liste für den Pfad
    current_station = end  # Setze die aktuelle Station auf die Endstation
    while current_station is not None:  # Solange die aktuelle Station nicht None ist (d.h. solange wir nicht am Startpunkt sind)

        # Füge die aktuelle Station, die Linie und die Zeit zum Pfad hinzu
        path.append((current_station,
                     previous_stations[current_station][1] if previous_stations[current_station] else None,
                     previous_stations[current_station][2] if previous_stations[current_station] else 0))
        current_station = previous_stations[current_station][0] if previous_stations[
            current_station] else None  # Setze die aktuelle Station auf die vorherige Station auf dem kürzesten Pfad
    path = path[::-1]  # Kehre die Reihenfolge des Pfads um, um den richtigen Weg vom Start zum Ziel zu erhalten

    return path, shortest_distances[end]  # Gib den Pfad und die kürzeste Distanz zum Ziel zurück


from colors import *


# Funktion, die die kürzeste Route übersichtlich ausgibt
def print_route(route, total_time):
    #  Überschriften und Grundinformationen zur Route
    print(f"\n\n{bcolors.BOLD + bcolors.CYAN}{'-' * 40}\nROUTEN INFORMATION:\n{'-' * 40}{bcolors.RESET}\n")
    print(
        f"{bcolors.BOLD + bcolors.WHITE}Die kürzeste Route von {bcolors.UNDERLINE + bcolors.RED + route[0][0] + bcolors.RESET + bcolors.BOLD + bcolors.WHITE}🚩 zu {bcolors.UNDERLINE + bcolors.BLUE + route[-1][0] + bcolors.RESET + bcolors.BOLD + bcolors.WHITE}🏁 ist:{bcolors.RESET}\n")
    print(f"    {bcolors.WHITE}Startstation ist {bcolors.UNDERLINE + bcolors.RED + route[0][0]}{bcolors.RESET}🚩\n")

    current_line = route[0][1]  # Aktuelle Line (U-Bahn oder Straßenbahn)
    line_route = f"    {bcolors.PURPLE + bcolors.UNDERLINE}{current_line}: {bcolors.RESET}" if current_line is not None else ""  # Aktuelle Line wird ausgegeben, (außer sie ist NULL bei der Startstation, wo man NOCH in keiner Line ist)

    for i in range(len(route)):
        station, line, time = route[i]  # Stops werden aufgeteilt und in die Variablen Station, Line und Time unterteilt
        if i == 0:  # Startstation soll nicht separat ausgegeben werden
            continue
        if line != current_line:    # wenn umgestiegen werden soll
            if current_line is not None:    #   wird nur ausgegeben, wenn der Umstieg nicht die bei der Startstation ist
                print(line_route.rstrip())  # unnötige Leerzeichen werden von der Route der einzelnen Line entfernt
                print(f"    {bcolors.UNDERLINE + bcolors.BOLD + bcolors.ORANGE}Umstieg{bcolors.RESET + bcolors.WHITE}: Steige von Linie {bcolors.UNDERLINE + bcolors.PURPLE + current_line + bcolors.RESET + bcolors.WHITE} um auf Linie {bcolors.UNDERLINE + bcolors.PURPLE + line + bcolors.RESET + bcolors.WHITE} in der Station {bcolors.UNDERLINE + bcolors.ORANGE + route[i - 1][0]}{bcolors.RESET}\n")
            current_line = line # Neue Line wird auf current Line gesetzt
            # Line Route wird aufgebaut aus den Informationen
            line_route = f"    {bcolors.UNDERLINE + bcolors.PURPLE + current_line + bcolors.RESET}: {bcolors.WHITE}{route[i - 1][0]} ({time} min') {station}{bcolors.RESET} "
        else:   # wenn nicht umgestiegen werden muss
            line_route += f"{bcolors.WHITE} ({time} min') {station}{bcolors.RESET}" # wird die neue station + Zeit einfach dran gehängt

    print(line_route.rstrip())
    # Endausgabe
    print(f"\n    {bcolors.WHITE}Zielstation {bcolors.UNDERLINE + bcolors.BLUE + route[-1][0] + bcolors.RESET + bcolors.WHITE}🏁 wurde erreicht!{bcolors.RESET}")
    print(f"\n{bcolors.BOLD + bcolors.WHITE}Gesamte Fahrzeit: {bcolors.GREEN + str(total_time)} Minuten{bcolors.RESET}\n")
    print(f"{bcolors.BOLD + bcolors.CYAN}{'-' * 40}{bcolors.RESET}\n\n")
