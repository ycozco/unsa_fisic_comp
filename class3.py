import math
def main():
    print('asdasdadad')
    pi = 3.14159265359
    print(mas(0.3,pi/6,1))
    print(masForced(0.3,pi/6,1,2))
#A = amplitud ;  w = v0 ; frecuencia = 0|  
def mas(amplitud, frecuencia,tiempo):
    result = "x("+str(tiempo)+") = "
    if(amplitud>0 and frecuencia>0 and tiempo>0):
        result += str(amplitud*math.cos(frecuencia*tiempo))
    else:
        result = "ingrese valores positivos"
    return result
def masForced(amplitud, frecuencia, tiempo, v0):
    result = "x("+str(tiempo)+") = "
    if(amplitud>0 and frecuencia>0 and tiempo>0):
        result += str(amplitud*math.cos(frecuencia*tiempo+v0))
    else:
        result = "ingrese valores positivos"
    return result

def electricOscilations(initalQ, frecuencia,v0, tiempo):
    result = "Q("+str(tiempo)+") = "
    if(tiempo>0 and frecuencia>0):
        result = str(initalQ*math.sin(frecuencia*tiempo+v0))
    else:
        result = "ingrese valores positivos"
    return result

def electricOscilationsLC(initalQ, frecuencia,v0, tiempo):
    result = "Q("+str(tiempo)+") = "
    if(tiempo>0 and frecuencia>0):
        result = str(initalQ*math.sin(frecuencia*tiempo+v0))
    else:
        result = "ingrese valores positivos"
    return result

main()