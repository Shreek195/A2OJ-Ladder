def hq9(s):
    chars = ['H', 'Q', '9']

    if any(i in chars for i in s):
        return "YES"
    return "NO"

if __name__ == "__main__":
    print(hq9(input().rstrip()))
