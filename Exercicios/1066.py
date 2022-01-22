par = impar = positivo = negativo = 0
for c in range(0, 5):
    v = int(input())
    if v % 2 == 0:
        par += 1
    else:
        impar += 1
    if v > 0:
        positivo += 1
    elif v < 0:
        negativo += 1


print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivo))
print("{} valor(es) negativo(s)".format(negativo))
