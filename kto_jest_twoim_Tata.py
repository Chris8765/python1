#Napisz program "Kto jest twoim tatą?", który umożliwia użytkownikowi wprowadzenie imienia i nazwiska osoby płci męskiej
#i przedstawia imię i nazwisko jej ojca. (Możesz dla zabawy wykorzystać nazwiska celebrytów, osób fikcyjnych lub nawet postaci historycznych).
#Umożliw użytkownikowi dodawanie, wymianę i usuwanie par syn - ojciec.

imie_i_nazwisko_syna = None
imie_i_nazwisko_ojca = None

choice = None

pary_syn_ojciec = None

while choice != "0":
    print(
    """
    0 - zakończ
    1 - wprowadzenie pary syn-ojciec
    2 - wymiana pary syn-ojciec
    3 - usuwanie pary syn-ojciec
    4 - ustalenie ojca na podstawie podania imienia i nazwiska syna
    5 - ustalenie dziadka na podstawie podania imienia i nazwiska wnuczka
    """
    )

    choice = input("Wybieram: ")
    print()

    if choice == "0":
        print ("Zakończnie programu. Żegnaj ....")




try:
    imie_i_nazwisko_syna = input("Podaj imie i nazwisko syna (w formacie: imie_nazwisko):\n")
    imie_i_nazwisko_ojca = input("Podaj imie i nazwisko ojca (w formacie: imie_nazwisko):\n")




except:
        imie_i_nazwisko_syna = 1234214
        imie_i_nazwisko_ojca = 434564

