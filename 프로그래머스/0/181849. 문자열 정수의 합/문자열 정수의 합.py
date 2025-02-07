def solution(num_str):
    total = 0
    for i in range(len(num_str)):
        total += int(num_str[i])
    return total