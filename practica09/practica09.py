import numpy as np
import math

# exer01:
def f1(x):
    return (math.e)**(-x)

def exer01_falsa():
    a = 2.5
    b = 4
    ni = 0
    es = 0.000001
    ea = 1
    rold = a
    while (es<ea):
      r = b - ((f1(b)*(b - a))/(f1(b) - f1(a)))
      ni = ni+1
      if (f1(a)*f1(r)<0):
         b=r
      else:
        if (f1(r)*f1(b)<0):
           a=r
      ea = abs((r-rold)/r)*100
      rold=r
    print('El valor de la raiz por el Método de la Falsa Posición es ',r)

def f2(x):
    return (math.e)**x -x 

def exer02_falsa():
    a = 0
    b = 0.5
    ni = 0
    es = 0.000001
    ea = 1
    rold = a
    while (es<ea):
        r = b - ((f2(b)*(b - a))/(f2(b) - f2(a)))
        ni = ni+1
        if (f2(a)*f2(r)<0):
            b=r
        else:
            if (f2(r)*f2(b)<0):
                a=r
        ea = abs((r-rold)/r)*100
        rold=r
    print('El valor de la raiz por el Método de la Falsa Posición es ',r)

def f3(x):
    p1 = 10*math.cos(2*x)
    p2 = (math.e)**(x/2)
    return p1*p2 - 4
def f3_derivada(x):
    p1 = -5*(math.e)**(x/2)
    p2 = 4*math.sin(2*x) - math.cos(2*x)
    return p1*p2
def exer03_newton():
    x1 = 0.5
    ni = 0
    es = 0.000001
    ea = 1
    while (es<ea):
      x2 = x1 - f3(x1)/f3_derivada(x1)
      ni = ni+1
      ea = abs((x2-x1)/x2)*100
      x1=x2
    print('El valor de la raiz por el Método de Newton-Rapshon es ',x2)
    print('en la linea ',ni)

def f4(x):
    return x**2 -2

def exer04_falsa():
    a = 0
    b = 2
    ni = 0
    es = 0.000001
    ea = 1
    rold = a
    while (es<ea):
        r = b - ((f4(b)*(b - a))/(f4(b) - f4(a)))
        ni = ni+1
        if (f4(a)*f4(r)<0):
            b=r
        else:
            if (f4(r)*f4(b)<0):
                a=r
        ea = abs((r-rold)/r)*100
        rold=r
    print('El valor de la raiz por el Método de la Falsa Posición es ',r)
    print('en la linea ',ni)

def f5(x):
    return x**3 - 2

def exer05_falsa():
    a = 0
    b = 2
    ni = 0
    es = 0.000001
    ea = 1
    rold = a
    while (es<ea):
        r = b - ((f5(b)*(b - a))/(f5(b) - f5(a)))
        ni = ni+1
        if (f5(a)*f5(r)<0):
            b=r
        else:
            if (f5(r)*f5(b)<0):
                a=r
        ea = abs((r-rold)/r)*100
        rold=r
    print('El valor de la raiz por el Método de la Falsa Posición es ',r)
    print('en la linea ',ni)

def f7(x):
    return x**3 + 4*x**2 - 10

def exer07_falsa():
    a = 1
    b = 2
    ni = 0
    es = 0.000001
    ea = 1
    rold = a
    while (es<ea):
        r = b - ((f7(b)*(b - a))/(f7(b) - f7(a)))
        ni = ni+1
        if (f7(a)*f7(r)<0):
            b=r
        else:
            if (f7(r)*f7(b)<0):
                a=r
        ea = abs((r-rold)/r)*100
        rold=r
    print('El valor de la raiz por el Método de la Falsa Posición es ',r)
    print('en la linea ',ni)
exer07_falsa()