#TP 2 méthode de Newton

import math


def Newton(f, fder, x0, epsilon, Nitermax):
    xold = x0
    xnew = xold - (f(xold)/fder(xold))
    n = 1
    while abs(xnew-xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = xold - (f(xold)/fder(xold))
        n+=1
    return xnew, n

#équation1

def f1(x):
    return ((x**4) + 3*x - 9)
def f1der(x):
    return (4*(x**3) +3)

print(Newton(f1, f1der, 1, 10**(-10), 50000))

print(Newton(f1, f1der, -2, 10**(-10), 50000))



#équation2

def f2(x):
    return (3*math.cos(x)-x-2)

def fder2(x):
    return (-1)*(3*math.sin(x)+1)

print(Newton(f2, fder2, 0, 10**(-6), 5*10**(4)))

print(Newton(f2, fder2, (-1), 10**(-6), 5*10**(4)))

print(Newton(f2, fder2, (-4), 10**(-6), 5*10**(4)))


#équation3

def f3(x):
    return (x*(math.exp(x)) - 7)

def f3der(x):
    return(math.exp(x) + x*(math.exp(x)))

print(Newton(f3, f3der, 1, 10**(-10), 50000))



#équation4


def f4(x):
    return (math.exp(x)-x-10)

def fder4(x):
    return (math.exp(x)-1)

print(Newton(f4, fder4, (-9), 10**(-6), 5*10**(4)))

print(Newton(f4, fder4, (2), 10**(-6), 5*10**(4)))


#équation5

def f5(x):
    return (2*(math.tan(x))-x-5)

def f5der(x):
    return (2*(1/(math.cos(x))**2) -1)

print(Newton(f5, f5der, 1, 10**(-10), 50000))


#équation6

def f6(x):
    return (math.exp(x)-(x**2)-3)

def fder6(x):
    return (math.exp(x)-2*x)

print(Newton(f6, fder6, 2, 10**(-6), 5*10**(4)))


#équation7

def f7(x):
    return (3*x + 4*(math.log(x)) - 7)

def f7der(x):
    return (3 + (4/x))

print(Newton(f7, f7der, 1, 10**(-10), 50000))


#équation8

def f8(x):
    return ((x**4)-2*(x**2)+4*x-17)

def fder8(x):
    return (4*(x**3)-4*x+4)

print(Newton(f8, fder8, 2, 10**(-6), 5*10**(4)))

print(Newton(f8, fder8, (-2), 10**(-6), 5*10**(4)))


#équation9

def f9(x):
    return (math.exp(x) - (2*math.sin(x)) -7)

def f9der(x):
    return (math.exp(x) - 2*math.cos(x))

print(Newton(f9, f9der, 2, 10**(-10), 50000))

#équation10

def f10(x):
    return(math.log((x**2)+4)*math.exp(x)-10)

def fder10(x):
    return(math.exp(x)*(((2*x)/(x**2)+4)+math.log((x**2)+4)))

print(Newton(f10, fder10, (3/2), 10**(-6), 5*10**(4)))



















