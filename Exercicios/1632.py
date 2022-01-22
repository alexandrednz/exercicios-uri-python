def main():
    t = int(input())
    for c in range(t):
        senha = input()

        lista_letrasnumero = ["A", "a", "E", "e", "I", "i", "O", "o", "S", "s"]
        letrasnumero = 0

        for n in senha:
            for i in lista_letrasnumero:
                if n == i:
                    letrasnumero += 1

        variacoes = (2 ** (len(senha) - letrasnumero)) * (3 ** letrasnumero)

        print(variacoes)

main()
