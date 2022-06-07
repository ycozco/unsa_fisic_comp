#Del problema anterior realice un código para poder 
#determinar la densidad de cualquier planeta del sistema planetario solar.
# Volumen = (4/3)*pi*r^3
# Densidad = (masa/volumen)
# Densidad = (3*massa)/(4*pi*r^3)

def get_density(planet_mass, planet_radius):
    volume = (4/3)*3.14*(planet_radius**3)
    density = (planet_mass/volume)
    return str(density) +" kg/m^3  \t OR " + str(density/1000) + " g/cm^3"
#test for mercury
print("mercury",get_density(3.3022*10**23, 2439.7*10**3))
#test for venus
print("venus",get_density(4.8685*10**24, 6051.8*10**3))
#test for earth
print("earth",get_density(5.9736*10**24, 6371*10**3))
#test for mars
print("mars",get_density(6.4185*10**23, 3389.5*10**3))
#test for jupiter
print("jupiter",get_density(1.8986*10**27, 69911*10**3))
#test for saturn
print("saturn",get_density(5.6834*10**26, 58232*10**3))
#test for uranus
print("uranus",get_density(8.6810*10**25, 25362*10**3))
#test for neptune
print("neptune",get_density(1.0243*10**26, 24622*10**3))
