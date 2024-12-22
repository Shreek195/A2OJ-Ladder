from collections import Counter

def valid(n, nums):
    count = Counter(nums)
    if count[5] >= 9:
        if count[0] > 0:
            value = ((count[5] // 9) * 9)  * "5" + count[0] * "0"
            print(value)
        else:
            print("-1")
    else:
        print(0 if count[0] > 0 else -1)

if __name__ == "__main__":
    n, nums = int(input()), list(map(int, input().rstrip().split()))
    valid(n, nums)
