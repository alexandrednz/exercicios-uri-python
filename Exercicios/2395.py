def main():
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())

    n = int(x/a) * int(y/b) * int(z/c)

    print(n)

main()