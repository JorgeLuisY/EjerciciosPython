#hallar el numero mayor y menor de un arreglo
a=[34,12,11,56,7,4,3,67,4,2]
mayor=a[0]
menor=a[0]
i=1
while i<len(a):
    if a[i]>mayor:
        mayor=a[i]
    if a[i]<menor:
        menor=a[i]
    i+=1
print a, "\n mayor= ",mayor, "\n menor= ",menor
