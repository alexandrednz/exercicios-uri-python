def main():

    x, y = map(int, input().split())
    while x != y:
        if x < y:
            print("Crescente")
        elif x > y:
            print("Decrescente")

        x, y = map(int, input().split())

main()
