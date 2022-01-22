esp1 = input()
esp2 = input()
esp3 = input()

if esp1 == "vertebrado":
    if esp2 == "ave":
        if esp3 == "carnivoro":
            print("aguia")
        elif esp3 == "onivoro":
            print("pomba")

    elif esp2 == "mamifero":
        if esp3 == "onivoro":
            print("homem")
        elif esp3 == "herbivoro":
            print("vaca")


elif esp1 == "invertebrado":
    if esp2 == "inseto":
        if esp3 == "hematofago":
            print("pulga")
        elif esp3 == "herbivoro":
            print("lagarta")

    elif esp2 == "anelideo":
        if esp3 == "hematofago":
            print("sanguessuga")
        elif esp3 == "onivoro":
            print("minhoca")
