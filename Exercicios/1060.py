positivo = negativo = 0
for c in range(0, 6):
    v = float(input())
    if v > 0:
        positivo += 1

print("{} valores positivos".format(positivo))
