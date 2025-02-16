def solution(my_string, is_suffix):
    answer = 1
    l = len(my_string) - len(is_suffix)
    if(l>=0):
        for i in range(len(is_suffix)):
            if(my_string[l+i] == is_suffix[i]):
                answer *= 1
            else:
                answer *= 0
    else:    
        answer = 0
    return answer