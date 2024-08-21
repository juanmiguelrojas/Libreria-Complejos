#Libreria de numeros complejos 
import math
def sumaC(m,d):
    preal = m[0] + d[0]
    pimg = m[1] + d[1]
    return (preal,pimg)

def restaC(m,d):
    preal = m[0] - d[0]
    pimg = m[1] - d[1]
    return (preal,pimg)

def multiplicacionC(m,d):
    preal = ((m[0]*d[0])-(m[1]*d[1]))
    pimg = ((m[0]*d[1])+(m[1]*d[0]))
    return (preal,pimg)

def divisionC(m,d):
    preal = ((m[0]*d[0]) + (m[1]*d[1])) / ((d[0])**2 + (d[1])**2)
    pimg = ((d[0]*m[1]) - (m[0]*d[1])) / ((d[0])**2 + (d[1])**2)
    return (preal,pimg)

def moduloC(m):
    mod = math.sqrt((m[0]**2) + (m[1]**2))
    #para que sea considerado modulo debe cumplir esta condicion
    if abs(mod) >= 0:
        pass
    return mod

def conjugadoC(m):
    return (m[0],-m[1])

def PolarToCart(m,d):
    a = m * math.cos(d)
    b = m * math.sin(d)
    return a,b

def CartToPolar(m):
    r = moduloC(m)
    theta = math.atan(m[1] / m[0])
    return (r,theta)

def faseDeC(m):
    theta = math.atan(m[1]/m[0])
    return theta

def main():
    a = (-5),(3.2)
    print(CartToPolar(a))
main()

#Pruebas
#copiar y pegar los datos en el la funmcion main
"""
SUMA
    a = (3),(-5)
    b = (-1),(4)
    print(sumaC(a,b))

    a = (1),(4)
    b = (1),(-3)
    print(sumaC(a,b))

RESTA
    a = (2),(-4)
    b = (5),(3)
    print(restaC(a,b))

    a = (6),(2)
    b = (1),(-3)
    print(restaC(a,b))

MULTIPLICACION
    a = (3),(-1)
    b = (1),(4)
    print(multiplicacionC(a,b))

    a = (-2),(1)
    b = (3),(7)
    print(multiplicacionC(a,b))

DIVISION
    a = (-2),(1)
    b = (1),(2)
    print(divisionC(a,b))

    a = (5),(10)
    b = (1),(2)
    print(divisionC(a,b))

MODULO
    a = (1),(1)
    print(moduloC(a))

    a = (3),(4)
    print(moduloC(a))

CONJUGADO
    a = (-5),(4)
    print(conjugadoC(a))

    a = (6),(-2)
    print(conjugadoC(a))

POLAR A CARTESIANAS
    a = 3.7
    b = 1.8
    print(PolarToCart(a,b))

    a = 4.5
    b = 1.5
    print(PolarToCart(a,b))

CARTESIANAS A POLARES
    a = (-5),(3.2)
    print(CartToPolar(a))

    a = (3),(4)
    print(CartToPolar(a))

FASE
    a = (1),(1)
    print(faseDeC(a))

    a = (3),(-2)
    print(faseDeC(a))
"""