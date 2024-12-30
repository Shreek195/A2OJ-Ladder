# Solution 1
def approach(n, nums, m, search):
    # Use a dictionary to count occurrences of each value in the search list
    search_count = {}
    for val in search:
        search_count[val] = search_count.get(val, 0) + 1

    v = 0
    p = 0

    # Iterate through nums and compute v and p
    for i, val in enumerate(nums):
        if val in search_count:
            count = search_count[val]
            v += (i + 1) * count
            p += (n - i) * count

    return f"{v} {p}"

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    m = int(input())
    search = list(map(int, input().rstrip().split()))

    print(approach(n, nums, m, search))

# Solution 2
def approach(n, nums, m, search):
    v, p = 0, 0

    ele_count = {}
    for val in search:
        ele_count[val] = ele_count.get(val, 0) + 1
    
    for i, val in enumerate(nums):
        if val in ele_count:
            count = ele_count[val]
            v += (i + 1) * count
            p += (n - i) * count

    return f"{v} {p}"

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    m = int(input())
    search = list(map(int, input().rstrip().split()))

    print(approach(n, nums, m, search))
