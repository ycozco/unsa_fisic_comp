#A partir de la segunda ley de movimiento de Newton y la ley 
# de gravitación universal realice un código que permita 
# determinar el valor de la gravedad para cualquier planeta 
# del sistema planetario solar
# medir la gravedad a una distancia h (del planeta)
#distancia sol a la medida => r = R+h
#R = distancia del sol al planeta 
#F = m.a
#F = m . g
#F = Fg
# Ms . g = G Ms Mp / r^2
#g = G Mp/ r^2
#g = G Mp/(R+h)^2
#h<= 2r  (r =  radio del planeta en cuestion) 
#Ley dfe gravitacion 
#F = cteGravi*( Ms Mp)/ (distancia que los separa ^2)

def get_gravity_any_planet(planet_mass, planet_radius, planet_altitude):
    G = 6.67408 * 10**-11
    result = 0
    if(planet_altitude<=planet_radius):
        result = G * planet_mass  / ((planet_radius+planet_altitude)**2)
    else: 
        result = "recuerda que la condicion de altitud a medir debe cumplir que la altitud sea menor o igual al diametro del planeta"
    return result
#test for mercury
print("mercury\t",get_gravity_any_planet(3.3022*10**23, 2439.7*10**3, 0))
#test for venus
print("venus\t",get_gravity_any_planet(4.8685*10**24, 6051.8*10**3, 0))
#test for earth
print("earth\t",get_gravity_any_planet(5.9736*10**24, 6371*10**3, 0))
print("test earth with distance = 7000000")
print("earth\t",get_gravity_any_planet(5.9736*10**24, 6371*10**3, 7000000))
#test for mars
print("mars\t",get_gravity_any_planet(6.4185*10**23, 3389.5*10**3, 0))
#test for jupiter
print("jupiter\t",get_gravity_any_planet(1.8986*10**27, 69911*10**3, 0))
#test for saturn
print("saturn\t",get_gravity_any_planet(5.6834*10**26, 58232*10**3, 0))
#test for uranus
print("uranus\t",get_gravity_any_planet(8.6810*10**25, 25362*10**3, 0))
#test for neptune
print("neptune\t",get_gravity_any_planet(1.0243*10**26, 24622*10**3, 0))