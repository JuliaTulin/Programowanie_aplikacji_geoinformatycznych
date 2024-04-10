def run():

    dane  = (2024, 'Python', 3.8)
    rok, jezyk, wersja =  dane
    print()
    print(rok)
    print(jezyk)
    print(wersja)

    # PRZYPISANIA 
print()
print("### PRZYPISANI  ###")

dane  = (2024, 'Python', 3.8);
rok, jezyk, wersja =  dane;
print(rok);
print(jezyk);
print(wersja);

oceny = [4, 3, 5, 2, 5, 4];
pierwsza, *srodek, ostatnia = oceny;
print(pierwsza);
print(srodek);
print(ostatnia);

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista');
imie, nazwisko, _, _ , zawod = info;
print(imie);
print(nazwisko);
print(zawod);

dane = (2024, ['Python', 3.8, ('Stabilna', 'wersja')]);
rok, [jezyk,  wersja, (opis)] = dane;

print(rok);
print(jezyk);
print(wersja);
print(opis);


# PRZYPISANIA Z WIELOMA CELAMI I WSPÓŁDZIELONE REFERENCJE

a = b = [1,2,3];
b[0] = 'zmieniono';

for i in a:
    print(a);

for i in b:
    print(b);

c = a[:];
c[0] = 'nowa wartość';

for i in c:
    print(c);

x = y = 10;
y += 1;
print(x, y);


# PRZYPISANIA ROZSZERZONE I WSPÓŁDZIELONE REFERENCJE

K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print(K, L, M, N);


if __name__ == "__main__":
    run()
