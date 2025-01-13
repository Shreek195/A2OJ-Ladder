from collections import Counter

def valid(n, k, s):
    freq = Counter(s)
    freqCount = sorted(freq.values(), reverse=True)

    coins = 0
    for i in freqCount:
        if k == 0:
            break
        take = min(i, k)
        coins += take ** 2
        k -= take

    return coins

if __name__ == "__main__":
    n, k = map(int, input().rstrip().split())
    s = input().strip()

    print(valid(n, k, s))
