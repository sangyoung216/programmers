def solution(strArr):
    answer = []
    value = ''
    for i in range(len(strArr)):
        if(i%2==0):
            value = strArr[i].lower()
            answer.append(value)
        else:
            value = strArr[i].upper()
            answer.append(value)
    return answer