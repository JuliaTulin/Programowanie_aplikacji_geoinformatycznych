import math
import random

wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12

tekst = str(potega)
#print(tekst)

wartosc_pi = math.pi
lista = [1, 2, 3, 4, 5]
losowa = random.choice(lista)
#print(losowa)

tekst = f"Wartosc:{tekst}"
print(len(tekst))
print(tekst[1:4])

dir(tekst)
print(tekst.upper())

tekst = tekst.replace(tekst[1],"p")
print(tekst)

lista = list(tekst)
lista = lista[0:8]
print(lista)

lista1 = [1, 2, 3, 4, 5]
lista = lista + lista1
print(lista)

index = lista.pop(7)
print(lista)

lista2= [1, 2, 3, "banan", 100]

lista3 = [x**2 for x in lista2 if x !="banan"]

lista41 = range(2, 17, 2)
lista4 = []
for n in lista41:
  lista4.append(n)

print(lista2)           
print(lista3)
print(lista4)


# słownik

# 15
ja = {}

# 16
ja['imie'] = 'Julia'
ja['nazwisko'] = 'Tulin'
ja['wiek'] = 21
ja['rodzice'] = [{'imie': 'Danuta', 'wiek': 51}, {'imie': 'Jacek', 'wiek': 52}]

# 17
print(ja['rodzice'])

# 18
print(ja['rodzice'][0]['imie'])

# 19
print(ja.keys())

# 20
czy_ma_rodzenstwo = 'rodzenstwo' in ja
print(czy_ma_rodzenstwo)

# KROTKI 
# 21
krotka1 = (1, 2, "3", 4, 2, 5)

# 22
print("Długość krotki:", len(krotka1))
print("Pierwszy wyraz:", krotka1[0])

# 23
liczba_dwojek = krotka1.count(2)
print("Liczba wystąpień wartości 2:", liczba_dwojek)

# 24
#krotka1[0] = 2  # błąd, ponieważ krotki nie są modyfikowalne

# ZBIORY
# 25
X = set("kalarepa")
Y = set("lepy")

# 26
czesc_wspolna = X.intersection(Y)
print("Część wspólna zbiorów X i Y:", czesc_wspolna)
