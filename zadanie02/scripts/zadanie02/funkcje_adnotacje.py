def run():

    dane  = (2024, 'Python', 3.8)
    rok, jezyk, wersja =  dane
    

# FUNKCJE FABRYKUJĄCE , ADNOTACJE
# 19
print()
print("### PRZYPISANIA  ###")

def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2)
print(potega_2(4))

#20
#a nonlocal
from typing import Callable

# a
def licznik() -> Callable[[], int]:
    count: int = 0
    def inkrementacja() -> int:
        nonlocal count
        count += 1
        return count
    return inkrementacja

inkrementacja = licznik()
print("Nonlocal")
print(inkrementacja())
print(inkrementacja())

# b
global_count: int = 0

def licznik() -> int:
    global global_count
    global_count += 1
    return global_count

print("Global")
print(licznik())
print(licznik())

#c
class Licznik:
    def __init__(self) -> None:
        self.count: int = 0
        
    def __call__(self) -> int:
        self.count += 1
        return self.count

licznik_instancji = Licznik()
print("Klasa z atrybutem instancji")
print(licznik_instancji())
print(licznik_instancji())

# d
def licznik() -> int:
    if not hasattr(licznik, 'count'):
        licznik.count = 0
    licznik.count += 1
    return licznik.count

print("Atrybut funkcji")
print(licznik())
print(licznik())

if __name__ == "__main__":
    run()













    