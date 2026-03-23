import sys

n = int(sys.stdin.readline().strip())
s, m, l, xl, xxl, xxxl = map(int, sys.stdin.readline().split())
t, p = map(int, sys.stdin.readline().split())

d = {
    's': s // t if s % t == 0 else s // t + 1, 
    'm': m // t if m % t == 0 else m // t + 1, 
    'l': l // t if l % t == 0 else l // t + 1,  
    'xl': xl // t if xl % t == 0 else xl // t + 1, 
    'xxl': xxl // t if xxl % t == 0 else xxl // t + 1,  
    'xxxl': xxxl // t if xxxl % t == 0 else xxxl // t + 1, 
    }

print(sum(d.values()))
print(n//p, n%p)