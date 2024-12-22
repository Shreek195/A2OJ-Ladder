n = int(input())

if n%2 == 1:
    print(-1)
else:
    ans = []
    for i in range(2, n + 1, 2):
        ans.extend([i, i-1])
    print(*ans)
