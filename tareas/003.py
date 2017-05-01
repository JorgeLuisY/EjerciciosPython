# M=2/3+3/4+...+n+1/n+2
n= float(raw_input("n: "))
a=1.0
M=0.0
while a<=n:
    M=M+((a+1)/(a+2))
    a+=1
    print M
