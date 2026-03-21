'''
import sys

IBSN = sys.stdin.readline()
m = int(IBSN[-2])

ibsnI = []
ind = 0
for i in range(13):
    if IBSN[i]=='*' : ibsnI.append(IBSN[i]);ind=i
    else: ibsnI.append(int(IBSN[i])) 

for i in range(13):
    if i==ind : continue
    elif i%2!=0 : m += ibsnI[i]
    else: m += ibsnI[i]*3

a = m%10 -1
print(a)
'''