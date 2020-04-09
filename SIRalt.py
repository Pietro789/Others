import time
import random
import math
import matplotlib.pyplot as plt
import numpy as np
start=time.time()

so=int(input("Digite o número inicial de pessoas sãs: "))
io=int(input("Digite o número inicial de infectados: "))
ro=int(input("Digite o número inicial de recuperados: "))
mo=int(input("Digite o número inicial de mortos: "))
c1=float(input("Digite a taxa de mortalidade dos jovens: "))
c2=float(input("Digite a taxa de mortalidade dos adultos: "))
c3=float(input("Digite a taxa de mortalidade dos idosos: "))
a=float(input("Digite a taxa de contaminação: "))
b=float(input("Digite a taxa de recuperação: "))

N=so+io+ro

t=int(input("Digite o tempo total: "))
s=so
i=io
r=ro
m=mo
t1=t/10000
t1=int(t1)
listat=np.zeros(t1,dtype=int)
for i in range (t1):
    listat[i]=i

lista=np.zeros(N,dtype=int)
listai=np.zeros(t1,dtype=int)
listas=np.zeros(t1,dtype=int)
listar=np.zeros(t1,dtype=int)
listam=np.zeros(t1,dtype=int)
listati=np.zeros(N,dtype=int)

for i in range (io):
    lista[N-i-1]=1
io=float(io)
i=io

for j in range (t):
    k=np.random.randint(0,N)
    if lista[k]==1:
        p=np.random.uniform(0,1)
        if p<b:
            lista[k]=2
            r+=1
            i-=1
        else:
            p=np.random.uniform(0,1)
            if k/N>0.85:
                c=c3
            if 0.6<k/N<0.85:
                c=c2
            if k/N<0.6:
                c=c1
            if p<c:
                lista[k]=3
                m+=1
                i-=1
    if lista[k]==0:
        p=np.random.uniform(0,1)
        if p<(a*i/N):
            lista[k]=1
            i+=1
            s-=1
    if j%10000==0 and j!=t:
        j1=j/10000
        j1=int(j1)
        listar[j1]=r
        listai[j1]=i
        listas[j1]=s
        listam[j1]=m

print("O número final de infectados é: ")
print(i)
print()
print("O número final de sãos é: ")
print(s)
print()
print("O número final de recuperados é: ")
print(r)
print()
print("O número final de mortos é: ")
print(m)
end=time.time()
print()
print("O tempo total da simulação é: ")
print(end-start)
plt.plot(listat, listai,'ro',color="Red")
plt.xlabel('Tempo')
plt.ylabel('Pessoas infectadas')
plt.title('Evolução temporal de uma doença')

plt.plot(listat, listas,'ro',color="Blue")
plt.xlabel('Tempo')
plt.ylabel('Pessoas sadias')
plt.title('Evolução temporal de uma doença')

plt.plot(listat, listam,'ro',color="Black")
plt.xlabel('Tempo')
plt.ylabel('Pessoas mortas')
plt.title('Evolução temporal de uma doença')

plt.plot(listat, listar,'ro',color="Green")
plt.xlabel('Tempo')
plt.ylabel('Pessoas recuperadas')
plt.title('Evolução temporal de uma doença')
plt.show()
