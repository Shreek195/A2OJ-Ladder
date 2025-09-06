def word():
    str1 = input().strip()
    cnt = len(str1)

    for i in str1:
        cnt = cnt-1 if i.islower() else cnt+1
        
    return str1.upper() if cnt > len(str1) else str1.lower()

if __name__ == "__main__":
    result = word()
    print(result)
