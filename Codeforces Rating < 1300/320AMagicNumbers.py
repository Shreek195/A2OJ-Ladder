def magic(n):
    if n[0] !='1':
        return "NO"

    freqMap = {1: 1, 4: 0}

    for i in range(len(n)):
        if n[i] == '1':
            freqMap[4] = 0
        elif n[i] == '4':
            freqMap[4] += 1
            if freqMap[4] >= 3:
                return "NO"
        else:
            return "NO"

    return "YES"

if __name__ == "__main__":
    print(magic(input()))
