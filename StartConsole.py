from colors import*


def programm_description():
    print(bcolors.HEADER + bcolors.BOLD + bcolors.UNDERLINE + bcolors.PURPLE + "WILLKOMMEN BEI PATH FINDER🚌🚦" + bcolors.RESET)

    print(bcolors.HEADER + bcolors.BOLD + bcolors.WHITE + "Dieses Programm kennt alle Wiener Verkehrsverbindungen, die mit U-bahn oder Strassenbahn erreichbar sind.\nSie können das Programm jederzeit mit 'exit' abbrechen." + bcolors.RESET)

    print(bcolors.HEADER + bcolors.BOLD + bcolors.UNDERLINE + bcolors.ORANGE + "\nWie suchen Sie nach dem Kürzesten Weg?" + bcolors.RESET)

    print(bcolors.HEADER + bcolors.BOLD + bcolors.WHITE + "Das Kommando sieht folgendermassen aus:" + bcolors.GREEN +"\nfilename_graph"+bcolors.RED+" start"+bcolors.BLUE+" ziel" + bcolors.RESET)

    print(bcolors.HEADER + bcolors.BOLD + bcolors.GREEN + "\nfilename_graph🗺️:"+bcolors.WHITE+" Filename, wo das Verkehrsnetz abgespeichert ist.")
    print(bcolors.HEADER + bcolors.BOLD + bcolors.RED + "start🚩:"+bcolors.WHITE+" Startstation.")
    print(bcolors.HEADER + bcolors.BOLD + bcolors.BLUE + "ziel🏁:"+bcolors.WHITE+" Zielstation.\n\n")
