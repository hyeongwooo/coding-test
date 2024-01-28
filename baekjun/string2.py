# 11720 숫자의 합
n = int(input())
number = input()
total = 0
for i in range(n):
    total += int(number[i])

# print(total)

# 10809 알파벳 찾기
alp = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in alp:
        print(alp.index(i), end = ' ')
    else:
        print(-1, end = ' ')

# 2675 문자열 반복

# n = int(input())
for _ in range(n):
    a, b = input().split()
    for x in b:
        print(x*int(a), end = '')
    print()
        
# 1152 단어의 개수
a = input().split()
print(len(a))

# 2908 상수
a, b = input().split()  # int형태는 슬라이싱 할 수 없기 때문에 문자열 형태로 입력받아야함!
a = int(a[::-1])        # step ---> a[start:end:step]
b = int(b[::-1]) 
if a > b:
    print(a)
else:
    print(b)

# 5622 다이얼
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
loc = 0
for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            loc += dial.index(j)+3
print(loc)
