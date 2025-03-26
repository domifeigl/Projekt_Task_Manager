

def hlavni_menu():
    option = input("Správce úkolů - Hlavní menu\n\r1. Přidat nový úkol\n\r2. Zobrazit všechny úkoly\n\r3. Odstranit úkol\n\r4. Konec programu\n\rVyberte možnost (1-4): ")
    print("\n")
    return int(option)


def pridat_ukol():
    nazev_ukolu = input("Zadejte název úkolu: ")
    popis_ukolu = input("Zadejte popis úkolu: ")

    if(nazev_ukolu == "" or popis_ukolu == ""):
        print("Prosím vyplňte název a popis úkolu.\n\r")
        pridat_ukol()
    else:
        novy_ukol = nazev_ukolu + " - " + popis_ukolu
        print(f"Úkol {nazev_ukolu} byl přidán.\n\r")
        return novy_ukol


def zobrazit_ukoly(ukoly):
    for index, hodnota in enumerate(ukoly, start =1):
        print("Seznam úkolů:")
        print(f"{index}. {hodnota}\n\r")


def odstranit_ukol(ukoly):
    index = input("Zadejte číslo úkolu, který chcete odstranit: ")
    index = int(index)
    index -= 1
    if(0 <= index < len(ukoly)):
        vyber_ukolu = ukoly[index]
        print(f"Úkol {vyber_ukolu} byl odstraněn.\n\r")
    else:
        print(f"Úkol pod číslem {index + 1} neexistuje.")
        odstranit_ukol(ukoly)


option = 0
ukoly = []

while option != 4:
    option = 0
    option= hlavni_menu()

    if(option <= 0 or option >4):
        print("Zadaná možnost neexistuje. Vbyrete možnost 1-4.\n\r")
    
    if(option == 1):
        ukoly.append(pridat_ukol())
    
    if(option == 2):
        zobrazit_ukoly(ukoly)
    
    if(option == 3):
        zobrazit_ukoly(ukoly)
        odstranit_ukol(ukoly)
   
    if(option == 4):
        print("Konec programu.")
    

