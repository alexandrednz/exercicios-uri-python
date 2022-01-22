def main():
    a, b, c = map(int, input().split())
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Valido-Equilatero")
        elif a != b and b != c and a != c:
            print("Valido-Escaleno")
        else:
            print("Valido-Isoceles")

        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("Retangulo: S")
        else:
            print("Retangulo: N")
    else:
        print("Invalido")

main()
