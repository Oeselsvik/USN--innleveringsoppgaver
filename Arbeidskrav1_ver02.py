# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 09:29:07 2024

@author: oskar
"""

#%% Antall kjoerte kilometer per aar
antall_km_per_aar = 10000  # Du kan endre dette etter eget forbruk

#%% Forsikringskostnad per aar
forsikring_elbil = 5000  # kr/aar
forsikring_bensinbil = 7500  # kr/aar

#%% Trafikkforsikringsavgift per dag (for begge biltyper)
trafikkforsikringsavgift_dag = 8.38
trafikkforsikringsavgift_per_aar = trafikkforsikringsavgift_dag * 365

#%% Drivstoffkostnad per km
stroempris_kwh = 2.00  # kr/kWh
drivstoffbruk_elbil = 0.2  # kWh/km
drivstoffpris_bensinbil = 1.0  # kr/km

#%% Bomavgift per km
bomavgift_elbil = 0.1  # kr/km
bomavgift_bensinbil = 0.3  # kr/km

#%% Aarlige drivstoffkostnader
drivstoffkostnad_elbil = antall_km_per_aar * drivstoffbruk_elbil * stroempris_kwh
drivstoffkostnad_bensinbil = antall_km_per_aar * drivstoffpris_bensinbil

#%% Aarlige bomkostnader
bomkostnad_elbil = antall_km_per_aar * bomavgift_elbil
bomkostnad_bensinbil = antall_km_per_aar * bomavgift_bensinbil

#%% Totale aarlige kostnader
total_kostnad_elbil = forsikring_elbil + trafikkforsikringsavgift_per_aar + drivstoffkostnad_elbil + bomkostnad_elbil
total_kostnad_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift_per_aar + drivstoffkostnad_bensinbil + bomkostnad_bensinbil

#%% Aarlig kostnadsdifferanse
kostnadsdifferanse = total_kostnad_bensinbil - total_kostnad_elbil

#%% Presentasjon av resultater
print("Aarlige totalkostnader:")
print(f"Elbil: {total_kostnad_elbil:.2f} kr")
print(f"Bensinbil: {total_kostnad_bensinbil:.2f} kr")
print(f"Aarlig kostnadsdifferanse: {kostnadsdifferanse:.2f} kr")
