# my_string, overwrite_string, s_str = input().strip().split(' ')
# s = input(s_str)
# def solution(my_string, overwrite_string, s):
#     answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
#     return answer

# result = solution(my_string, overwrite_string, s)
# print(result)

def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

# 입력 받기
my_string, overwrite_string, s_str = input().strip().split(' ')
s = int(s_str) # 문자열을 정수형으로 변환

# 함수 호출 및 결과 출력
result = solution(my_string, overwrite_string, s)
print(result)
