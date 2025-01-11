

#%% Be brukeren oppgi fødselsåret
# Bruk input-funksjonen til å hente fødselsår fra brukeren og konverter til heltall
alder = int(input('Hvilket år er du født? '))

#%% Regn ut alderen i 2025
# Trekk fødselsåret fra 2025 for å finne alderen
alder_2025 = 2025 - alder

#%% Skriv ut alderen til skjermen med en passende melding
# Bruk print-funksjonen til å vise resultatet
print(f'I løpet av året 2025 blir du {alder_2025} år gammel.') 


