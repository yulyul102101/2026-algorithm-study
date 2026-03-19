import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    teams_win = {i: 0 for i in range(1, n + 1)}
    teams_lose = {i: 0 for i in range(1, n + 1)}
    for _ in range(m):
        a, b, p, q = map(int, sys.stdin.readline().split())
        teams_win[a] += p
        teams_lose[a] += q
        teams_win[b] += q
        teams_lose[b] += p
    teams_score = {i : pow(teams_win[i], 2)/(pow(teams_win[i], 2) + pow(teams_lose[i], 2)) if pow(teams_win[i], 2) + pow(teams_lose[i], 2) != 0 else 0 for i in range(1, n + 1)}
    res_max = max(teams_score.values())
    res_min = min(teams_score.values())
    print(int(res_max * 1000))
    print(int(res_min * 1000))
