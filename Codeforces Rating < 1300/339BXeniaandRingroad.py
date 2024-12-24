def ringRoad(n, m, nums):
    steps = 0
    current = 1

    for stop in nums:
        if stop >= current:
            steps += stop - current
        else:
            steps += (n - current) + stop
        current = stop

    print(steps)

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().rstrip().split()))
    ringRoad(n, m, nums)
