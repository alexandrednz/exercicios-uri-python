def main():
    for c in range(int(input())):
        frase = input()
        sequencia = ""
        num2 = "abc"
        num3 = "def"
        num4 = "ghi"
        num5 = "jkl"
        num6 = "mno"
        num7 = "pqrs"
        num8 = "tuv"
        num9 = "wxyz"
        i_ant = "\n"
        for i in frase:

            if i == i.upper() and i != ' ':
                sequencia = sequencia + "#"

            for grupo in [num2, num3, num4, num5, num6, num7, num8, num9]:
                if i.lower() in grupo and i_ant.lower() in grupo and i != i.upper():
                    sequencia = sequencia + "*"

            if i.lower() == "a":
                sequencia = sequencia + ('2' * 1)
            if i.lower() == "b":
                sequencia = sequencia + ('2' * 2)
            if i.lower() == "c":
                sequencia = sequencia + ('2' * 3)
            if i.lower() == "d":
                sequencia = sequencia + ('3' * 1)
            if i.lower() == "e":
                sequencia = sequencia + ('3' * 2)
            if i.lower() == "f":
                sequencia = sequencia + ('3' * 3)
            if i.lower() == "g":
                sequencia = sequencia + ('4' * 1)
            if i.lower() == "h":
                sequencia = sequencia + ('4' * 2)
            if i.lower() == "i":
                sequencia = sequencia + ('4' * 3)
            if i.lower() == "j":
                sequencia = sequencia + ('5' * 1)
            if i.lower() == "k":
                sequencia = sequencia + ('5' * 2)
            if i.lower() == "l":
                sequencia = sequencia + ('5' * 3)
            if i.lower() == "m":
                sequencia = sequencia + ('6' * 1)
            if i.lower() == "n":
                sequencia = sequencia + ('6' * 2)
            if i.lower() == "o":
                sequencia = sequencia + ('6' * 3)
            if i.lower() == "p":
                sequencia = sequencia + ('7' * 1)
            if i.lower() == "q":
                sequencia = sequencia + ('7' * 2)
            if i.lower() == "r":
                sequencia = sequencia + ('7' * 3)
            if i.lower() == "s":
                sequencia = sequencia + ('7' * 4)
            if i.lower() == "t":
                sequencia = sequencia + ('8' * 1)
            if i.lower() == "u":
                sequencia = sequencia + ('8' * 2)
            if i.lower() == "v":
                sequencia = sequencia + ('8' * 3)
            if i.lower() == "w":
                sequencia = sequencia + ('9' * 1)
            if i.lower() == "x":
                sequencia = sequencia + ('9' * 2)
            if i.lower() == "y":
                sequencia = sequencia + ('9' * 3)
            if i.lower() == "z":
                sequencia = sequencia + ('9' * 4)
            if i == " ":
                sequencia = sequencia + ('0')

            i_ant = i

        print(sequencia)

main()