def main():
    n = int(input())
    s_all = b_all = a_all = s1_all = b1_all = a1_all = 0
    for c in range(n):
        nome = input()
        s, b, a = map(int, input().split())
        s1, b1, a1 = map(int, input().split())
        s_all += s
        b_all += b
        a_all += a
        s1_all += s1
        b1_all += b1
        a1_all += a1

    pontos_saque = (100 * s1_all)/ s_all
    print("Pontos de Saque: {:.2f} %.".format(pontos_saque))
    pontos_bloqueio = (100 * b1_all)/ b_all
    print("Pontos de Bloqueio: {:.2f} %.".format(pontos_bloqueio))
    pontos_ataque = (100 * a1_all)/ a_all
    print("Pontos de Ataque: {:.2f} %.".format(pontos_ataque))

main()
