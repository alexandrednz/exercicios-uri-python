def main():

    continuar = True

    while continuar:
        valido = False
        while not valido:
            nota1 = float(input())
            if 0 <= nota1 <= 10:
                valido = True
            else:
                print("nota invalida")

        valido = False
        while not valido:
            nota2 = float(input())
            if 0 <= nota2 <= 10:
                valido = True
            else:
                print("nota invalida")

        media = (nota1 + nota2)/2
        print("media = {:.2f}".format(media))

        x = 0
        while x != 1 and x != 2:
            print("novo calculo (1-sim 2-nao)")
            x = int(input())
        if x == 2:
            continuar = False

main()
