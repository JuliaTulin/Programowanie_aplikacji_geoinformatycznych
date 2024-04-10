def run():

    dane  = (2024, 'Python', 3.8)
    rok, jezyk, wersja =  dane
    

    
    # FUNKCJE ANONIMOWE - LAMBDA
print()
print("### FUNKCJE ANONIMOWE - LAMBDA  ###")
#22

biblioteka = [
    {'tytul': 'Harry Potter i Kamień Filozoficzny', 'autor': 'J.K. Rowling', 'rok_wydania': 1997},
    {'tytul': 'Władca Pierścieni: Drużyna Pierścienia', 'autor': 'J.R.R. Tolkien', 'rok_wydania': 1954},
    {'tytul': 'Game of Thrones', 'autor': 'George R.R. Martin', 'rok_wydania': 1996},
    {'tytul': 'Zdobyć Everest', 'autor': 'Bear Grylls', 'rok_wydania': 2015},
    {'tytul': 'Java Podstawy', 'autor': 'Herbert Schildt', 'rok_wydania': 2002}
]

# a. sort wedlug roku wydania
posortowane_ksiazki = sorted(biblioteka, key=lambda x: x['rok_wydania'])
print("Książki posortowane według roku wydania")
for ksiazka in posortowane_ksiazki:
    print(ksiazka)

# b. Filtracja ksiazek wydanych po 2000 roku 
ksiazki_po_2000 = filter(lambda x: x['rok_wydania'] > 2000, biblioteka)
print("\nKsiążki wydane po 2000 roku:")
for ksiazka in ksiazki_po_2000:
    print(ksiazka)

# c. Transformacja listy do listy tytułów
tytuly = map(lambda x: x['tytul'], biblioteka)
print("\nTytuły książek:")
for tytul in tytuly:
    print(tytul)

if __name__ == "__main__":
    run()
