def solution(arr1, arr2):
    answer = 0
    total_arr1 = 0
    total_arr2 = 0
    if (len(arr1) > len(arr2)):
        answer = 1
    elif(len(arr2) > len(arr1)):
        answer = -1
    else:
        for i in range(len(arr1)):
            total_arr1 += arr1[i]
            total_arr2 += arr2[i]
        if(total_arr1 > total_arr2):
            answer = 1
        elif(total_arr2 > total_arr1):
            answer = -1
        else:
            answer = 0
    return answer