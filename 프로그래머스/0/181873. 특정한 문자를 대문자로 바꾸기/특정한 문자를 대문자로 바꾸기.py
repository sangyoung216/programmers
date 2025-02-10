def solution(my_string, alp):
    alp_Large = alp.upper()
    answer = my_string.replace(alp, alp_Large)
    return answer