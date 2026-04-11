import sys

n = int(sys.stdin.readline())

for _ in range(n):
    ox_result = sys.stdin.readline().strip()
    total_score = 0
    current_streak = 0
    
    for char in ox_result:
        if char == 'O':
            current_streak += 1
            total_score += current_streak
        else:
            current_streak = 0
            
    print(total_score)