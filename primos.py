'''Programa para obtener la cantidad de números primos menores o iguales que el número ingresado'''
lista=[]
final=int(input("Hasta qué número quieres la lista:"))
contador=0
for i in range(2,final+1):
    primos=True
    divisor=2
    while divisor<=i**0.5 and primos:
        if i%divisor==0:
            primos=False
        else:
            divisor+=1
    if primos==True:
        lista.append(i)
        contador+=1
print(lista)
print("La cantidad de números primos es",contador)
