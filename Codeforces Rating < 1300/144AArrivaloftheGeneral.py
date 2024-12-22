def general(n, nums):
    maxIdx = minIdx = 0
    for i in range(len(nums)):
        if nums[i] <= nums[minIdx]:
            minIdx = i
        if nums[i] > nums[maxIdx]:
            maxIdx = i

    if maxIdx > minIdx:
        steps = maxIdx + (n-1 - minIdx) - 1
    else:
        steps = maxIdx + (n-1 - minIdx)

    print(steps)
        
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    general(n, nums)
