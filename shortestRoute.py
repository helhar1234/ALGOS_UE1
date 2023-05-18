from colors import *


class ShortestRoutes:
    def __init__(self):
        self.routes = {}

    def get_route(self, start, end):
        if start in self.routes and end in self.routes[start]:
            return self.routes[start][end]
        else:
            return None

    def add_route(self, start, end, route):
        if start not in self.routes:
            self.routes[start] = {}
        self.routes[start][end] = route


# Funktion, die die kürzeste Route übersichtlich ausgibt
def print_route(route, total_time):
    #  Überschriften und Grundinformationen zur Route
    print(f"\n\n{bcolors.BOLD + bcolors.CYAN}{'-' * 40}\nROUTEN INFORMATION:\n{'-' * 40}{bcolors.RESET}\n")
    print(
        f"{bcolors.BOLD + bcolors.WHITE}Die kürzeste Route von {bcolors.UNDERLINE + bcolors.RED + route[0][0] + bcolors.RESET + bcolors.BOLD + bcolors.WHITE}🚩 zu {bcolors.UNDERLINE + bcolors.BLUE + route[-1][0] + bcolors.RESET + bcolors.BOLD + bcolors.WHITE}🏁 ist:{bcolors.RESET}\n")
    print(f"    {bcolors.WHITE}Startstation ist {bcolors.UNDERLINE + bcolors.RED + route[0][0]}{bcolors.RESET}🚩\n")

    current_line = route[0][1]  # Aktuelle Line (U-Bahn oder Straßenbahn)
    line_route = f"    {bcolors.PURPLE + bcolors.UNDERLINE}{current_line}: {bcolors.RESET}" if current_line is not None else ""  # Aktuelle Line wird ausgegeben, (außer sie ist NULL bei der Startstation, wo man NOCH in keiner Line ist)

    for i in range(1, len(route)):
        station, line, total_time_to_station = route[i]  # Stops werden aufgeteilt und in die Variablen Station, Line und Time unterteilt
        time = total_time_to_station - route[i-1][2] # Berechnung der Fahrzeit von der vorherigen Station zur aktuellen Station

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


