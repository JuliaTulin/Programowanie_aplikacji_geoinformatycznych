# 1
imiona = ["Julia", "Rafał", "Zuzanna", "Jakub", "Szymon"]

for indeks, imie in enumerate(imiona):
    print("Indeks:", indeks, "- Imię:", imie)

# a
liczba = 6

if liczba > 0 and liczba % 2 == 0:
    print("Liczba jest dodatnia i parzysta")

# b
liczba = int(input("Podaj liczbę: "))

if liczba != 0:
    print("Liczba jest różna od zera")

# c
dostepne_owoce = ['jabłko', 'banan', 'pomarańcza']
owoc = input("Podaj nazwę owocu: ")

if owoc in dostepne_owoce:
    print("Owoc jest dostępny")

suma = 0
while suma <= 100:
    liczba = int(input("Podaj liczbę: "))
    suma += liczba

print("Suma liczb przekroczyła 100. Suma = ", suma)
