# 백준 15964 이상한 기호
import sys
a, b = map(int, sys.stdin.readline().split(' '))
answer = (a+b)*(a-b)
print(answer)

# 백준 2475 검증수
import sys
a, b, c, d, e = map(int, sys.stdin.readline().split(' '))
answer = ((a**2)+(b**2)+(c**2)+(d**2)+(e**2))%10
print(answer)

# 두번째 방법(반복문으로 해결가능!)
import sys
num = map(int, sys.stdin.readline().split(' '))
result = 0
for i in num:
    result += i**2
print(result%10)
