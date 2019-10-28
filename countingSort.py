wpisanie= input("podaj listę do posortowania")
lista = []
for x in range(len(wpisanie)):
    lista.append(int(wpisanie[x]))
print(lista)
index = []

for x in range(0, max(lista)+2,1 ):
    index.append(0)
print(index)

for x in range(len(lista)):
    for y in range(len(index)):
        if lista[x] == y:
            index[y]+=1
print(index)

ostateczna =[]

for x in range(len(index)):
    for y in range(index[x]):
        ostateczna.append(x)

print(ostateczna)
