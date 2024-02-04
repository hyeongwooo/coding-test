# 2083 럭비클럽
while 1:
    name, age, weight = input().split()
    if '#' in name:
        break
    if int(age) > 17 or int(weight) >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')

# 3046 R2
r1, s = map(int, input().split())
r2 = ((2 * s)-r1)
print(r2)

# 4470 줄번호
n = int(input())
for i in range(n):
    name = input()
    print('%d. %s' % (i, name))    # %d는 이자리에 정수가 들어갈 것이라는 의미 / %s는 이자리에 문자열이 들어간다는 의미 / 마지막 %는 앞의 의미들이 뒤에 대응된다는 뜻

# 4562 no brainer
n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    if a < b:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")

# 10156 과자
k, n, m = map(int, input().split())
if k * n == m or m > k * n:
    print("0")

elif k * n > m:
    print((k*n)-m)
else:
    print(m-(k*n))

# 10101 삼각형
a = int(input())
b = int(input())
c = int(input())
if a + b + c == 180:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print(" Isosceles")
    else:
        print("Scalene")
else:
    print("Error")

# 10768 특별한 날
month = int(input())
day = int(input())

if month < 2:
    print("Before")
elif month == 2:
    if day == 18:
        print("Special")
    elif day < 18:
        print("Before")
    else:
        print("After")
else:
    print("After")

# 10797 10부제
import sys
day = int(input())
num = list(map(int, input().split()))

cnt = 0 

for i in range(len(num)):
    if num[i] == day:
        cnt += 1
    else:
        continue
print(cnt)