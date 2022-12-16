'''Ejemplo aplicativo para obtener el número de combinaciones sin repetición
'''
numeros=[1,2,3,4,5,6,7,8,9,10]

contador=0
listas=[]
for i in numeros:
    for j in numeros:
        for k in numeros:
            for l in numeros:
                for m in numeros:
                    if i!=j and i!=k and i!=l and i!=m and j!=k and j!=l\
                         and j!=m and k!=l and k!=m and l!=m:
                        comb=[i,j,k,l,m]
                        comb.sort()
                        if comb not in listas:  #Permite descartar combinaciones duplicadas
                            listas.append(comb)                   
                            contador+=1
                            print("{:3} : {}".format(contador,comb))
