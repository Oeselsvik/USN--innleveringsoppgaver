#%% Funksjon for beregning av areal og ytre omkrets
import math

def figur_egenskaper(a, b):
    # Beregning av radius for halvsirkelen
    radius = a / 2

    # Beregning av areal
    areal_halvsirkel = math.pi * radius**2 / 2
    areal_trekant = (a * b) / 2
    totalt_areal = areal_halvsirkel + areal_trekant

    # Beregning av ytre omkrets
    omkrets_halvsirkel = math.pi * radius  # Halve omkretsen av en sirkel
    hypotenus = math.sqrt(a**2 + b**2)  # Pythagoras for hypotenusen i trekanten
    ytre_omkrets = b + hypotenus + omkrets_halvsirkel

    # Bygg forklaringer
    forklaring_areal = (
        f"Halvsirkelens areal beregnes som π * r² / 2, hvor r = a/2 = {radius:.2f}. "
        f"Dette gir arealet {areal_halvsirkel:.2f}.\n"
        f"Trekantens areal beregnes som (g * h) / 2, hvor g = {a} og h = {b}. "
        f"Dette gir arealet {areal_trekant:.2f}.\n"
        f"Totalt areal er summen av disse, som blir {totalt_areal:.2f}."
    )

    forklaring_omkrets = (
        f"Halvsirkelens omkrets er π * r = {omkrets_halvsirkel:.2f}.\n"
        f"Hypotenusen i trekanten beregnes med Pythagoras' setning som √(a² + b²), "
        f"som gir {hypotenus:.2f}.\n"
        f"Den ytre omkretsen er summen av høyden b = {b}, hypotenusen {hypotenus:.2f}, "
        f"og halvsirkelens omkrets {omkrets_halvsirkel:.2f}, som totalt blir {ytre_omkrets:.2f}."
    )

    return totalt_areal, ytre_omkrets, forklaring_areal, forklaring_omkrets

#%% Hovedprogram
if __name__ == "__main__":
    # Brukerinput for a og b
    print("Velkommen! Dette programmet beregner arealet og den ytre omkretsen av figuren.")
    
    def les_inndata(prompt):
        while True:
            try:
                verdi = float(input(prompt))
                if verdi <= 0:
                    print("Vennligst skriv inn et positivt tall.")
                    continue
                return verdi
            except ValueError:
                print("Ugyldig input. Vennligst skriv inn et tall.")
    
    a = les_inndata("Skriv inn lengden på a (grunnlinjen til trekanten): ")
    b = les_inndata("Skriv inn lengden på b (høyden til trekanten): ")

    # Beregning
    areal, omkrets, forklaring_areal, forklaring_omkrets = figur_egenskaper(a, b)

    # Utskrift av detaljerte forklaringer og resultater
    print("\nBeregning av areal:")
    print(forklaring_areal)
    print("\nBeregning av ytre omkrets:")
    print(forklaring_omkrets)
    print("\nOppsummert:")
    print(f"Arealet av figuren er: {areal:.2f}")
    print(f"Den ytre omkretsen av figuren er: {omkrets:.2f}")

