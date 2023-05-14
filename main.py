import os    # um zu überprüfen, ob eine Datei existiert
import re    # um die Zeilen aus der Datei zu parsen

from StartConsole import *  # um die Beschreibung des Programms auszugeben
from graph import *     # um die Klasse Graph zu importieren


def check_file_exists(filename):    # Funktion um zu überprüfen, ob eine Datei existiert
    if not os.path.isfile(filename):    # Wenn die Datei nicht existiert
        print(bcolors.WARNING + "\nFile not found!" + bcolors.RESET)     # Gib eine Warnung aus
        return False    # Gib zurück, dass die Datei nicht existiert
    else:   # Wenn die Datei existiert
        return True  # Gib zurück, dass die Datei existiert


def check_station_exists(station):  # Funktion um zu überprüfen, ob eine Station existiert
    return True     # Gib zurück, dass die Station existiert


def create_network_from_file(filename):     # Funktion um ein Netzwerk aus einer Datei zu erstellen
    graph = Graph()     # Erstelle ein Graph Objekt
    with open(filename, 'r') as file:   # Öffne die Datei
        for line in file:   # Für jede Zeile in der Datei
            parts = line.strip().split(': ')    # Teile die Zeile an dem ':' auf
            if len(parts) > 1:  # wenn die Zeile mehr als einen Teil hat
                line_name = parts[0]    # der erste Teil ist der Name der Linie
                line = parts[1]  # der zweite Teil ist die Linie
                line_parts = re.findall(r'\".*?\" \d', line)    # finde alle Stationen in der Linie
                for i in range(len(line_parts) - 1):    # für jede Station in der Linie
                    station1 = line_parts[i].split('"')[1]  # speichere die erste Station in einer Variable
                    station2 = line_parts[i + 1].split('"')[1]  # speichere die zweite Station in einer Variable
                    weight = int(line_parts[i].split(' ')[-1])  # speichere das Gewicht in einer Variable
                    graph.add_route(station1, station2, weight, line_name)  # füge die Verbindung hinzu
    return graph    # gib den Graphen zurück


programm_description()  # Gib die Beschreibung des Programms aus

while True:     # Wiederhole so lange bis der Benutzer das Programm beendet
    command = input(bcolors.HEADER + bcolors.RED + "path_finder: " + bcolors.RESET)   # Gib eine Eingabeaufforderung aus
    if not command.strip():  # Wenn die Eingabe leer ist
        print(bcolors.WARNING + "\nInvalid command!" + bcolors.RESET)   # Gib eine Warnung aus
        continue     # Springe zum nächsten Durchlauf

    split_input = command.split()   # Teile die Eingabe an den Leerzeichen auf

    if split_input[0] == "exit":    # Wenn der Benutzer das Programm beenden will
        print(bcolors.CYAN + bcolors.BOLD + "Goodbye!" + bcolors.RESET)     # Gib eine Verabschiedung aus
        break   # Beende das Programm

    if len(split_input) < 3:     # Wenn die Eingabe weniger als 3 Teile hat
        print(bcolors.WARNING + "\nInvalid command!" + bcolors.RESET)   # Gib eine Warnung aus
        continue    # Springe zum nächsten Durchlauf

    if not split_input[0].endswith(".txt"):     # Wenn die Eingabe keine Dateiendung hat
        split_input[0] += ".txt"    # Füge die Dateiendung hinzu

    if check_file_exists(split_input[0]):   # Wenn die Datei existiert
        network = create_network_from_file(split_input[0])  # Erstelle ein Netzwerk aus der Datei
        if network.station_exists(split_input[1]) and network.station_exists(split_input[2]):  # Wenn beide Stationen existieren
            network.show_network()   # Gib das Netzwerk aus
            break
        else:   # Wenn eine der Stationen nicht existiert
            print(bcolors.WARNING + "\nInvalid Station!" + bcolors.RESET)   # Gib eine Warnung aus

    break
