def drinks(n, nums):
    return sum(nums) / n

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    print(drinks(n, nums))
