#Program który wczytuje komunikat użytkownika, a następnie wypisuje go w odwrotnej kolejności

komunikat = input("Podaj komunikat który ma zostać zapisany w odwrotnej kolejności:")

high = len(komunikat)
low = -1
odwrotny = ""

for pozycja in range(high-1, low, -1):

    odwrotny += (komunikat[pozycja])

print ("A oto komunikat w odwróconej kolejności:", odwrotny)

input ("Aby zakończyć program naciśnij klawisz enter.")