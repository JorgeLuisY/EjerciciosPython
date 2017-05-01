# Desarrollar el siguiente algoritmo T=1/1+1/2+1/3+...+1/n
n= float(raw_input("n: "))
a= 1.0
T= 0
while a<=n:
    T=T + (1/a)
    a+=1
    print T
