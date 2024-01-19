# 백준 1330
A, B = map(int, input().strip().split(' '))
if A > B:
    print(">")
elif A < B: # elif: 이렇게만 써주면 안됨
    print("<")
else:
    print("==")

# 백준 9498
score = int(input())
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score <70:
    print("D")
else:
    print("F")

# 백준 14681 사분면 고르기
x, y = int(input()), int(input()) # 줄바꿈으로 입력 받고 싶으면 int(input())따로따로 두번 써주면 된다!
if x > 0 and y > 0:
    print("1")
elif x > 0 and y < 0:
    print("4")
elif x < 0 and y > 0:
    print("2")
else:
    print("3")

# 백준 2753 윤년 
year = int(input())

if ((year % 4 == 0) and (year % 100 !=0)) or (year % 400 ==0):
    print("1")
else:
    print("0")

# 백준 2420 사파리 월드 

N, M = map(int, input().strip().split(' '))
if N > M:
    print(N-M)
else:
    print(M-N)