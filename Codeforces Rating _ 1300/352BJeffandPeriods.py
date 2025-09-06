from collections import defaultdict

def valid(n, nums):
    idxMap = defaultdict(list)
    for i, value in enumerate(nums):
        idxMap[value].append(i+1)

    results = []
    for x, idx in idxMap.items():
        if len(idx) == 1:
            results.append((x, 0))
        else:
            p = idx[1] - idx[0]
            is_valid = all(idx[i] - idx[i-1] == p for i in range(2, len(idx)))
            if is_valid:
                results.append((x, p))

    results.sort()

    print(len(results))
    for x, p in results:
        print(x, p)

if __name__ == "__main__":
    n, nums = int(input()), list(map(int, input().rstrip().split()))
    valid(n, nums)
