def funcForBook(n, nums):
    cnt = 0
    i = 0
    while cnt < n:
        cnt += nums[i%7]
        i += 1
    
    print(i % 7 if i % 7 != 0 else 7)

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    funcForBook(n, nums)
