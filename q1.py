import math
def distancia(x1,y1,x2,y2):
    ecuacion=math.sqrt((y2-y1)**2+(x2-x1)**2)
    return ecuacion

print(distancia(3,1,2,3))
