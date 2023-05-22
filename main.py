import os
import re
import shlex  # für die Eingabe von Stationen mit Leerzeichen

from StartConsole import *
from graph import *
from shortestRoute import *


def check_file_exists(filename):
    if not os.path.isfile(filename):
        print(bcolors.WARNING + "\nVerkehrsnetz nicht gefunden!" + bcolors.RESET)
        return False
    else:
        return True


def create_network_from_file(filename):
    #   File mit dem Verkehrsnetz wird im Lesemodus geöffnet
    with open(filename, 'r') as file:
        #   Es werden 2 Sets für Stations und Routes definiert
        stations = set()
        routes = []

        #   Jede Zeile wird aufgeteilt (bei ':')
        for line in file:
            parts = line.strip().split(': ')
            if len(parts) > 1:
                line_name = parts[0]
                line = parts[1]
                line_parts = re.findall(r'\".*?\"(?: \d)?', line)  # REGEX für eine gültige Route

                #   Für jede Zeile werden alle Stationen in Form von Routen (2 verbundene Stationen und die Zeit dazwischen) geteilt
                for i in range(len(line_parts) - 1):
                    station1 = line_parts[i].split('"')[1]  # 1. Station
                    station2 = line_parts[i + 1].split('"')[1]  # 2. Station
                    weight = int(line_parts[i].split(' ')[-1])  # Fahrtzeit zwischen Station 1 und 2
                    line_name = line_name  # Speichern Sie den Namen der Linie für die spätere Verwendung

                    #   Stationen werden zum Stations-Set hinzugefügt
                    stations.add(station1)
                    stations.add(station2)
                    #   Route wird zum Routes-Set hinzugefügt
                    routes.append((station1, station2, weight, line_name))

        #   Graph-Objekt wird erstellt (mit den Stationen)
        graph = Graph(sorted(list(stations)))
        #   Alle Routen werden hinzugefügt
        for route in routes:
            graph.add_route(*route)  # * ->  teilt die Werte in route (=Stationen und Gewicht) in einzelne Variablen auf,
            #   daher nimmt die Methode add_route 4 Variablen

        #   Graph wird an main zurückgegeben
        return graph


programm_description()  # Beschreibung des Programms wird ausgegeben

routes = ShortestRoutes()  # Objekt für die kürzesten Routen wird erstellt

previous_filename = ""  # Variable für die vorherige Datei
filename = ""  # Variable für die aktuelle Datei
network = ""  # Variable für das aktuelle Netzwerk

while True:  # Endlosschleife für die Eingabe von Befehlen
    command = input(bcolors.HEADER + bcolors.RED + "path_finder: " + bcolors.RESET)
    if not command.strip():  # Wenn der Befehl leer ist, wird die Schleife erneut ausgeführt
        print(bcolors.WARNING + "\nUngültiger Befehl!" + bcolors.RESET)
        continue

    split_input = shlex.split(command)  # Eingabe wird in einzelne Wörter geteilt

    if split_input[0] == "exit":  # Wenn der Befehl "exit" ist, wird das Programm beendet
        print(bcolors.CYAN + bcolors.BOLD + "Auf Wiedersehen!" + bcolors.RESET)
        break

    if len(split_input) < 3:  # Wenn die Eingabe weniger als 3 Wörter hat, wird die Schleife erneut ausgeführt
        print(bcolors.WARNING + "\nUngültiger Befehl!" + bcolors.RESET)
        continue

    if not split_input[0].endswith(".txt"):  # Wenn die Eingabe nicht mit ".txt" endet, wird ".txt" hinzugefügt
        split_input[0] += ".txt"

    #   Wenn die Datei existiert, wird sie geöffnet und das Netzwerk wird erstellt
    if check_file_exists(split_input[0]):
        filename = split_input[0]  # Dateiname wird gespeichert
        if filename != previous_filename:  # Wenn der Dateiname nicht gleich dem vorherigen Dateinamen ist
            previous_filename = filename  # wird der vorherige Dateiname aktualisiert
            network = create_network_from_file(split_input[0])  # Netzwerk wird erstellt

        #   Wenn die Stationen existieren, wird die kürzeste Route gesucht
        if network.station_exists(split_input[1]) and network.station_exists(split_input[2]):
            #   Wenn die Route bereits gesucht wurde, wird sie aus dem Dictionary geholt
            existing_route = routes.get_route(split_input[1], split_input[2])
            if existing_route:  # Wenn die Route existiert, wird sie ausgegeben
                route, total_time = existing_route
            else:  # Wenn die Route nicht existiert, wird sie gesucht und zum Dictionary hinzugefügt
                route, total_time = network.find_shortest_route(split_input[1], split_input[2])
                routes.add_route(split_input[1], split_input[2], (route, total_time))
            print_route(route, total_time)  # Route wird ausgegeben
        else:  # Wenn die Stationen nicht existieren, wird eine Fehlermeldung ausgegeben
            if not network.station_exists(split_input[1]):
                print(bcolors.WARNING + f"\nUngültige Station: {split_input[1]}!" + bcolors.RESET)
            else:
                print(bcolors.WARNING + f"\nUngültige Station: {split_input[2]}!" + bcolors.RESET)
    else:  # Wenn die Datei nicht existiert, wird eine Fehlermeldung ausgegeben
        print(bcolors.WARNING + f"\nDatei nicht gefunden: {split_input[0]}" + bcolors.RESET)
