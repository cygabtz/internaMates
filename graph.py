import numpy as np
import matplotlib.pyplot as plt

# Definir la función V(r)
def V(r):
    return (1/3) * np.pi * np.sqrt(((292/np.pi - 3.6**2) / (3.6 + r))**2 - (3.6 - r)**2) * (3.6**2 + r**2 + 3.6*r)

# Crear un rango de valores para r
r_values = np.linspace(0.1, 10, 400)  # Ajusta el rango según sea necesario

# Calcular los valores de V(r)
V_values = V(r_values)

# Graficar la función
plt.plot(r_values, V_values)
plt.xlabel('r')
plt.ylabel('V(r)')
plt.title('Representación de la función V(r)')
plt.grid(True)
plt.show()
