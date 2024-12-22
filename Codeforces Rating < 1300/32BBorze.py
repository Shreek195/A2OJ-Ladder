def borze():
    s = input().strip()
    i = 0
    result = ""
    borzeMap = {'.' : '0', '-.': '1', '--': '2'}

    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in borzeMap:
            result += borzeMap[s[i:i+2]]
            i += 2
        else:
            result += borzeMap[s[i]]
            i += 1

    print(result)
            
if __name__ == "__main__":
    borze()
