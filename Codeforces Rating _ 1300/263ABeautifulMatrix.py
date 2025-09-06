def beautiful_matrix():
    steps = 0
    for _ in range(5):
        nums = list(map(int, input().split()))
        if 1 in nums:
            # Calculate matrix inner steps to bring element in middle 
            # Calculate list inner steps to bring elemnet in middle
            steps = abs(_ - 2) + abs(nums.index(1) - 2)

    print(steps)
    return
            

if __name__ == "__main__":
    beautiful_matrix()
