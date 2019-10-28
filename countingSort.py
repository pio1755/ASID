wpisanie= input("podaj listę do posortowania")
lista = []
for x in range(len(wpisanie)):
    lista.append(int(wpisanie[x]))
print(lista)
index = []
ostateczna = []
for x in range(len(lista)):
    ostateczna.append(0)
for x in range(0, max(lista)+2,1 ):
    index.append(0)
print(index)

for x in range(len(lista)):
    for y in range(len(index)):
        if lista[x] == y:
            index[y]+=1
print(index)
for x in range(0,len(index)-1):
    if x < len(index):
        index[x+1]=index[x]+index[x+1]

print(index)

for x in range(0,len(lista)):
    for y in range(0,):
        if lista[x] == x and x < len(index):
            ostateczna[x]=x

print(ostateczna)


