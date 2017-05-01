#dado 2 listas a,b. asignar en c, la suma de a y b
a=[12,14,12,18,19,20]
b=[14,17,19,19,22,1]
c=[]
d=[]
e=[]
f=[]
g=[]
i=0
while i<len(a):
    c.append(a[i]+b[i])
    d.append(a[i]-b[i])
    e.append(a[i]*b[i])
    f.append((a[i])/(b[i]))
    g.append(a[i]%b[i])
    i+=1
print "A= ",a,"\nB= ",b,"\nC= ",c,"\nD= ",d,"\nE= ",e,"\nF= ",f,"\nG= ",g






