from sympy import symbols, Eq, solve, pi, sqrt, re, im

# Definir las variables
R, H, l = symbols('R H l', real=True, positive=True)
r = 2.7

# Definir las ecuaciones
eq1 = Eq(pi*H / 3 * (2*R + r), l * (pi * (2*R**2 - 2*R*r + H**2)) / (sqrt(H**2 + (R-r)**2)))
eq2 = Eq(pi / 3 * (R**2 + r**2 + R*r), l * (pi * H * (R+r)) / (sqrt(H**2 + (R-r)**2)))
eq3 = Eq(pi * (r**2 + (R+r) * sqrt((R-r)**2 + H**2)) - 292, 0)

# Resolver el sistema de ecuaciones
sol = solve((eq1, eq2, eq3), (R, H, l), dict=True)

# Filtrar soluciones reales y positivas
sol_real = [s for s in sol if all(re(val) > 0 and im(val) == 0 for val in s.values())]

# Imprimir las soluciones
print(sol_real)