import sys

n, m = map(int, sys.stdin.readline().split())

pokemons = [sys.stdin.readline().strip() for _ in range(n)]
questions = [sys.stdin.readline().strip() for _ in range(m)]

d = {name: i+1 for i, name in enumerate(pokemons)}

for q in questions:
    if q.isdigit():
        print(pokemons[int(q) - 1])
    else:
        print(d[q])