def solution(num_list):
    answer = 0
    i = 0
    while 1:
        if(i==len(num_list)):
            answer = -1
            break
        elif(num_list[i]<0):
            answer = i
            break
        else:
            i = i+1
        
    return answer