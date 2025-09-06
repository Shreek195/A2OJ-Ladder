def trip(k, months):
    sorted_months = sorted(months, reverse=True)
    result = 0
    cnt = 0

    if k == 0:
        return 0

    for month in sorted_months:
        result += month
        cnt += 1
        if result >= k:
            return cnt

    return -1

if __name__ == "__main__":
    k = int(input())
    months = list(map(int, input().rstrip().split()))
    result = trip(k, months)
    print(result)
