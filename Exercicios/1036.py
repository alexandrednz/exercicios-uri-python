def main():
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    delta = b**2 - 4*a*c
    if delta < 0 or a == 0:
        print("Impossivel calcular")
    else:
        R1 = (-b + delta**(1/2)) / (2 * a)
        R2 = (-b - delta**(1/2)) / (2 * a)
        print("R1 = {:.5f}".format(R1))
        print("R2 = {:.5f}".format(R2))


main()