def main():
    n = int(input())
    for c in range(n):
        t = int(input())
        anos = 2015 - t
        if anos > 0:
            print(anos, "D.C.")
        else:
            print((anos - 1) * -1, "A.C.")

main()
