#permitir el ingreso de numeros a un arreglo mientras este sea diferente de cero, luego
#mostrar la sumatoria de pares
#sumatoria numero impares
#sumetoria de positivos
#sumatoria de numero negativos
a=[]
numero=1
while numero!=0:
    numero= int(raw_input("ingrese numero: "))
    a.append(numero)
print a
sumapar=0
sumaimpar=0
sumapositivos=0
sumanegativos=0
for i in a:
    if i%2==0:
        sumapar+=i
    else:
        sumaimpar+=i
    if i>0:
        sumapositivos+=i
    else:
        sumanegativos+=i
print "suma pares = ",sumapar
print "\n suma impares = ",sumaimpar
print "\n suma positivos = ",sumapositivos
print "\n suma negativos = ",sumanegativos

                        
