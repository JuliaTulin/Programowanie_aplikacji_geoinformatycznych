def run():


    dane  = (2024, 'Python', 3.8)
    rok, jezyk, wersja =  dane
    

    
    # GENERATORY - FUNKCJE I WYRAŻENIA GENERATORÓW
print()
print("### GENERATORY  ###")
# 23

def dni_tygodnia():
    dzien = 0
    nazwy_dni = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    while True:
        yield nazwy_dni[dzien % 7]
        dzien += 1

print("\nTydzień:")
for dzien in dni_tygodnia():
    print(dzien)
    if dzien == 'niedziela':
        break

print("\nPierwsze trzy dni tygodnia:")
generator = dni_tygodnia()
for _ in range(3):
    print(next(generator))

dni_tygodnia = (nazwa for nazwa in ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela'])

print("\nTydzień:")
for dzien in dni_tygodnia:
    print(dzien)


print("\nPierwsze trzy dni tygodnia:")
dni_tygodnia = (nazwa for nazwa in ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela'])
for _ in range(3):
    print(next(dni_tygodnia))



if __name__ == "__main__":
    run()
