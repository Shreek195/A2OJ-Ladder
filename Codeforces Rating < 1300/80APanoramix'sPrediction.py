import math

def check(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def funcPredict(n, m):
    # 7, 8, 9, 10, 11

    for i in range(n+1, m+1):
        if check(i):
            if i == m:
                print("YES")
                return
            else:
                break

    print("NO")
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    funcPredict(n, m)
