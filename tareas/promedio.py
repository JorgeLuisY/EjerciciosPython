#dado un arreglo, hallar el promedio de todos sus valores
a=[12,14,16,17,19,20]
i=0
suma=0
while i<len(a):
    suma+=a[i]
    i+=1
print(suma)/(len(a))
