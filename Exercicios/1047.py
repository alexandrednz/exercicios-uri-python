h1, m1, h2, m2 = map(int, input().split())

minutos1 = m1 + h1 * 60
minutos2 = m2 + h2 * 60

if minutos2 <= minutos1:
    minutos2 += 24 * 60

total = minutos2 - minutos1

minutos = total % 60
horas = total // 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))


