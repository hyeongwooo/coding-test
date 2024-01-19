# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

# a	b	result
# 2	91	364
# 91	2	912

def solution(a, b):
    answer = 0
    a, b = str(a), str(b)
    if int(a+b) > 2 * int(a) * int(b):
        return int(a+b)
    else:
        return 2 * int(a) * int(b)
    
a, b = map(int, input().strip().split(' '))
result = solution(a, b)
print(result)