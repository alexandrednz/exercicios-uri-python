def main():
    for c in range(int(input())):
        linha = input()
        valores = []
        contador = 0
        valor = ""
        for i in linha:
            try:
                if i in "0123456789":
                    valor = valor + i
                elif i not in "0123456789" and linha[contador + 1] in "0123456789":
                    valores.append(valor)
                    valor = ""
            except IndexError:
                pass
            contador += 1

        valores.append(valor)
        print(int(valores[1]) + int(valores[2]) + int(valores[3]))

main()