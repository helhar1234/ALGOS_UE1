from colors import *


class ShortestRoutes:  # Klasse für die kürzesten Routen
    def __init__(self):  # Konstruktor
        self.routes = {}  # Dictionary für die Routen

    def get_route(self, start, end):  # Funktion, die die Route aus dem Dictionary holt
        if start in self.routes and end in self.routes[start]:  # Wenn die Route existiert, wird sie zurückgegeben
            return self.routes[start][end]
        else:  # Wenn die Route nicht existiert, wird None zurückgegeben
            return None

    def add_route(self, start, end, route):  # Funktion, die die Route zum Dictionary hinzufügt
        if start not in self.routes:  # Wenn die Startstation nicht im Dictionary ist, wird sie hinzugefügt
            self.routes[start] = {}  # Dictionary für die Endstationen wird erstellt
        self.routes[start][end] = route  # Route wird zum Dictionary hinzugefügt


# Funktion, die die kürzeste Route übersichtlich ausgibt
def print_route(route, total_time):
    # Überschriften und Grundinformationen zur Route
    print(f"\n\n{bcolors.BOLD + bcolors.CYAN}{'-' * 40}\nROUTEN INFORMATION:\n{'-' * 40}{bcolors.RESET}\n")
    print(f"{bcolors.BOLD + bcolors.WHITE}Die kürzeste Route von {bcolors.UNDERLINE + bcolors.RED + route[0][0] + bcolors.RESET + bcolors.BOLD + bcolors.WHITE}🚩 zu {bcolors.UNDERLINE + bcolors.BLUE + route[-1][0] + bcolors.RESET + bcolors.BOLD + bcolors.WHITE}🏁 ist:{bcolors.RESET}\n")
    print(f"    {bcolors.WHITE}Startstation ist {bcolors.UNDERLINE + bcolors.RED + route[0][0]}{bcolors.RESET}🚩\n")

    current_line = None  # Variable für die aktuelle Linie
    line_route = ""  # Variable für die Route der aktuellen Linie

    for i in range(1, len(route)):  # Für jede Station in der Route
        station, line, _ = route[i]  # Stops werden aufgeteilt und in die Variablen Station, Line und Time unterteilt

        if line != current_line:  # wenn umgestiegen werden soll
            if current_line is not None:  # wird nur ausgegeben, wenn der Umstieg nicht die Startstation ist
                print(line_route.rstrip())  # unnötige Leerzeichen werden von der Route der einzelnen Linie entfernt
                print(f"    {bcolors.UNDERLINE + bcolors.BOLD + bcolors.ORANGE}Umstieg{bcolors.RESET + bcolors.WHITE}: Steige von Linie {bcolors.UNDERLINE + bcolors.PURPLE + current_line + bcolors.RESET + bcolors.WHITE} um auf Linie {bcolors.UNDERLINE + bcolors.PURPLE + line + bcolors.RESET + bcolors.WHITE} in der Station {bcolors.UNDERLINE + bcolors.ORANGE + route[i - 1][0]}{bcolors.RESET}\n")
            current_line = line  # Neue Linie wird zur aktuellen Linie
            line_route = f"    {bcolors.UNDERLINE + bcolors.PURPLE + current_line + bcolors.RESET}: {bcolors.WHITE}{route[i - 1][0]} -> {bcolors.WHITE}{station}{bcolors.RESET} "
        else:  # wenn nicht umgestiegen werden muss
            line_route += f" -> {bcolors.WHITE}{station}"

    print(line_route.rstrip())  # unnötige Leerzeichen werden von der Route der einzelnen Linie entfernt
    # Endausgabe
    print(f"\n    {bcolors.WHITE}Zielstation {bcolors.UNDERLINE + bcolors.BLUE + route[-1][0] + bcolors.RESET + bcolors.WHITE}🏁 wurde erreicht!{bcolors.RESET}")
    print(f"\n{bcolors.BOLD + bcolors.WHITE}Gesamte Fahrzeit: {bcolors.GREEN + str(total_time)} Minuten{bcolors.RESET}\n")
    print(f"{bcolors.BOLD + bcolors.CYAN}{'-' * 40}{bcolors.RESET}\n\n")
