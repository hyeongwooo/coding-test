# 백준 15552 빠른 입출력
import sys
n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split(' '))
    print(a+b)

# 반복문으로 여러 입력을 받는 경우 시간초과를 방지하기 위해 sys.stidin.readline() 사용