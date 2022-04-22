myDict = {
    "Moritz": ["m", 21, "Vongole"],
    "Lukas": ["m", 30, "Steak"],
    "Emir": ["m", 20, "Bolognese"]
}


def add_item():
    show_list()
    while True:
        myDict[input("Wenn wollen sie den Wohnort hinzufügen\n")].insert(1, input("Wohnort eingeben\n"))
        if input("Wenn sie fertig sind \"FERTIG\" eingeben\n sonst Enter drücken\n") == "FERTIG":
            break


def show_list():
    for key, value in myDict.items():
        print(key, value)


def main():
    add_item()
    show_list()


main()