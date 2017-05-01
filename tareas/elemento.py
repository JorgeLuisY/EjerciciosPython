#permitir el ingreso de N numeros ingresados por teclado a un arreglo

n=int(raw_input("coloque el numero de elemento que desea ingresar: "))
a=[]
i=0
while i<n:
    elemento=raw_input("Elemento: ")
    a.append(elemento)
    i+=1
print a
