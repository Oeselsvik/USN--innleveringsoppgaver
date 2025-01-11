#%% Importere nødvendige biblioteker
import numpy as np  # For numeriske beregninger
import matplotlib.pyplot as plt  # For plotting

#%% Definere intervallet for x og funksjonen f(x)
# Opprette en array med 200 punkter mellom -10 og 10
x = np.linspace(-10, 10, 200)

# Beregne verdiene til funksjonen f(x) = -x^2 - 5
f_x = -x**2 - 5

#%% Plotting av funksjonen
# Opprette selve plottet
plt.plot(x, f_x, label="f(x) = -x^2 - 5")

# Legge til tittel og akselmerking
plt.title("Plot av funksjonen f(x) = -x^2 - 5")
plt.xlabel("x")  # x-akse merking
plt.ylabel("f(x)")  # y-akse merking

# Legge til rutenett og en forklaring (legend)
plt.grid(True)
plt.legend()

# Vise plottet
plt.show()
