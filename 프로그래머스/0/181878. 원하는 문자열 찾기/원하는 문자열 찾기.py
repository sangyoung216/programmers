def solution(myString, pat):
    myString_small = myString.lower()
    pat_small = pat.lower()
    if(pat_small in myString_small):
        answer = 1
    else:
        answer = 0
    return answer