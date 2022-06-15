import math
def solve_potential_eq(n,a,b,V1,V2,x,y):
    pi = 3.141592653589793
    result = 0
    i=1
    if n<1:
        result = "Error: n must be greater than 0"
    while i<=n:
        temp1 = V2*math.sinh((n*pi*x)/b)
        temp2 = V1*math.sinh((n*pi*(a-x))/b)
        temp3 = (math.sinh((n*pi*a)/b))
        temp4 = math.sin((n*pi/b)*y)
        result += (1/n)*((temp1 + temp2)/temp3)*temp4
        i+=2
    result += (4/pi)*result
    return result   #return the result of the function
#test
rs =solve_potential_eq(10,2,5,3,4,11,5)
print(rs)