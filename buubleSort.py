wpisanie = input("Podaj listę do posortowania")
lista = []
for x in range(len(wpisanie)):
    lista.append(int(wpisanie[x]))

print(lista)

pomocnicza = 0

for x in range(len(lista)-1,0,-1):
    for y in range(x):
        if lista[y]>lista[y+1] :
            pomocnicza = lista[y]
            lista[y]=lista[y+1]
            lista[y+1]=pomocnicza

print(lista)
