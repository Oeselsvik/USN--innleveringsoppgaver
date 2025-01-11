#%% Importer nødvendige moduler
import numpy as np

#%% Definer funksjonen for konvertering
def grader_til_radianer(v_grad):
    """
    Konverterer en vinkel fra grader til radianer.
    """
    v_rad = v_grad * np.pi / 180  # Formelen for konvertering 
    return v_rad

#%% Hovedprogram
# Les inn gradtallet fra brukeren
v_grad = float(input('Skriv inn gradtallet: '))

# Bruk funksjonen til å konvertere
v_rad = grader_til_radianer(v_grad)

# Skriv ut resultatet
print(f'Gradtallet {v_grad:.2f} tilsvarer {v_rad:.4f} radianer.')

