# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:19:03 2024

@author: oskar
"""

# Antall kjørte kilometer per år
antall_km_per_år = 8000  # endre selv viss du vil

# Bilforsikringskostnad per år
forsikring_elbil = 5000  # kr/år
forsikring_bensinbil = 7500  # kr/år

# Trafikkforsikringsavgift per dag (likt for for begge biltyper)
trafikkforsikringsavgift_dag = 8.38
trafikkforsikringsavgift_per_år = trafikkforsikringsavgift_dag * 365

# Drivstoffkostnad per km
strømpris_kwh = 2.00  # kr/kWh
drivstoffbruk_elbil = 0.2  # kWh/km
drivstoffpris_bensinbil = 1.0  # kr/km

# Bompengeavgift per km
bomavgift_elbil = 0.1  # kr/km
bomavgift_bensinbil = 0.3  # kr/km

# Årlige drivstoffkostnader
drivstoffkostnad_elbil = antall_km_per_år * drivstoffbruk_elbil * strømpris_kwh
drivstoffkostnad_bensinbil = antall_km_per_år * drivstoffpris_bensinbil

# Årlige bomkostnader
bomkostnad_elbil = antall_km_per_år * bomavgift_elbil
bomkostnad_bensinbil = antall_km_per_år * bomavgift_bensinbil

# Totale årlige kostnader for begge biltyper
total_kostnad_elbil = forsikring_elbil + trafikkforsikringsavgift_per_år + drivstoffkostnad_elbil + bomkostnad_elbil
total_kostnad_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift_per_år + drivstoffkostnad_bensinbil + bomkostnad_bensinbil

# Årlig kostnadsdifferanse
kostnadsdifferanse = total_kostnad_bensinbil - total_kostnad_elbil

# Presentasjon av resultater
print("Årlige totalkostnader:")
print(f"Elbil: {total_kostnad_elbil:.2f} kr")
print(f"Bensinbil: {total_kostnad_bensinbil:.2f} kr")
print(f"Årlig kostnadsdifferanse: {kostnadsdifferanse:.2f} kr")
