'''Ejemplo aplicatvio para obtener el número de variaciones sin repetición
'''

import random
from random import *

consonantes=["B","C","D","F","G","H","J","K","L","M"]
vocales=["A","E","I","O","U"]
contador=0
lista=[]
for i in consonantes:
    for j in vocales:
        for k in consonantes:
            for l in vocales:
                for m in consonantes:
                    for n in vocales:
                        if i!=k and i!=m and k!=m and j!=l and j!=n and l!=n:
                            contador+=1
                            lista.append(i+j+k+l+m+n)

print(lista[randrange(0,len(lista)-1)],lista[randrange(0,len(lista)-1)],lista[randrange(0,len(lista)-1)],lista[randrange(0,len(lista)-1)],lista[randrange(0,len(lista)-1)])
print(contador)
