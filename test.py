# 백준 1001
def solution(A, B):
    div = A - B 
    return div

A, B = map(int, input().strip().split(' '))
result = solution(A, B)
print(result)

#백준 곱셈10998
A, B = map(int, input().strip().split(' '))
print(A*B)

# 백준 10869
A, B = map(int, input().strip().split(' '))
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# 백준 1008
A, B = map(int, input().strip().split(' '))
print(A/B)

# 백준 11382
A, B, C = map(int, input().strip().split(' '))
print(A+B+C)