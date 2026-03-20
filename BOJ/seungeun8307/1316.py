import sys

def gc(w):
    s = set()
    p = ''

    for ch in w:
        if ch != p:
            if ch in s: return False
            s.add(ch)
        p = ch
    return True


N = int(sys.stdin.readline())

count = 0
for i in range(N):
    w = sys.stdin.readline()
    if(gc(w)): count += 1

print(count)