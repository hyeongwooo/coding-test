# 백준 2884 알람시계
import sys
hour, min = map(int, sys.stdin.readline().split())
if min < 45:
    if hour == 0:
        hour = 23
        min += 60
    else:
        hour -= 1
        min += 60
    
print(hour, min-45)

# 백준 2525 오븐시계
import sys
hour, min = map(int, sys.stdin.readline().split())
plus = int(input())

hour += plus // 60
min += plus % 60

if min >= 60:
    hour += 1
    min -= 60

if hour >= 24:
    hour -= 24

print(hour, min)

# 백준 2480 주사위 세개
import sys
a, b, c = map(int, sys.stdin.readline().split())
if a==b==c:
    print(10000+(a*1000))
elif a==b:
    print(1000+(a*100))
elif b==c:
    print(1000+(b*100))
elif a==c:
    print(1000+(a*100))
else:
    print(max(a,b,c)*100)