def solution(my_string, is_prefix):
    answer = 1
    for i in range(len(is_prefix)):
        if(i<=len(my_string)-1):
            if(my_string[i] == is_prefix[i]):
                mul = 1
            else:
                mul = 0
        else:
            mul = 0
        answer *= mul
    return answer