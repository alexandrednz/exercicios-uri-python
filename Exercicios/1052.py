mes = int(input())
lista = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
cont = 0

for c in lista:
    cont += 1
    if cont == mes:
        print(c)