def main():

    n = int(input())
    coelhos = ratos = sapos = 0
    for c in range(1, n + 1):
        cob, tipo = input().split()
        cob = int(cob)
        if tipo == "C":
            coelhos += cob
        elif tipo == "R":
            ratos += cob
        elif tipo == "S":
            sapos += cob

    total = coelhos + ratos + sapos
    per_coelhos = (coelhos/total) * 100
    per_ratos = (ratos/total) * 100
    per_sapos = (sapos/total) * 100

    print("Total: {} cobaias".format(total))
    print("Total de coelhos: {}".format(coelhos))
    print("Total de ratos: {}".format(ratos))
    print("Total de sapos: {}".format(sapos))
    print("Percentual de coelhos: {:.2f} %".format(per_coelhos))
    print("Percentual de ratos: {:.2f} %".format(per_ratos))
    print("Percentual de sapos: {:.2f} %".format(per_sapos))

main()

