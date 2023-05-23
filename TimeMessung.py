import re
import time  # für die Zeitmessungen

from graph import *
from shortestRoute import *


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
            graph.add_route(
                *route)  # * ->  teilt die Werte in route (=Stationen und Gewicht) in einzelne Variablen auf,
            #   daher nimmt die Methode add_route 4 Variablen

        #   Graph wird an main zurückgegeben
        return graph

# Erstellung des Graphens
start = time.time()

graph = create_network_from_file("wv.txt")

end = time.time()

print(f"Die Ausführung der Funktion create_network_from_file() hat {end - start} Sekunden gedauert.")

# Wegsuche
start = time.time()

route, total_time = graph.find_shortest_route("Floridsdorf", "Praterstern")

end = time.time()

print(f"Die Ausführung der Funktion find_shortest_route hat {end - start} Sekunden gedauert.")