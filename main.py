import os
import re

from StartConsole import *
from graph import*

def check_file_exists(filename):
    if not os.path.isfile(filename):
        print(bcolors.WARNING + "\nFile not found!" + bcolors.RESET)
        return False


def check_station_exists(station):
    return True


def create_network_from_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(': ')
            if len(parts) > 1:  # make sure there is something after the ':'
                line_name = parts[0]  # save the line name
                line = parts[1]
                line_parts = re.findall(r'\".*?\" \d', line)  # split the remaining string into station-time pairs
                for i in range(len(line_parts) - 1):
                    station1 = line_parts[i].split('"')[1]
                    station2 = line_parts[i + 1].split('"')[1]
                    weight = int(line_parts[i].split(' ')[-1])
                    graph.add_route(station1, station2, weight, line_name)  # add the line name when adding the route
    return graph


programm_description()

while True:
    command = input(bcolors.HEADER + bcolors.RED + "path_finder: " + bcolors.RESET)
    if not command.strip():
        print(bcolors.WARNING + "\nInvalid command!" + bcolors.RESET)
        continue

    split_input = command.split()

    if split_input[0] == "exit":
        print(bcolors.CYAN + bcolors.BOLD + "Goodbye!" + bcolors.RESET)
        break

    if len(split_input) < 3:
        print(bcolors.WARNING + "\nInvalid command!" + bcolors.RESET)
        continue

    if not split_input[0].endswith(".txt"):
        split_input[0] += ".txt"

    if check_file_exists(split_input[0]):
        network = create_network_from_file(split_input[0])
        if network.station_exists(split_input[1]) and network.station_exists(split_input[2]):
            network.show_network()
            break
        else:
            print(bcolors.WARNING + "\nInvalid Station!" + bcolors.RESET)

    break
