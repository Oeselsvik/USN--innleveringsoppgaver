#%% a) Opprett en dictionary med land, hovedstad og antall innbyggere
# Opprett en dictionary kalt 'data' med informasjon om ulike land
data = {
    "Norge": {"hovedstad": "Oslo", "innbyggere": 0.68},
    "Sverige": {"hovedstad": "Stockholm", "innbyggere": 1.66},
    "Danmark": {"hovedstad": "København", "innbyggere": 1.34},
    "England": {"hovedstad": "London", "innbyggere": 8.982}
}

#%% b) Program som skriver ut hovedstad og innbyggere for et valgt land
# Ber brukeren skrive inn et land
land = input("Skriv inn et land (f.eks. England): ")

# Hent info fra dictionaryen hvis landet finnes
if land in data:
    hovedstad = data[land]["hovedstad"]
    innbyggere = data[land]["innbyggere"]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
    print(f"Beklager, informasjon om {land} finnes ikke i systemet.")

#%% c) Program som lar brukeren legge til et nytt land i dictionaryen
# Ber brukeren legge til et nytt land
nytt_land = input("Skriv inn et nytt land du vil legge til: ")

# Sjekk om landet allerede finnes
if nytt_land in data:
    print(f"{nytt_land} finnes allerede i systemet. Ingen ny informasjon er lagt til.")
else:
    # Ber om informasjon om det nye landet
    hovedstad = input(f"Hva er hovedstaden i {nytt_land}? ")
    innbyggere = float(input(f"Hvor mange innbyggere (i mill.) er det i {hovedstad}? "))
    data[nytt_land] = {"hovedstad": hovedstad, "innbyggere": innbyggere}
    print(f"{nytt_land} er lagt til i systemet.")

# Skriver ut oppdatert dictionary
print("Oppdatert informasjon i dictionaryen:")
for land, info in data.items():
    print(f"{land}: Hovedstad = {info['hovedstad']}, Innbyggere = {info['innbyggere']} mill.")


