def rozdil(n, nums):
    print("Still Rozdil" if nums.count(min(nums)) > 1 else f"{nums.index(min(nums)) + 1}")

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().rstrip().split()))

    rozdil(n, nums)
