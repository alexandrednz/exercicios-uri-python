def main():
    while True:
        try:

            exp = input()
            aux = 0
            for i in exp:
                if i == "(":
                    aux += 1
                if i == ")":
                    aux -= 1

                if aux < 0:
                    break

            if aux == 0:
                print("correct")
            else:
                print("incorrect")

        except EOFError:
            break

main()
