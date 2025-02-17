def solution(my_strings, parts):
    my = []
    for i in range(len(my_strings)):
        start = parts[i][0]
        end = parts[i][1]
        my.append(my_strings[i][start:end+1])

    answer = ''.join(my)
    return answer