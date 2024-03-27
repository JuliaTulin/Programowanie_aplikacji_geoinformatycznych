import json
import string

with open("C:/Users/jtuli/Desktop/STUDIA/6_semestr/Python/zadanie01/teksty.json") as plik:
    dane = json.load(plik)

tekst_polaczony = ""
for tekst in dane["teksty"]:
    tekst_polaczony += tekst[next(iter(tekst))]

tekst_polaczony = tekst_polaczony.lower()

wyrazy = tekst_polaczony.split()

wyrazy = [wyraz.strip(string.punctuation) for wyraz in wyrazy]

wyrazy = [wyraz[:-1] + wyraz[-1].upper() for wyraz in wyrazy]

wyrazy = [wyraz for wyraz in wyrazy if 'a' not in wyraz and 'A' not in wyraz]

unikalne_wyrazy = set(wyrazy)

ilosci_wystapien = {wyraz: wyrazy.count(wyraz) for wyraz in unikalne_wyrazy}

with open("wyniki.json", "w") as file:
    json.dump({"tekst_polaczony": tekst_polaczony,
               "wyrazy_unikatowe": list(unikalne_wyrazy),
               "ilosci_wystapien": ilosci_wystapien}, file, indent=4)
