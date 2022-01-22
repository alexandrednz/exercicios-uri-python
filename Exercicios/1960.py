n = int(input())
Ds = n // 500
n = n % 500
Cs = n // 100
n = n % 100
Ls = n // 50
n = n % 50
Xs = n // 10
n = n % 10
Vs = n // 5
n = n % 5
Is = n
lista = ['D', 'C', 'L', 'X', 'V', 'I']
cont = -1

for c in [Ds, Cs, Ls, Xs, Vs, Is]:
    cont += 1
    if c != 0:
        print(lista[cont] * c, end="")