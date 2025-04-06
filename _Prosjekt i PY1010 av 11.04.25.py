#!/usr/bin/env python
# coding: utf-8

# In[17]:


#%% Importer nødvendige biblioteker
# Vi bruker pandas for å lese Excel-filen, numpy for numeriske operasjoner, og matplotlib for plotting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[27]:


#%% Del a) Les inn Excel-filen og lagre data i arrays
# Les inn dataen fra Excel-filen
filnavn = 'support_uke_24.xlsx'
df = pd.read_excel(filnavn)

# Lagre hver kolonne i separate arrays
u_dag = df.iloc[:, 0].to_numpy()  # Ukedag
kl_slett = df.iloc[:, 1].to_numpy()  # Klokkeslett
varighet = df.iloc[:, 2].to_numpy()  # Samtalevarighet (hh:mm:ss eller tidsobjekt)
score = df.iloc[:, 3].to_numpy()  # Kundens tilfredshet

#%% Konverter samtalevarighet til sekunder
varighet_sekunder = []

for v in varighet:
    if isinstance(v, str):
        # Hvis tekstformat: "hh:mm:ss"
        h, m, s = map(int, v.split(":"))
        sekunder = h * 3600 + m * 60 + s
    else:
        # Hvis tidsobjekt med .total_seconds()
        sekunder = v.total_seconds() if hasattr(v, 'total_seconds') else v
    varighet_sekunder.append(sekunder)

varighet_sekunder = np.array(varighet_sekunder)


# In[65]:


#%% Del b) Antall henvendelser per ukedag

# Tell hvor mange ganger hver ukedag forekommer
unike_ukedager, antall = np.unique(u_dag, return_counts=True)

# Lag dictionary
ukedag_til_antall = dict(zip(unike_ukedager, antall))

# Ønsket rekkefølge
rekkefolge = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag']
sorterte_verdier = [ukedag_til_antall[d] for d in rekkefolge]

# Finn høyeste verdi for å fargekode den
maksverdi = max(sorterte_verdier)

# Velg farge per søyle
farger = ['darkblue' if verdi == maksverdi else 'cornflowerblue' for verdi in sorterte_verdier]

# Tegn søylediagram
plt.figure(figsize=(8, 5))
bars = plt.bar(rekkefolge, sorterte_verdier, color=farger, alpha=0.9)

plt.xlabel('Ukedag')
plt.ylabel('Antall henvendelser')
plt.title('Antall henvendelser per ukedag')

# Legg på tall over søylene
for bar in bars:
    høyde = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, høyde + 1,
             f'{høyde:.0f}', ha='center', va='bottom', fontsize=10)

plt.ylim(top=maksverdi + 10)
plt.show()


# In[35]:


#%% Del c) Finn korteste og lengste samtaletid (minutter og sekunder)
min_samtale = np.min(varighet_sekunder)
maks_samtale = np.max(varighet_sekunder)

# Konverter til minutter og sekunder
min_minutter = int(min_samtale // 60)
min_sekunder = int(min_samtale % 60)

maks_minutter = int(maks_samtale // 60)
maks_sekunder = int(maks_samtale % 60)

# Vis resultatet
print(f'Minste samtaletid: {min_minutter} minutter og {min_sekunder} sekunder')
print(f'Lengste samtaletid: {maks_minutter} minutter og {maks_sekunder} sekunder')


# In[41]:


#%% Del d) Beregn gjennomsnittlig samtaletid
gjennomsnitt_samtale = np.mean(varighet_sekunder)

# Konverter til minutter og sekunder
gj_minutter = int(gjennomsnitt_samtale // 60)
gj_sekunder = int(gjennomsnitt_samtale % 60)

print(f'Gjennomsnittlig samtaletid: {gj_minutter} minutter og {gj_sekunder} sekunder')


# In[45]:


#%% Del e) Henvendelser per 2-timers bolk
# Definer tidsintervaller
intervaller = [(8, 10), (10, 12), (12, 14), (14, 16)]
resultater = []

# Konverter klokkeslett til timer
kl_timer = np.array([int(t.split(':')[0]) for t in kl_slett])

# Tell antall henvendelser i hver tidsperiode
for start, slutt in intervaller:
    antall_henv = np.sum((kl_timer >= start) & (kl_timer < slutt))
    resultater.append(antall_henv)

# Visualiser som sektordiagram
etiketter = [f'{start}-{slutt}' for start, slutt in intervaller]
plt.figure(figsize=(7, 7))
plt.pie(resultater, labels=etiketter, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'orange'])
plt.title('Henvendelser per 2-timers bolk')
plt.show()



# In[57]:


#%% Del f) Beregn NPS (Net Promoter Score) med norske begreper

# Filtrer bort manglende svar (NaN)
score_renset = score[~pd.isna(score)]

# Antall totalt som har gitt tilbakemelding
totalt_antall = len(score_renset)

# Tell antall kunder i hver kategori
antall_negative = np.sum((score_renset >= 1) & (score_renset <= 6))
antall_noytrale = np.sum((score_renset == 7) | (score_renset == 8))
antall_positive = np.sum((score_renset == 9) | (score_renset == 10))

# Beregn prosentandeler
prosent_negative = (antall_negative / totalt_antall) * 100
prosent_positive = (antall_positive / totalt_antall) * 100

# Beregn NPS
nps = prosent_positive - prosent_negative

# Skriv ut resultatet
print("=== NPS-beregning ===")
print(f"Antall svar totalt: {totalt_antall}")
print(f"Negative kunder:  {antall_negative} ({prosent_negative:.1f}%)")
print(f"Nøytrale kunder:  {antall_noytrale}")
print(f"Positive kunder:  {antall_positive} ({prosent_positive:.1f}%)")
print(f"--> NPS = {nps:.1f}")


# In[59]:


#%% Etiketter og data (ikke en del av prosjektoppgaven)

etiketter = ['Negative', 'Nøytrale', 'Positive']
verdier = [antall_kritikere, antall_noytrale, antall_ambassadoerer]
farger = ['red', 'gold', 'green']

# Lag kakediagram
plt.figure(figsize=(6, 6))
plt.pie(verdier, labels=etiketter, colors=farger, autopct='%1.1f%%', startangle=140)
plt.title('Fordeling av kundetilfredshet')
plt.axis('equal')  # Sørger for rund sirkel
plt.show()


# In[63]:


# Visuell representasjon av NPS som "termometer" (ikke en del av prosjektoppgaven)
plt.figure(figsize=(8, 1.5))
plt.axhline(y=0, xmin=0, xmax=1, color='lightgray', linewidth=20)

# Fargede segmenter
plt.axhline(y=0, xmin=0, xmax=0.33, color='red', linewidth=20, label='Negative')
plt.axhline(y=0, xmin=0.33, xmax=0.66, color='gold', linewidth=20, label='Nøytrale')
plt.axhline(y=0, xmin=0.66, xmax=1, color='green', linewidth=20, label='Positive')

# Beregn NPS-plassering (fra -100 til +100 → normalisert til 0–1)
nps_normalisert = (nps + 100) / 200

# Marker punktet på linjen
plt.plot(nps_normalisert, 0, marker='o', color='black', markersize=12)
plt.text(nps_normalisert, 0.05, f'NPS = {nps:.1f}', ha='center', fontsize=12)

# Fjern akser og vis tittel
plt.axis('off')
plt.title('Net Promoter Score (NPS)', fontsize=13)
plt.show()


# In[ ]:




