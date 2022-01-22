def main():
    n = int(input())
    fat = 1
    for c in range(n, 0, -1):
        fat = fat * c
    print(fat)

main()