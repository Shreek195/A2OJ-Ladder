def toggle(x):
    return 1 if x == 0 else 0

def lightsOut():
    mat = [list(map(int, input().split())) for i in range(3)]
    ans = [[1, 1, 1], 
           [1, 1, 1], 
           [1, 1, 1]]

    for i in range(3):
        for j in range(3):
            if mat[i][j] % 2 == 1:
                ans[i][j] = toggle(ans[i][j])
                if i < 2:
                    ans[i+1][j] = toggle(ans[i+1][j])
                if i > 0:
                     ans[i-1][j] = toggle(ans[i-1][j])
                if j < 2:
                     ans[i][j+1] = toggle(ans[i][j+1])
                if j > 0:
                     ans[i][j-1] = toggle(ans[i][j-1])
    return ans

if __name__ == "__main__":
    result = lightsOut()

    for _ in result:
        print(''.join(map(str, _)))
