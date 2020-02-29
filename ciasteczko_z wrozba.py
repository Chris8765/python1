# Oto program "ciasteczko z wróżbą", program rozlosowuje dla Ciebie jedną z 5 wróżb.
import random

numer = random.randint(1,5)

if numer == 1:
    print("Dzisiaj będzie dobry dzień")
elif numer == 2:
    print("Uważaj, wypadki chodzą po ludziach")
elif numer == 3:
    print("Wygrasz dzisiaj milion złotych")
elif numer == 4:
    print ("Kup sobie rower, może Ci się przydać")
else:
    print ("Pracuj mało, zarabiaj dużo")

input("\nAby zakończyć program, naciśnij klawisz Enter.")