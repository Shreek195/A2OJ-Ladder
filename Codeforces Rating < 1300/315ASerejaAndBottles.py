def sereja(n, bottles):
    unopened = 0
    
    for i in range(n):
        valid = False
        for j in range(n):
            if i != j and bottles[i][0] == bottles[j][1]:
                valid = True
                break

        if not valid:
            unopened += 1

    return unopened

if __name__ == "__main__":
    n = int(input())
    bottles = [tuple(map(int, input().rstrip().split())) for i in range(n)]
    print(sereja(n, bottles))
