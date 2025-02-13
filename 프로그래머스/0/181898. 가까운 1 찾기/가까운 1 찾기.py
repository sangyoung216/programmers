def solution(arr, idx):
    i = 0
    answer = -1
    while (i<=len(arr)-1):
        if(i>=idx):
            if(arr[i] == 1):
                answer = i
                break
        i += 1
    return answer