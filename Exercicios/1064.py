soma = positivo = 0

for c in range(0, 6):
    v = float(input())
    if v > 0:
        positivo += 1
        soma += v

media = soma/positivo

print("{} valores positivos".format(positivo))
print("{:.1f}".format(media))