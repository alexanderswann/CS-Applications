import math
l= 36
t = 3.2
vix = l/t
viy = (vix* math.tan(0.820305))
v = math.sqrt((vix*vix)+(viy*viy))
maxy = ((viy*viy)/19.62)+.3048

print("the rocket went "+str(maxy)+" meters high\nthe initial x velocity is "+str(vix)+ " m/s \nthe initial y velocity is "+ str(viy)+" m/s" + "\n the total velovity is "+str(v)+ "m/s")
