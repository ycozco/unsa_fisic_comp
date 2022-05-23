
def main():
    print("Hello World")
def aceleration(mass1,mass2,force):
    result ="ingrese valores positivos"
    if(mass1>0 and mass2>0 and force>0):
        result= force/(mass1+mass2)
    return result

def atWood_aceleration(mass1, mass2, gravity):
    aceleration = 0
    if(mass1>0 and mass2>0 and gravity>0):
        if (mass1>mass2):
            aceleration = (mass1-mass2)*gravity/(mass1+mass2)
        if (mass2>mass1):
            aceleration = (mass2-mass1)*gravity/(mass1+mass2)
    else:
        aceleration = "ingrese valores positivos"
    return aceleration
def atWood_tension(mass1, mass2, gravity):
    aceleration = atWood_aceleration(mass1, mass2, gravity)
    tension = 0
    if(mass1>0 and mass2>0 and gravity>0):
        if (mass1>mass2):
            tension = (mass1)*(gravity+aceleration)
        if (mass2>mass1):
            tension = (mass2)*(gravity+aceleration)
    else:
        tension = "ingrese valores positivos"
    return tension
def fr_hockey(v0,vi,gravity,distance):
    result = 0
    if(gravity>0 and distance>0 and v0 ==0):
        result = (vi**2)/(2*gravity*distance)
    else:
        result = "ingrese valores positivos"
    return result

def get_force(fi,fj,mass):
    icomp = ''
    jcomp = ''
    result = 0
    if(mass>0):
        icomp += str(fi*mass)
        icomp += str(fj*mass)
    else:
        result = "ingrese valor positivo para masa"
    return result

def get_force2(vi,v0,distance,mass,time):
    result = 0
    if(mass>0 and distance>0 and time>0):
        result = (vi-v0)*mass/time
    else:
        result = "ingrese valores positivos"
    return result


