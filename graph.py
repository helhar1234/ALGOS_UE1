class Graph: # Klasse die den Graphen repräsentiert
    def __init__(self): # Konstruktor
        self.network = {} # Dictionary das die Stationen und ihre Verbindungen speichert

    def add_station(self, station): # Methode um Stationen hinzuzufügen (wenn sie noch nicht existieren)
        if station not in self.network: # Wenn die Station noch nicht im Dictionary ist
            self.network[station] = {}  # Füge sie hinzu

    def add_route(self, station1, station2, weight=1, line=None): # Methode um Verbindungen zwischen Stationen hinzuzufügen
        self.add_station(station1) # Füge die Stationen hinzu, falls sie noch nicht existieren
        self.add_station(station2) # Füge die Stationen hinzu, falls sie noch nicht existieren
        self.network[station1][station2] = (weight, line) # Füge die Verbindung hinzu (mit Gewicht und Linie)
        self.network[station2][station1] = (weight, line) # Füge die Verbindung hinzu (mit Gewicht und Linie)

    def show_network(self): # Methode um das Netzwerk auszugeben
        for station in self.network: # Für jede Station im Dictionary
            print(station, "->", self.network[station]) # Gib die Station und ihre Verbindungen aus (als Dictionary)

    def station_exists(self, station): # Methode um zu überprüfen ob eine Station existiert
        return station in self.network # Gib zurück ob die Station im Dictionary ist (True/False)

    def get_matrix(self): # Methode um die Adjazenzmatrix zu bekommen
        stations = list(self.network.keys()) # Erstelle eine Liste mit allen Stationen im Dictionary
        matrix = [[0 for _ in range(len(stations))] for _ in range(len(stations))] # Erstelle eine Matrix mit der Größe der Anzahl der Stationen
        for i, station1 in enumerate(stations): # Für jede Station im Dictionary
            for j, station2 in enumerate(stations): # Für jede Station im Dictionary
                if station2 in self.network[station1]: # Wenn die Stationen verbunden sind
                    matrix[i][j] = self.network[station1][station2][0] # Setze das Gewicht in die Matrix ein
        return matrix # Gib die Matrix zurück
