def solution(myString, pat):
    myList = list(myString)
    for i in range(len(myList)):
        if(myList[i] == 'A'):
            myList[i] = 'B'
        elif(myList[i] == 'B'):
            myList[i] = 'A'

    rev_String = "".join(myList)
    if(pat in rev_String):
        answer = 1
    else:
        answer = 0
    return answer