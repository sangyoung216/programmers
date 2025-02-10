def solution(num_list):
    leng = len(num_list)
    total = 0
    mul = 1
    if(leng > 10):
        for i in range(leng):
            total += num_list[i]
        answer = total
    else:
        for i in range(leng):
            mul *= num_list[i]
        answer = mul
    return answer