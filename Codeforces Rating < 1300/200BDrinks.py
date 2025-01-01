def drinks(n, nums):
    print(sum(nums) / n)

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    drinks(n, nums)
