#Implementar un código computacional para la solución de la segunda ley de Kepler
# Velocidad aerolar  
# VA = da/dt
# da = 1/2*r^2*(diferencial de teta)
# dt = 1/2*r^2*w
# dt = 1/2*r^2*(velocidad angular)
# Segunda ley de kepler  establece que la velocidad aerolar es constante 
# VA = 1/2*r^2*w
# V_t = Componente transversal
# se cumple que r1^2 * w1 = r2^2 * w2    >>> si r1<r2 entonces  w1>w2
# r1*V_t1 = r2*V_t2  
# En el afelio y perihelio el componente transversal es igual a la velcoidad del planeta
# cumpliendose tambien la siguiente relacion rp*vp = ra*va  
# (rp = radio del planeta en el perihelio / vp = velocidad del planeta en el perihelio)
# (ra = radio del planeta en el afelio / va = velocidad del planeta en el afelio)
# El momento angular se conserva al no existir torque.
def aerolar_velocity(planet_radius_to_sun_1, planet_angular_velocity_1, planet_radius_to_sun_2, planet_angular_velocity_2):
    gen_result = ""
    result1 = 0
    result2 = 0
    result1 = 1/2(planet_radius_to_sun_1**2) * planet_angular_velocity_1
    result2 = 1/2(planet_radius_to_sun_2**2) * planet_angular_velocity_2
    if(result1 == result2):
        gen_result= "los dos planetas tienen la misma velocidad aerolar r1:" + str(result1) + "/t r2:" + str(result2)
    return gen_result
