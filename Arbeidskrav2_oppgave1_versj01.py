# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:17:55 2024

@author: oskar
"""

#%% Trinn 1: Be brukeren oppgi fødselsåret
# Bruk input-funksjonen til å hente fødselsår fra brukeren og konverter til heltall
alder = int(input('Hvilket år er du født? '))

#%% Trinn 2: Regn ut alderen i 2024
# Trekk fødselsåret fra 2024 for å finne alderen
alder_2024 = 2024 - alder

#%% Trinn 3: Skriv ut alderen til skjermen med en passende melding
# Bruk print-funksjonen til å vise resultatet
print(f'I løpet av året 2024 blir du {alder_2024} år gammel.') 


