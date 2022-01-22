def main():
    n, m = map(int, input().split())
    listatempos = []
    for c in range(n):
        voltas = input().split()
        tempototal = 0

        for i in voltas:
            tempototal += int(i)

        listatempos.append(tempototal)

    listatempos_aux = list(listatempos)

    primeiro = listatempos.index(min(listatempos)) + 1
    del(listatempos[listatempos.index(min(listatempos))])
    segundo = listatempos_aux.index(min(listatempos)) + 1
    del(listatempos[listatempos.index(min(listatempos))])
    terceiro = listatempos_aux.index(min(listatempos)) + 1

    print(primeiro)
    print(segundo)
    print(terceiro)

main()
