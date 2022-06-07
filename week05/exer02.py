import math 
def planetVelocity(masss, radius):
    G = 6.67 * 10 ** -11
    return math.sqrt((G*masss)/(radius))