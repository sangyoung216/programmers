def solution(num_list):
    total_odd = 0
    total_even = 0
    for i in range(len(num_list)):
        if(i%2==0):
            total_odd += num_list[i]
        else:
            total_even += num_list[i]
    
    return total_odd if total_odd >= total_even else total_even