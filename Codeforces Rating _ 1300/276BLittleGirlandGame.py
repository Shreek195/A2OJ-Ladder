from collections import Counter

def gameWinner(s):
    countMap = Counter(s)

    ans = sum(1 for i in countMap.values() if i%2 != 0)
    print("First" if ans == 0 or ans%2 == 1 else "Second")

if __name__ == '__main__':
    gameWinner(input().rstrip())
