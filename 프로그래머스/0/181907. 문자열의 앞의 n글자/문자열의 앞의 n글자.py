def solution(my_string, n):
    my = []
    for i in range(n):
        my.append(my_string[i])
    
    answer = ''.join(my)
    return answer