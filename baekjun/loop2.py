# 백준 8393 합
a = int(input())
sum = 0
for i in range(1, a+1):
    sum += i
print(sum)

# 백준 25304 영수증

total = int(input())
num = int(input())
sum = 0

for i in range(num):
    price, cnt = map(int, input().split())
    sum += (price * cnt)

if total == sum:
    print("Yes")
else:
    print("No")

# 백준 25314 코딩은 체육과목 입니다. 
for _ in range(int(input())//4):
    print("long", end = " ")
print("int")

# 백준 11021 
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    sum = a+b
    print(f'Case #{i+1}: {sum}')  # fstring을 사용하여 문자열 출력 --> {} 를 써서 표현함!

# 백준 2439 별 찍기-2 
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)