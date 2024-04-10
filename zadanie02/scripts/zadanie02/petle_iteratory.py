def run():


    dane  = (2024, 'Python', 3.8)
    rok, jezyk, wersja =  dane
    

    
    # TECHNIKI TWORZENIA PĘTLI - UZUPEŁNIENIE
print()
print("### PĘTLE I ITERATORY  ###")
#14
imiona = ['Anna', 'Jan', 'Ewa'];
oceny = [5, 4, 3];
pary = zip(imiona, oceny);

print(tuple(pary));

# 15
liczby = [1, 2, 3, 4, 5];

def kwadrat(x):
    return x*x;

sq = map(kwadrat, liczby);
print(list(sq));


# ITERATORY, DOKUMENTOWANIE KODU, FUNKCJE, ARGUMENTY
# 16
arg = [1, 'Ala', 34, 5];
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
        return  arg[0]
    elif isinstance(arg, int):
        arg = 65482652
        return arg

arg = zmien_wartosc(arg);
print(arg);


# 17
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    suma = cena * ilosc
    podsumowanie = f"Produkt: {nazwa_produktu}, Cena: {suma} zł, Ilość: {ilosc}"
    return podsumowanie, suma


zamowienia = []

# Produkt 1
podsumowanie_zamowienia_1, wartosc_zamowienia_1 = zamowienie_produktu("Kubek termiczny", cena=45.99)
zamowienia.append(podsumowanie_zamowienia_1)
print("Podsumowanie zamowienia 1:", podsumowanie_zamowienia_1)
print("Wartość zamowienia 1:", wartosc_zamowienia_1)

# Produkt 2
podsumowanie_zamowienia_2, wartosc_zamowienia_2 = zamowienie_produktu("Długopis", cena=4.99, ilosc=2)
zamowienia.append(podsumowanie_zamowienia_2)
print("Podsumowanie zamowienia 2:", podsumowanie_zamowienia_2)
print("Wartość zamowienia 2:", wartosc_zamowienia_2)

# Produkt 3
podsumowanie_zamowienia_3, wartosc_zamowienia_3 = zamowienie_produktu("Słuchawki", cena=99.99)
zamowienia.append(podsumowanie_zamowienia_3)
print("Podsumowanie zamowieniau 3:", podsumowanie_zamowienia_3)
print("Wartość zamowienia 3:", wartosc_zamowienia_3)

print("Lista zamówień:", zamowienia)



# 18
def stworz_raport(*args, **kwargs):
    for id_produktu in args:
        nazwa_klucza_nazwa = f"{id_produktu}_nazwa"
        nazwa_klucza_cena = f"{id_produktu}_cena"
        if nazwa_klucza_nazwa in kwargs and nazwa_klucza_cena in kwargs:
            print(f"ID produktu: {id_produktu}, Nazwa: {kwargs[nazwa_klucza_nazwa]}, Cena: {kwargs[nazwa_klucza_cena]}")
        else:
            print(f"Brak informacji dla produktu o ID: {id_produktu}")

#stworz_raport(101, 102, 101_nazwa="Kubek termiczny", 101_cena="45.99 zł", 102_nazwa="Długopis", 102_cena="4.99 zł")



if __name__ == "__main__":
    run()
