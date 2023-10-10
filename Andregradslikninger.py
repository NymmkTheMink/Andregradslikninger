from pylab import *

a = float(input("Skriv inn koeffisienten foran x^2-leddet: "))
b = float(input("Skriv inn koeffisienten foran x-leddet: "))
c = float(input("Skriv inn konstandleddet: "))

x = linspace(-10, 10, 1001)

y = a * x ** 2 + b * x + c

s = -b/(2*a)

if b**2 - 4*a*c > 0:
    x1 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x3 = (x1 + x2) / 2
    y1 = a * x3 ** 2 + b * x3 + c
    print("Nullpunktene er ved x =", x1, "og x =", x2)
    print("Ekstremalpunktet til funksjonen er ved x =", x3, "og y =", y1)
    plt.plot([x1], [0], marker='o', markersize=7, color="k")
    plt.plot([x2], [0], marker='o', markersize=7, color="k")
    plt.plot([x3], [y1], marker='o', markersize=7, color="k")
elif b**2 - 4*a*c == 0:
    x1 = -b / (2*a)
    plt.plot([x1], [0], marker='o', markersize=7, color="k")
    print("Funksjonen har et nullpunkt som er ved x =", x1,)
    print("Ektremalpunktet til funksjonen er ved x =", x1, "og y = 0")
else:
    y1 = a * s ** 2 + b * s + c
    print("Funksjonen har ingen nullpunkter")
    print("Ektremalpunktet til funksjonen er ved x =", s, "og y =", y1)
    plt.plot([s], [y1], marker='o', markersize=7, color="k")

plot(x, y, "c") 
title("Andregradsfunkjon")
grid(color = "r")
xlabel("x-aksen")
ylabel("y-aksen")
xlim(-5, 5)
ylim(-5,10)
axhline(y=0, color = "m")
axvline(x=0, color = "b")
axvline(x=s, color = "y", linestyle = "--")

show()