import random


toegestane_doosnummers = list(range(1,5))

# Plaats de kat in een willekeurige doos
kat_positie = random.randint(1, 5)

# Spelbord
dozen = ["[]", "[]", "[]", "[]", "[]"]

# Game loop
while True:
    #Vraag gebruiker om een doosnummer
    doos_nummer = int(input("Kies een doosnummer (1 t/m 5): "))
    #if doos_nummer not in range(1,5):

    # Kijk of de kat in de gekozen doos zit
    if doos_nummer == kat_positie:
        print("Gefeliciteerd! Je hebt de kat gevonden.")
        #break
    
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

