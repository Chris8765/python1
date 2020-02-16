#Napisz program "Kto jest twoim tatą?", który umożliwia użytkownikowi wprowadzenie imienia i nazwiska osoby płci męskiej
#i przedstawia imię i nazwisko jej ojca. (Możesz dla zabawy wykorzystać nazwiska celebrytów, osób fikcyjnych lub nawet postaci historycznych).
#Umożliw użytkownikowi dodawanie, wymianę i usuwanie par syn - ojciec.

name_and_surname_son = None
name_and_surname_dad = None

son = None
dad = None
grandfather = None
grandpa = None
grandson = None

content = None

choice = None

pair_son_dad ={}

while choice != "0":
    print(
    """
    Main Menu

    0 - End
    1 - Input pair son-dad
    2 - Change the name of dad in pair son-dad
    3 - Remove pair son-dad
    4 - Determination of dad based on the name of the son
    5 - Determination of grandfather based on the name of the grandson
    6 - Determination of son based on the name of the father
    7 - Determination of grandson based on the name of the grandfather
    8 - Show me entire Database
    """
    )

    choice = input("I choose: ")
    print()

    if choice == "0":
        content = pair_son_dad.items()
        print(content)

        print ("The End of Program . Goodbye ....")

    elif choice =="1":
        name_and_surname_son = input("Give me the name of son: ")
        if name_and_surname_son not in pair_son_dad:
                name_and_surname_dad =  input("Give me the name of dad: ")
                pair_son_dad[name_and_surname_son] = name_and_surname_dad
                print("\nName of pair son and dad is added.")
        else:
                print("\nThis pair son and dad already exist! You can change the name of dad.")

    elif choice =="2":
        name_and_surname_son = input(" Give me the name of son, whose name of dad should I change: ")
        if name_and_surname_son in pair_son_dad:
            name_and_surname_dad = input("Give me the name of dad:")
            print("\nFather's name of: " + name_and_surname_son +"is changed.")
        else:
            print("\nThe name and surname doesn't exist. Please add it.")

    elif choice =="3":
        name_and_surname_son = input("Which name of son and automatic name of dad should I remove: ")
        if name_and_surname_son in pair_son_dad:
            del pair_son_dad[name_and_surname_son]
            print("\nOK, I removed that:" + name_and_surname_son +"name and surname his dad")
        else:
            print("\nI can't do it!" + name_and_surname_son + "isn't in database.")

    elif choice =="4":
        name_and_surname_son = input("Give me the name of son, and I give you the name of dad: ")
        if name_and_surname_son in pair_son_dad:
            dad = pair_son_dad[name_and_surname_son]
            print("\n The Dad of " + name_and_surname_son +" is: " + dad)
        else:
            print("\nUnfortunately, I don't have pair of names son and dad in database.")

    elif choice =="5":
        grandson = input("Give me the name of gradson, and I give you the name of grandfather: ")
        if grandson in pair_son_dad:

            dad = pair_son_dad[grandson]
            name_and_surname_son = dad

            if name_and_surname_son in pair_son_dad:
                grandfather = pair_son_dad[name_and_surname_son]

                print("\nThe Grandfather of " + grandson + " is: " + grandfather)
        else:
            print("\nUnfortunately, I don't have the name of son, dad and grandfather in database.")

    elif choice =="6":
        name_and_surname_dad = input("Give me the name of dad, and I give you the name of son: ")

        for name_and_surname_son in pair_son_dad:

                if pair_son_dad[name_and_surname_son] == name_and_surname_dad:

                    son = name_and_surname_son

                    print("\n The Son of " + name_and_surname_dad +" is: " + son)

        print("\n If there isn't any results, It means: \"I don't have pair of names son and dad in database.\"")

    elif choice == "7":
        grandfather = input("Give me the name of gradfather, and I give you the name of grandson: ")

        for name_and_surname_son in pair_son_dad:

                if pair_son_dad[name_and_surname_son] == grandfather:

                    dad = name_and_surname_son





        if grandfather in pair_son_dad[name_and_surname_son]:

            grandpa = grandfather
            dad = pair_son_dad[name_and_surname_son]


            if dad in pair_son_dad[name_and_surname_son]:
                grandson = name_and_surname_son

                print("\nThe Grandson of " + grandpa + " is: " + grandson)
        else:
            print("\nUnfortunately, I don't have the name of son, dad and grandfather in database.")

    elif choice == "8":
        content = pair_son_dad.items()
        print(content)
    else:
        print("\nUnfortunately, " + choice + " is not right choice.")






