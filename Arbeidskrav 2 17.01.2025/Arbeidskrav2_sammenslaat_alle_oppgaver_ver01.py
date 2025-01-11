#%% Oppgave 1: Beregning av alder i 2025
# Bruk input-funksjonen til å hente fødselsår fra brukeren og konverter til heltall
alder = int(input('Hvilket år er du født? '))

# Regn ut alderen i 2025
alder_2025 = 2025 - alder

# Skriv ut alderen til skjermen med en passende melding
print(f'I løpet av året 2025 blir du {alder_2025} år gammel.') 

#%% Oppgave 2: Beregning av pizzaer til klassefest
import math

# Be brukeren om å skrive inn antall elever
antall_elever = int(input('Skriv inn antall elever: '))

# Beregn antall pizzaer
antall_pizzaer = math.ceil(antall_elever / 4)

# Skriv ut resultatet
print(f'Det må handles inn {antall_pizzaer} pizzaer til klassefesten.')

#%% Oppgave 3: Konvertering av grader til radianer
import numpy as np

def grader_til_radianer(v_grad):
    """
    Konverterer en vinkel fra grader til radianer.
    """
    v_rad = v_grad * np.pi / 180  # Formelen for konvertering 
    return v_rad

# Les inn gradtallet fra brukeren
v_grad = float(input('Skriv inn gradtallet: '))

# Bruk funksjonen til å konvertere
v_rad = grader_til_radianer(v_grad)

# Skriv ut resultatet
print(f'Gradtallet {v_grad:.2f} tilsvarer {v_rad:.4f} radianer.')

#%% Oppgave 4: Håndtering av dictionary med land
# Opprett en dictionary kalt 'data' med informasjon om ulike land
data = {
    "Norge": {"hovedstad": "Oslo", "innbyggere": 0.68},
    "Sverige": {"hovedstad": "Stockholm", "innbyggere": 1.66},
    "Danmark": {"hovedstad": "København", "innbyggere": 1.34},
    "England": {"hovedstad": "London", "innbyggere": 8.982}
}

# Ber brukeren skrive inn et land
land = input("Skriv inn et land (f.eks. England): ")

# Hent info fra dictionaryen hvis landet finnes
if land in data:
    hovedstad = data[land]["hovedstad"]
    innbyggere = data[land]["innbyggere"]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
    print(f"Beklager, informasjon om {land} finnes ikke i systemet.")

# Legge til nytt land
nytt_land = input("Skriv inn et nytt land du vil legge til: ")

if nytt_land in data:
    print(f"{nytt_land} finnes allerede i systemet. Ingen ny informasjon er lagt til.")
else:
    hovedstad = input(f"Hva er hovedstaden i {nytt_land}? ")
    innbyggere = float(input(f"Hvor mange innbyggere (i mill.) er det i {hovedstad}? "))
    data[nytt_land] = {"hovedstad": hovedstad, "innbyggere": innbyggere}
    print(f"{nytt_land} er lagt til i systemet.")

# Skriver ut oppdatert dictionary
print("Oppdatert informasjon i dictionaryen:")
for land, info in data.items():
    print(f"{land}: Hovedstad = {info['hovedstad']}, Innbyggere = {info['innbyggere']} mill.")

#%% Oppgave 5: Beregning av areal og omkrets
import math

def figur_egenskaper(a, b):
    radius = a / 2
    areal_halvsirkel = math.pi * radius**2 / 2
    areal_trekant = (a * b) / 2
    totalt_areal = areal_halvsirkel + areal_trekant
    
    omkrets_halvsirkel = math.pi * radius
    hypotenus = math.sqrt(a**2 + b**2)
    ytre_omkrets = b + hypotenus + omkrets_halvsirkel

    return totalt_areal, ytre_omkrets

a = float(input("Skriv inn lengden på a (grunnlinjen til trekanten): "))
b = float(input("Skriv inn lengden på b (høyden til trekanten): "))

areal, omkrets = figur_egenskaper(a, b)
print(f"Arealet av figuren er: {areal:.2f}")
print(f"Den ytre omkretsen av figuren er: {omkrets:.2f}")

#%% Oppgave 6: Plotting av funksjonen f(x) = -x^2 - 5
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
f_x = -x**2 - 5

plt.plot(x, f_x, label="f(x) = -x^2 - 5")
plt.title("Plot av funksjonen f(x) = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
