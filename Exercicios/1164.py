def main():

    n = int(input())
    for c in range(1, n+1):

        x = int(input())

        soma = 0
        for i in range(1, x):
            if x % i == 0:
                soma += i

        if soma == x:
            print("{} eh perfeito".format(x))
        else:
            print("{} nao eh perfeito".format(x))

main()
