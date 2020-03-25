zakres_gorny = 1000
zakres_dolny = 0

def display_instruction():
    
    print("\"Jaka to liczba - zamiana rolami\" to program polegający na podawaniu przez użytkownika")
    print("liczb z zakresu od 1 do ",zakres_gorny,", a komputer szuka tej liczby metodą połowienia przedziału.")


def give_number(question, zakres_dolny, zakres_gorny):
    """Popros o podanie liczby z odpowiedniego zakresu."""
    
    response = None
    while response not in range (zakres_dolny, zakres_gorny):
        response = int(input(question))
    return response



def questions(zakres_dolny, zakres_gorny):
    szukana_liczba = give_number("Podaj liczbę całkowitą którą ma szukać komputer: ", zakres_dolny, zakres_gorny)

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



def main():
    
    display_instruction()
    questions(zakres_dolny, zakres_gorny)



    
    
    
#rozpoczęcie programu
main()
input("Aby zakończyć program naciśnij klawisz enter.")