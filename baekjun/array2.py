# 2738 행렬 덧셈
import sys
A, B = [], []
a, b = map(int, sys.stdin.readline().split(' '))

for row in range(a):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(b):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(a):
    for col in range(b):
        print(A[row][col] + B[row][col], end = ' ')
    print()

# 2566 최댓값 
table = [list(map(int, input().split())) for _ in range(9)]  # 9개의 숫자로 이루어진 여러 줄의 입력을 받아 9x9 크기의 이차원 리스트의 table에 저장

max_num = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row = row +1
            max_col = col +1
            max_num = table[row][col]
        
print(max_num)
print(max_row, max_col)

10798 세로읽기
table = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(table[i]):
            print(table[i][j], end = '')


# 2563 색종이
array = [[0 for _ in range(101)]for _ in range(101)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    for row in range(a, a+10):
        for col in range(b, b+10):
            array[row][col] = 1    # 가로, 세로 방향으로 10x10 크기의 사각형 부분이 1로 채워진다. 

result = 0

for i in array:
    result += i.count(1)          # 시작하는 10x10 크기의 사각형 영역에 1을 채우고, 최종적으로 전체 배열에서 1의 개수를 세어 출력
print(result)