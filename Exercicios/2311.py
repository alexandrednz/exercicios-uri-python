def main():
    n = int(input())
    for c in range(n):
        nome = input()
        gd = float(input())
        n1, n2, n3, n4, n5, n6, n7 = map(float, input().split())
        maior = max(n1, n2, n3, n4, n5, n6, n7)
        menor = min(n1, n2, n3, n4, n5, n6, n7)

        nota = (n1 + n2 + n3 + n4 + n5 + n6 + n7 - maior - menor) * gd
        print("{} {:.2f}".format(nome, nota))

main()