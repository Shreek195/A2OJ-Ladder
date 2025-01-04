def hq9(s):
    chars = ['H', 'Q', '9']

    if any(i in chars for i in s):
        print("YES")
        return
    print("NO")

if __name__ == "__main__":
    hq9(input().rstrip())
