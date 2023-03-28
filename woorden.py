# Spelen met woorden
# Wat Python code om alvast aan de slag te kunnen
# Het bestand 'woorden.txt.zip' staat op deze pagina

bestand_met_woorden = open("woorden.txt", "rt") # alleen-lezen van tekst
lijst_met_woorden = bestand_met_woorden.readlines()
#lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()

aantal_woorden = len(lijst_met_woorden)
print(aantal_woorden)