def football():
    n = int(input())
    teams = {}

    for _ in range(n):
        team = input().rstrip()
        if team in teams:
            teams[team] += 1
        else:
            teams[team] = 1
            
    winner = max(teams, key=teams.get)
    return winner
            
if __name__ == "__main__":
    print(football())
