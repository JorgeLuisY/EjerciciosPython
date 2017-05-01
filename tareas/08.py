a=[22,15,14,17,23,11,20]
b=[11,18,14,13,11]
c=[]
if len(a)>len(b):
    tam=len(b)
else:
    tam =len(a)
i=0
while i<tam:
    c.append(a[i]+b[i])
    i+=1
print c
