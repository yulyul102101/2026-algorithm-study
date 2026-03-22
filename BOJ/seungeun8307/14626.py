import sys

IBSN = sys.stdin.readline().strip()

ibsnI = []
ind = 0
for i in range(13):
    if IBSN[i] == '*':
        ibsnI.append('*')
        ind = i
    else: ibsnI.append(int(IBSN[i]))

m = 0
for i in range(13):
    if i == ind: continue
    if i % 2 == 0: m += ibsnI[i]
    else: m += ibsnI[i] * 3

for j in range(10):
    tmp = j * (1 if ind % 2 == 0 else 3) + m
    if tmp % 10 == 0:
        print(j)
        break