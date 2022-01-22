def main():
    n = int(input())
    lista = input().split()
    mult2 = mult3 = mult4 = mult5 = 0
    for c in lista:
        if int(c) % 2 == 0:
            mult2 += 1
        if int(c) % 3 == 0:
            mult3 += 1
        if int(c) % 4 == 0:
            mult4 += 1
        if int(c) % 5 == 0:
            mult5 += 1

    print("{} Multiplo(s) de 2".format(mult2))
    print("{} Multiplo(s) de 3".format(mult3))
    print("{} Multiplo(s) de 4".format(mult4))
    print("{} Multiplo(s) de 5".format(mult5))

main()