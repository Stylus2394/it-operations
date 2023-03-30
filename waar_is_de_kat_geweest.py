import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


toegestane_doosnummers = list(range(1,6))
aantal_pogingen = 0

# Plaats de kat in een willekeurige doos
kat_positie = random.randint(1, 5)

# Spelbord
dozen = ["[]", "[]", "[]", "[]", "[]"]

# Game loop
while True:
    print(bcolors.HEADER, "De kat zit in doos", kat_positie, bcolors.ENDC)

    #Vraag gebruiker om een doosnummer
    doos_nummer = int(input("Kies een doosnummer (1 t/m 5): "))

    
    if doos_nummer not in toegestane_doosnummers:
        #doos_nummer = int(input("2. Kies een doosnummer (1 t/m 5): "))
        print(bcolors.FAIL, "Vul een nummer in tussen 1-5", bcolors.ENDC)
        continue       

    aantal_pogingen += 1

    print(bcolors.OKBLUE, "Aantal pogingen:", aantal_pogingen, bcolors.ENDC)

    # Kijk of de kat in de gekozen doos zit
    if doos_nummer == kat_positie:
        print(bcolors.OKGREEN, "Gefeliciteerd! Je hebt de kat gevonden.", bcolors.ENDC)
        print(bcolors.OKCYAN, "Je had", aantal_pogingen , " pogingen nodig om de kat te vinden.", bcolors.ENDC)    
    
    # Verplaats de kat
    if kat_positie == 1:
        kat_positie += 1
    elif kat_positie == 5:
        kat_positie -= 1
    else:
        kat_positie += random.choice([-1, 1])

    # Update het spelbord
    dozen = ["[]" if i != kat_positie - 1 else "[Kat]" for i in range(5)]
    print("  ".join(dozen))

