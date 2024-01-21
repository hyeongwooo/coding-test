# 백준 10871 x보다 작은 수
import sys
n, x = map(int, sys.stdin.readline().split(' '))  
num = list(map(int, input().split()))               # num 변수를 만들어 둘째 줄에 입력되는 숫자들을 list에 int로 집어넣는다.

for i in range(n):
    if num[i] < x:
        print(num[i], end = " ")

# 백준 10807 개수 세기
n = int(input())
num = list(map(int, input().split()))
v = int(input())

print(num.count(v))

# 백준 5597 과제 안내신분?...
student = [i for i in range(1, 31)] # 각 반복에서 i 값을 리스트에 포함시킨다. 
for _ in range (28):
    applied = int(input())
    student.remove(applied)   # remove() 함수를 사용하여 student에 있는 수에서 num에 해당하는 수를 삭제 --> 그럼 30명중에 입력한 28개 수가 삭제되므로 누가 안냈는지 바로 찾기 가능!
print(min(student))
print(max(student))

# 백준 2738 행렬 덧셈
import sys
A, B = [], []                                    # 행렬 받을 리스트 정의 
a, b = map(int, sys.stdin.readline().split(' ')) # a, b를 통해 행렬의 크기를 입력받음

for row in range(a):                             # A, B에 행렬의 원소를 입력받는다. 행의 크기만큼 입력을 반복하여 받는다. 
    row = list(map(int, input().split()))
    A.append(row)

for row in range(a):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(a):
    for col in range(b):
        print(A[row][col] + B[row][col], end = ' ')
    print()
