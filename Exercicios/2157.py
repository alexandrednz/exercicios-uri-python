def main():
    n = int(input())
    for c in range(n):
        a, b = map(int, input().split())
        sequencia = espelho = ""
        for i in range((b - a) + 1):
            num = str(a + i)
            sequencia += num
        for h in range((b - a) + 1):
            num = str(b - h)
            inversonum = num[::-1]
            espelho += inversonum
        print("{}{}".format(sequencia, espelho))

main()
