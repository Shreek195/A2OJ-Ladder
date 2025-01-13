def can_sort_by_reversing_segment(n, a):
    sorted_a = sorted(a)
    
    # Find the first and last mismatch
    l, r = 0, n - 1
    while l < n and a[l] == sorted_a[l]:
        l += 1
    while r >= 0 and a[r] == sorted_a[r]:
        r -= 1
    
    # If no mismatch found, the array is already sorted
    if l > r:
        print("yes")
        print(1, 1)
        return
    
    # Reverse the segment [l, r] and check
    a[l:r+1] = a[l:r+1][::-1]
    if a == sorted_a:
        print("yes")
        print(l + 1, r + 1)  # Convert to 1-based indexing
    else:
        print("no")

# Input reading
n = int(input())
a = list(map(int, input().split()))

can_sort_by_reversing_segment(n, a)
