def solution(my_string, n):
    l = len(my_string) - n
    my = []
    for i in range(n):
        my.append(my_string[l+i])
        
    answer = ''.join(my)
    return answer