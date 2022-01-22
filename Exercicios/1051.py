salario = float(input())

if salario <= 2000:
    print("Isento")
else:
    if salario <= 3000:
        imposto = (salario - 2000) * 8/100
    elif salario <= 4500:
        imposto = 1000 * (8/100) + (salario - 3000) * (18/100)
    else:
        imposto = 1000 * (8/100) + 1500 * (18/100) + (salario - 4500) * (28/100)

    print("R$ {:.2f}".format(imposto))
