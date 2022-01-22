def main():

    while True:
        soma = 0
        m, n = map(int, input().split())

        if m <= 0 or n <= 0:
            break

        maior = max(m, n)
        menor = min(m, n)
        for c in range(menor, maior + 1):
            print(c, end=" ")
            soma += c
        print("Sum={}".format(soma))

main()

