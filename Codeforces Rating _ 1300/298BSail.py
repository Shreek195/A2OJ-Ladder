from collections import Counter

def sail(t, sx, sy, ex, ey, d):
    dMap = Counter(d)
    x, y = ex - sx, ey - sy

    # Check if the target is unreachable
    if (x > 0 and dMap["E"] < x) or (x < 0 and dMap["W"] < -x) or \
       (y > 0 and dMap["N"] < y) or (y < 0 and dMap["S"] < -y):
        print(-1)
        return

    # Simulate the movement
    time = 0
    for i in d:
        if x == 0 and y == 0:  # Stop when the destination is reached
            print(time)
            return

        if x > 0 and i == "E":
            x -= 1
        elif x < 0 and i == "W":
            x += 1

        if y > 0 and i == "N":
            y -= 1
        elif y < 0 and i == "S":
            y += 1

        time += 1

    # If loop ends but destination is reached, print the time
    print(time if x == 0 and y == 0 else -1)

if __name__ == "__main__":
    t, sx, sy, ex, ey = list(map(int, input().rstrip().split()))
    direction = input().rstrip()
    sail(t, sx, sy, ex, ey, direction)
