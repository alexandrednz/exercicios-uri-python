def main():
    n = int(input())

    plano = [[0 for y in range(101)] for x in range(101)]

    for c in range(n):
        x1, x2, y1, y2 = map(int, input().split())
        for i in range(x1 + 1, x2 + 1):
            for j in range(y1 + 1, y2 + 1):
                plano[i][j] = 1

    marcados = 0
    for k in plano:
        marcados += (sum(k))

    print(marcados)

main()
