def solution(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total/len(numbers)