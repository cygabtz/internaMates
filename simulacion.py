import numpy as np
import matplotlib.pyplot as plt

def calculate_volume(H, r, R=3.7):
    """Calcula el volumen del cono truncado."""
    return (np.pi * H / 3) * (R**2 + r**2 + R * r)

def calculate_area(H, r, R=3.7):
    """Calcula el área superficial del cono truncado."""
    G = np.sqrt(H**2 + (R - r)**2)  # Generatriz
    return np.pi * r**2 + np.pi * (R + r) * G

# R = 3.7 (constante)
R = 3.7

# Rango de valores para H y r
H_values = np.linspace(1, 20, 100)  # Altura entre 1 y 20 cm
r_values = np.linspace(1, 10, 100)  # Radio menor entre 1 y 10 cm

# Crear matrices para H y r
H, r = np.meshgrid(H_values, r_values)

# Calcular V y A
V = calculate_volume(H, r, R)
A = calculate_area(H, r, R)

# Crear las gráficas
fig = plt.figure(figsize=(12, 6))

# Gráfica del volumen
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(H, r, V, cmap='viridis')
ax1.set_title('Volumen del Cono Truncado')
ax1.set_xlabel('Altura (H) [cm]')
ax1.set_ylabel('Radio menor (r) [cm]')
ax1.set_zlabel('Volumen (V) [cm³]')

# Gráfica del área superficial
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(H, r, A, cmap='plasma')
ax2.set_title('Área Superficial del Cono Truncado')
ax2.set_xlabel('Altura (H) [cm]')
ax2.set_ylabel('Radio menor (r) [cm]')
ax2.set_zlabel('Área (A) [cm²]')

plt.tight_layout()
plt.show()