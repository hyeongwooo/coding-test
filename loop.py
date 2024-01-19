# 백준 2741 n번 찍기
N = int(input())
for i in range(N):
    print(i+1, sep = '')

# 백준 10872 팩토리얼
N = int(input())
result = 1            # factorial의 초기값은 1이므로 1로 초기화
if 0<= N <=12:
    for i in range(1, N+1):
        result *= i 
print(result)

# 백준 10952 A+B=5
while 1:
    a, b = map(int, input().strip().split(' '))
    if (a==0 and b==0):
        break
    else:
        print(a+b)

# 백준 2739 구구단 출력
n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n*i)

# 백준 2438 별 찍기 
n = int(input())
for i in range(1, n+1):
    print('*'*i)

# 백준 10951 사칙연산
while 1:
    try:
        a, b = map(int, input().strip().split(' '))
        print(a+b)
    except EOFError:
        break
## 위 문제는 문자열을 입력받아 EOF(End of File)를 판단할 수 있는 문제임. 
## 입력으로 테스트 케이스가 주어지지 않으므로 EOF를 판단해서 프로그램을 종료해야함.
## 파이썬으로 EOF 판단하는 방법은 두가지가 있음
# 1. 
# while 1:
#      try:
#         a, b = map(int, input().strip().split(' '))
#         print(a+b)
#      except EOFError:
#         break
# 2. 
# import sys
# lines = sys.stdin.readlines()
# for line in lines:
#     a, b = map(int, input().strip().split(' '))
#     print(a+b)
