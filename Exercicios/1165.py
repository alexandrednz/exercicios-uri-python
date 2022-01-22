def main():

    n = int(input())

    for c in range(1, n+1):
        v = int(input())

        divisores = 0
        for i in range(1, v+1):
            if v % i == 0:
                divisores += 1

        if divisores > 2:
            print("{} nao eh primo".format(v))
        else:
            print("{} eh primo".format(v))

main()



