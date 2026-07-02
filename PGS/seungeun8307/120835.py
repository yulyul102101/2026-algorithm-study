def solution(emergency):
    answer = []
    sem = sorted(emergency, reverse=True)
    no = {num: i+1 for i, num in enumerate(sem)}
    answer = [no[num] for num in emergency]
    return answer