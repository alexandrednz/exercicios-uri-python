def main():
    n = int(input())
    for c in range(n):
        p1, p2 = input().split()

        if max(len(p1), len(p2)) == len(p1):
            maior = p1
            menor = p2
        else:
            maior = p2
            menor = p1

        palavra = ""

        for i in range(len(maior)):

            if i == len(menor):
                palavra += maior[i:]
                break

            palavra += p1[i]
            palavra += p2[i]

        print(palavra)

main()
