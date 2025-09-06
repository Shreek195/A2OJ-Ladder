def evenOdd(n, k):
    odd_count = (n + 1) // 2
    if k <= odd_count:
        print(2 * k - 1)
    else:
        print(2 * (k - odd_count))

if __name__ == "__main__":
    n, k = map(int, input().split())
    evenOdd(n, k)
