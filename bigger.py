# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

def solution(a, b):
    answer = 0
    # sum = str(a) + str(b)
    # sum_other = str(b) + str(a)
    # if sum > sum_other:
    #     return sum
    # else:
    #     return sum_other
    # 위와 같은 방법으로 해도 실행은 되는데 왜 오류가 나는지?....
    a, b = str(a), str(b)
    if int(a+b) >= int(b+a):
        return int(a+b)
    else:
        return int(b+a)


    
a, b = map(int, input().strip().split(' '))
result = solution(a, b)
print(result)