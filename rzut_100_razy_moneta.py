#program który 100 razy rzuca monteą i podaje użytkownikowi liczbę orzełków i reszek

reszka = 0
orzel = 0
licznik = 0


import random

while licznik < 100:
        rzut = random.randint(1,2)
        licznik += 1

        if rzut == 1:
            reszka += 1
        else:
            orzel += 1

print("Liczba reszek wynosi:", reszka)
print("Liczba orzełków wynosi:", orzel)