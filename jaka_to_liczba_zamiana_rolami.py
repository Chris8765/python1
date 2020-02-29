zakres_gorny = 1000
zakres_dolny = 0


print("\"Jaka to liczba - zamiana rolami\" to program polegający na podawaniu przez użytkownika")
print("liczb z zakresu od 1 do ",zakres_gorny,", a komputer szuka tej liczby metodą połowienia przedziału.")

szukana_liczba = int(input("Podaj liczbę całkowitą którą ma szukać komputer: "))

max_prob = int(input("Podaj ile prób ma komputer: "))

liczba_komputera = (zakres_gorny - zakres_dolny)/2

tries = 0

licznik = max_prob - 1

while tries < max_prob and liczba_komputera != szukana_liczba:

    if szukana_liczba > liczba_komputera:

            zakres_dolny = liczba_komputera
            liczba_komputera = int(liczba_komputera + (zakres_gorny - zakres_dolny) / 2)
    else:
            zakres_gorny = liczba_komputera
            liczba_komputera = int(liczba_komputera - (zakres_gorny - zakres_dolny) / 2)

    tries += 1
    licznik = max_prob - tries
if tries == max_prob:
            print ("Komputer nie zdołał znaleźć Twojej liczby w zadanej przez Ciebie liczbie prób :(")


if szukana_liczba == liczba_komputera:
            print ("Komputer odnalazł liczbę w:",tries, "krokach")
            print ("Komputer miał jeszcze do wykorzystania: ",licznik, "prób")
            print ("A liczba przez Ciebie podana to: ",szukana_liczba)


input("Aby zakończyć program naciśnij klawisz enter.")