import os
import re
import shlex    # für die Eingabe von Stationen mit Leerzeichen

from StartConsole import *
from graph import*
from shortestRoute import*


def check_file_exists(filename):
    if not os.path.isfile(filename):
        print(bcolors.WARNING + "\nVerkehrsnetz nicht gefunden!" + bcolors.RESET)
        return False
    else:
        return True


def check_station_exists(station):
    return True


def create_network_from_file(filename):
    with open(filename, 'r') as file:
        stations = set()
        routes = []

        for line in file:
            parts = line.strip().split(': ')
            if len(parts) > 1:
                line_name = parts[0]
                line = parts[1]
                line_parts = re.findall(r'\".*?\"(?: \d)?', line)

                for i in range(len(line_parts) - 1):
                    station1 = line_parts[i].split('"')[1]
                    station2 = line_parts[i + 1].split('"')[1]
                    weight = int(line_parts[i].split(' ')[-1])

                    stations.add(station1)
                    stations.add(station2)
                    routes.append((station1, station2, weight, line_name))

        graph = Graph(sorted(list(stations)))
        for route in routes:
            graph.add_route(*route)

        return graph


programm_description()

routes = ShortestRoutes()

while True:
    command = input(bcolors.HEADER + bcolors.RED + "path_finder: " + bcolors.RESET)
    if not command.strip():
        print(bcolors.WARNING + "\nUngültiger Befehl!" + bcolors.RESET)
        continue

    split_input = shlex.split(command)

    if split_input[0] == "exit":
        print(bcolors.CYAN + bcolors.BOLD + "Auf Wiedersehen!" + bcolors.RESET)
        break

    if len(split_input) < 3:
        print(bcolors.WARNING + "\nUngültiger Befehl!" + bcolors.RESET)
        continue

    if not split_input[0].endswith(".txt"):
        split_input[0] += ".txt"

    if check_file_exists(split_input[0]):
        network = create_network_from_file(split_input[0])
        if network.station_exists(split_input[1]) and network.station_exists(split_input[2]):
            existing_route = routes.get_route(split_input[1], split_input[2])
            if existing_route:
                route, total_time = existing_route
            else:
                route, total_time = network.find_shortest_route(split_input[1], split_input[2])
                routes.add_route(split_input[1], split_input[2], (route, total_time))
            print_route(route, total_time)
        else:
            if not network.station_exists(split_input[1]):
                print(bcolors.WARNING + f"\nUngültige Station: {split_input[1]}!" + bcolors.RESET)
            else:
                print(bcolors.WARNING + f"\nUngültige Station: {split_input[2]}!" + bcolors.RESET)
    else:
        print(bcolors.WARNING + f"\nDatei nicht gefunden: {split_input[0]}" + bcolors.RESET)
