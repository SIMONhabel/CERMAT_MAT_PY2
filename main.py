#úloha 4
import sympy as sp

a = sp.Symbol('a')
expr1 = (1 - 2*a)**2
# Převedení výrazu do kódu
expr2 = (1 + 4*a**2) / (1 + 2*a) - 2*a
# Vydělení a zjednodušení (simplify)
result = sp.simplify(expr1 / expr2)

print(f"Zjednodušený výraz: {result}")

# úloha 8
x = sp.Symbol('x') # plat běžných zaměstnanců
# Rovnice váženého průměru: 1/3 *(x + 6000) + 2/3 * x = 46200
eq = sp.Eq((x + 6000)/3 + 2*x/3, 46200)

plat_bezny = sp.solve(eq, x)[0]
plat_senior = plat_bezny + 6000

print(f"Průměrný plat seniorního zaměstnance: {plat_senior} Kč")

#úloha 9
def f(x):
    return 0.5 * x**2 - 2

# Souřadnice y
y_A = f(4)
y_B = f(0)

# Výpočet směrnice (k) a posunu (q) přímky y = kx + q
q = y_B # protože B má x = 0, y udává přímo q
k = (y_A - y_B) / (4 - 0)

print(f"Předpis lineární funkce: y = {int(k)}x + ({int(q)})")

#úloha 12

b2 = sp.Symbol('b2')
# Velikost vektoru (x2 - x1)^2 + (y2 - y1)^2 = velikost^2
# (3 - (-1))^2 + (b2 - 4)^2 = 5^2
eq = sp.Eq(4**2 + (b2 - 4)**2, 25)
reseni = sp.solve(eq, b2)

print("Možné souřadnice bodu B:")
for r in reseni:
    print(f"B[3; {r}]")

#úloha 16
import math

# Kombinace 2 bodů ze 7 celkových
vsechny_dvojice = math.comb(7, 2)
# Kombinace 2 bodů ze 3 na stejné úsečce
kolinearni_body = math.comb(3, 2)

pocet_primek = vsechny_dvojice - kolinearni_body + 1

print(f"Celkový počet různých přímek: {pocet_primek}")

#úloha 22

a1 = 240   # převod 24 cm na 240 mm
an = 2000  # převod 2 m na 2000 mm
d = 4      # mm

# Z rovnice an = a1 + (n-1)*d vyjádříme n:
n = (an - a1) / d + 1

print(f"Celkový počet vláken: {int(n)}")

#úloha 20

r_nadoby = 12 / 2  # poloměr je polovina průměru
r_kulicky = 3

# Vzorec pro objem koule
V_kulicky = (4/3) * math.pi * r_kulicky**3
# Obsah podstavy (kruh)
podstava = math.pi * r_nadoby**2

# Zvýšení hladiny (dh)
dh = V_kulicky / podstava

print(f"Hladina stoupne o: {dh:.2f} cm")