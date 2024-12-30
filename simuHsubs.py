import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir las variables
r, R = sp.symbols('r R')
A0 = 292

# Definir la expresión de H en función de r y R
H_expr = sp.sqrt(((A0 - sp.pi * r**2) / (sp.pi * (r + R)))**2 - (R - r)**2)

# Definir la expresión del volumen V en función de r y R
V_expr = (1/3) * sp.pi * H_expr * (r**2 + r*R + R**2)

# Convertir la expresión de V a una función numérica
V_func = sp.lambdify((r, R), V_expr, 'numpy')

# Crear una malla de valores para r y R
r_vals = np.linspace(1, 10, 100)
R_vals = np.linspace(1, 10, 100)
r_grid, R_grid = np.meshgrid(r_vals, R_vals)

# Calcular los valores de V en la malla
V_vals = V_func(r_grid, R_grid)

# Graficar V en función de r y R
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(r_grid, R_grid, V_vals, cmap='viridis')

ax.set_xlabel('r')
ax.set_ylabel('R')
ax.set_zlabel('V')
ax.set_title('Volumen del Cono Truncado en función de r y R')

plt.show()
