v = float(input())

# notas

cem = v // 100
v = v % 100
cinquenta = v // 50
v = v % 50
vinte = v // 20
v = v % 20
dez = v // 10
v = v % 10
cinco = v // 5
v = v % 5
dois = v // 2
v = v % 2

# moedas

um = v // 1
v = v - 1*um
cent50 = (v*100) // 50
v = (v*100) % 50
cent25 = v // 25
v = v % 25
cent10 = v // 10
v = v % 10
cent5 = v // 5
v = v % 5
cent1 = v

# saída
print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00".format(cem))
print("{:.0f} nota(s) de R$ 50.00".format(cinquenta))
print("{:.0f} nota(s) de R$ 20.00".format(vinte))
print("{:.0f} nota(s) de R$ 10.00".format(dez))
print("{:.0f} nota(s) de R$ 5.00".format(cinco))
print("{:.0f} nota(s) de R$ 2.00".format(dois))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00".format(um))
print("{:.0f} moeda(s) de R$ 0.50".format(cent50))
print("{:.0f} moeda(s) de R$ 0.25".format(cent25))
print("{:.0f} moeda(s) de R$ 0.10".format(cent10))
print("{:.0f} moeda(s) de R$ 0.05".format(cent5))
print("{:.0f} moeda(s) de R$ 0.01".format(cent1))
