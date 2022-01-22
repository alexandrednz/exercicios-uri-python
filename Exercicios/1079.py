def main():

    n = int(input())
    for c in range(1, n + 1):
        v1, v2, v3 = map(float, input().split())
        mediapond = (v1 * 2 + v2 * 3 + v3 * 5)/10
        print("{:.1f}".format(mediapond))

main()
