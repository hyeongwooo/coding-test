# 문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.
# ["a","b","c"] --> ["a,b,c"]

def solution(arr):
    answer = ''
    for i in (arr): # for i in range에서 range는 정수 범위에 대해서만 작동!!
        answer += i
    return answer

input_array = ["a","b","c"]
result = solution(input_array)
print(result)