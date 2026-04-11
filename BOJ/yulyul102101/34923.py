import sys

def solve():
    current_time_str = sys.stdin.readline().strip()
    target_time_str = sys.stdin.readline().strip()

    if not current_time_str or not target_time_str:
        return

    def to_minutes(time_str):
        h, m = map(int, time_str.split(':'))
        if h == 12:
            h = 0
        return h * 60 + m

    current_min = to_minutes(current_time_str)
    target_min = to_minutes(target_time_str)

    diff = abs(target_min - current_min)
    min_dist = min(diff, 720 - diff)

    print(min_dist * 6)

if __name__ == "__main__":
    solve()
