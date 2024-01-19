def solution(str1, str2):
    answer = '' # 변수가 비어있는 문자열로 초기화
    for i in range(0, len(str1)):
        answer = answer + str1[i] + str2[i]

    return answer

str1, str2 = input().strip().split(' ')
result = solution(str1, str2)
print(result)