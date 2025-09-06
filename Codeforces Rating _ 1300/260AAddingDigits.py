def digits(a, b, n):
    # Calculate the remainder when 10 * a is divided by b
    r = (10 * a) % b
    
    # Find the first valid digit to append
    d = (b - r) % b if r != 0 else 0  # If r == 0, the valid digit is 0
    
    # If the digit is invalid (not a single digit), return -1
    if d > 9:
        return -1
    
    # Append `d` and add `n-1` zeroes to create the required number
    result = str(a) + str(d) + '0' * (n-1)

    return result
    
if __name__ == "__main__":
    a, b, n = map(int, input().split())
    print(digits(a, b, n))
