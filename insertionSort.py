wpisanie = input("Podaj listę do posortowania")
lista = []
for x in range(len(wpisanie)):
    lista.append(int(wpisanie[x]))

print(lista)

for x in range(1, len(lista)):
    klucz = lista[x]
    y=x-1
    while y>=0 and klucz < lista[y]:
        lista[y+1]=lista[y]
        y-=1
    lista[y+1] = klucz

print(lista)

