while True:
    dier = input("Voer een dier in, of geef <enter> om af te sluiten: ")
    if len(dier) == 0:
        print("Ok, tot ziens")
        break
    print("Uw invoer is", len(dier), "lang")