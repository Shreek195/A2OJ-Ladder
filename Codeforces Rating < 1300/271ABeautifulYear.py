def beautifulYear(year):
    while True:
        a = year % 10
        b = (year // 10) % 10
        c = (year // 100) % 10
        d = (year // 1000) % 10

        if len({a, b, c, d}) == 4: 
            return year
        year += 1

if __name__ == "__main__":
    y = int(input())
    print(beautifulYear(y + 1))
