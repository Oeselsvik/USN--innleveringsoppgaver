#%% Importer nødvendig modul
# math-modulen brukes for å runde opp til nærmeste heltall
import math

#%% Input fra bruker
# Be brukeren om å skrive inn antall elever
antall_elever = int(input('Skriv inn antall elever: '))

#%% Beregn antall pizzaer
# Hver elev spiser 1/4 pizza. Antall pizzaer beregnes ved å dele antall elever på 4
# math.ceil() brukes for å runde opp til nærmeste heltall
antall_pizzaer = math.ceil(antall_elever / 4)

#%% Skriv ut resultatet
# Resultatet vises som en setning der antall pizzaer er et heltall
print(f'Det må handles inn {antall_pizzaer} pizzaer til klassefesten.')
