def solution(num_list, n):
    answer = []
    answer_left = num_list[0:n]
    answer_right = num_list[n:len(num_list)+1]
    answer = answer_right + answer_left
    return answer