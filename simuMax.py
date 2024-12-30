import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Definir las variables
r, R = sp.symbols('r R')
A0 = 292

# Definir la expresión de H en función de r y R
H_expr = sp.sqrt(((A0 - sp.pi * r**2) / (sp.pi * (r + R)))**2 - (R - r)**2)

# Definir la expresión del volumen V en función de r y R
V_expr = (1/3) * sp.pi * H_expr * (r**2 + r*R + R**2)

# Convertir la expresión de V a una función numérica
V_func = sp.lambdify((r, R), V_expr, 'numpy')

# Definir la función objetivo para minimizar (negativo del volumen)
def objective(x):
    r_val, R_val = x
    return -V_func(r_val, R_val)

# Definir las restricciones y límites
constraints = [{'type': 'ineq', 'fun': lambda x: x[0]},  # r >= 0
               {'type': 'ineq', 'fun': lambda x: x[1]},  # R >= 0
               {'type': 'ineq', 'fun': lambda x: 10 - x[0]},  # r <= 10
               {'type': 'ineq', 'fun': lambda x: 10 - x[1]}]  # R <= 10

# Definir los límites para r y R
bounds = [(0, 10), (0, 10)]

# Realizar la optimización
result = minimize(objective, [5, 5], bounds=bounds, constraints=constraints)

# Obtener los valores óptimos de r y R
r_opt, R_opt = result.x
V_opt = -result.fun

print(f"Valores óptimos: r = {r_opt}, R = {R_opt}, Volumen máximo = {V_opt}")

# Crear una malla de valores para r y R
r_vals = np.linspace(0, 10, 100)
R_vals = np.linspace(0, 10, 100)
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

# Marcar el punto óptimo
ax.scatter(r_opt, R_opt, V_opt, color='r', s=100, label='Óptimo')
ax.legend()

plt.show()
