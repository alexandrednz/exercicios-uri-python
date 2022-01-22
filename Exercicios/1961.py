def main():
    p, n = map(int, input().split())
    lista = input().split()
    canoanterior = int(lista[0])
    for c in lista:
        if int(c) - canoanterior > p or int(c) - canoanterior < p * -1:
            resultado = "GAME OVER"
            break
        else:
            resultado = "YOU WIN"
            canoanterior = int(c)

    print(resultado)

main()

