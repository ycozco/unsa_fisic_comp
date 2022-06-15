#Implementar un código computacional para determinar la solución de la 
#tercera ley de Kepler para cualquier planeta que describa una órbita elíptica.
#
#Tercera Ley: Para cualquier planeta, el cuadrado
#de su período orbital (tiempo que tarda en dar
#una vueta alrededor del Sol) es directamente
#proporcioal al cubo del radio medio con el Sol
# T = periodo actual del planeta 
# K = T^2/R^3 siempre es constante 
# K = 1 en nuestro sistema solar
def get_period_third_kepler(orbital_rad_ua,period_rad_years):
    # ua = 149597870700 Valor de una UA en metros
    result = 0
    result = (period_rad_years**2)/(orbital_rad_ua**3)
    # gen_result= round(result,2) redondea el resultado a 2 decimales
    return result

#test jupiter
print("jupiter\t",get_period_third_kepler(5.2,11.86)," \tor ", round(get_period_third_kepler(5.2,11.86),5) )
#test saturn
print("saturn\t",get_period_third_kepler(9.58,29.46)," \tor ", round(get_period_third_kepler(9.58,29.46),5) )
#test uranus
print("uranus\t",get_period_third_kepler(19.2,84.01)," \tor ", round(get_period_third_kepler(19.2,84.01),5) )
#test neptuneDDD
print("neptune\t",get_period_third_kepler(30.1,164.8)," \tor ", round(get_period_third_kepler(30.1,164.8),5) )
#test pluto
print("pluto\t",get_period_third_kepler(39.5,248.3)," \tor ", round(get_period_third_kepler(39.5,248.3),5) )
#test mercury
print("mercury\t",get_period_third_kepler(0.38,0.24)," \tor ", round(get_period_third_kepler(0.38,0.24),5) )
#test venus
print("venus\t",get_period_third_kepler(0.72,0.62)," \tor ", round(get_period_third_kepler(0.72,0.62),5) )
#test earth
print("earth\t",get_period_third_kepler(1,1)," \tor ", round(get_period_third_kepler(1,1),5) )
#test mars
print("mars\t",get_period_third_kepler(1.52,1.88)," \tor ", round(get_period_third_kepler(1.52,1.88),5) )





