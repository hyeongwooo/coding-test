# 백준 1271 엄청난 부자
import sys
n, m = map(int, sys.stdin.readline().split(' '))
print(n//m)
print(n%m)

# 백준 2338 긴자리 계산
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

# 백준 2558 A+B-2
a = int(input())
b = int(input())
print(a+b)

# 백준 3003 킹,퀸,룩,비숍,나이트,폰
# 내가 푼 풀이
import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split(' '))
h, i, j, k, l, m = 1, 1, 2, 2, 2, 8
print(h-a, i-b, j-c, k-d, l-e, m-f)

# 두번째 방볍
chess = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))
for i in range(6):
    print(chess[i] - a[i], end = '')

# 백준 3733 shares
while 1:
    try:
        n, s = map(int, input().split())
    except EOFError:
        break
    else:
        print(s//(n+1))

# 백준 4101 크냐?
while 1:
    a, b = map(int, input().split())
    if a==0 and b ==0:
        break
    elif a > b:
        print("Yes")
    else:
        print("No")

# 백준 4999 아
a = str(input())
b = str(input())

if len(a) >= len(b):
    print('go')
else:
    print('no')

# 백준 5341 pyramid
while 1:
    result = 0
    a = int(input())
    if a == 0:
        break
    for i in range(1, a+1):
        result += i
    print(result)

# 백준 5522 카드게임
sum = 0
for i in range(5):
    score = int(input())
    sum += score
print(sum)

# 백준 6840 who is the middle?
import sys
import math

list = []
list.append(int(input()))
list.append(int(input()))
list.append(int(input()))
print(sorted(list)[1])

# 백준 7891 can you add this?
a = int(input())
for _ in range(a):
    b, c = map(int, input().split(' '))
    print(b+c)

# 백준 10757 큰 수 A+B
import sys
a, b = map(int, sys.stdin.readline().split())
print(a+b)

