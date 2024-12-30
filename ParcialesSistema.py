import sympy as sp

# Definir las variables
r, R, H, lambda_ = sp.symbols('r R H lambda')
A0 = sp.symbols('A0')

# Definir la función de Lagrange
V = (1/3) * sp.pi * H * (r**2 + r*R + R**2)
A = sp.pi * (r + R) * sp.sqrt((R - r)**2 + H**2) + sp.pi * r**2
L = V + lambda_ * (A - A0)

# Calcular las derivadas parciales
dL_dr = sp.diff(L, r)
dL_dR = sp.diff(L, R)
dL_dH = sp.diff(L, H)
dL_dlambda = sp.diff(L, lambda_)

# Resolver el sistema de ecuaciones
solutions = sp.solve([dL_dr, dL_dR, dL_dH, dL_dlambda], (r, R, H, lambda_))

# Mostrar las soluciones
print(solutions)
