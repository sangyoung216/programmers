def solution(n, k):
    answer = []
    i = 1
    while 1:
        if(n<k*i):
            break
        else:
            answer.append(k*i)
            i += 1
    return answer