# 문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.
# my_string	k	result
# "string"	3	"stringstringstring"
# "love"	10	"lovelovelovelovelovelovelovelovelovelove"

# def solution(my_string, k):
#     answer = ''
#     for k in (my_string):
#         answer = my_string + my_string[k] 
#     return answer

# my_string, k = input().strip().split(' ')
# k = int(k)
# result = solution(my_string, k)
# print(result)

def solution(my_string, k):
    return my_string * k

my_string, k = input().strip().split(' ')
k = int(k)
result = solution(my_string, k)
print(result)
