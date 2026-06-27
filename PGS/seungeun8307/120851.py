def solution(my_string):
    nums = [int(i) for i in my_string if i.isdigit()]
    answer = sum(nums)
    return answer