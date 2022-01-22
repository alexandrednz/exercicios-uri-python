def main():
    n = int(input())
    lista = input().split()
    pas = 1
    r_ant = int(lista[1]) - int(lista[0])
    try:
        for c in range(1, n - 1):
            termo1 = lista[c]
            termo2 = lista[c + 1]

            r = int(termo2) - int(termo1)

            if r != r_ant:
                pas += 1
                r_ant = int(lista[c + 2]) - int(lista[c + 1])
            else:
                r_ant = r
        print(pas)

    except IndexError:
        print(pas)

main()
