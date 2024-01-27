# 10818 최소, 최대
n = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))

2562 최대값
numbers = []
for i in range(9):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers))+1)

# 10810 공 넣기

n, m  = map(int, input().split())
basket = [0] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        basket[idx] = k

for i in range(1, n+1):
    print(basket[i], end = ' ')

#10813 공 바꾸기
N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for b in basket:
    print(b, end = ' ')

# 3052 나머지
numbers = []
for _ in range(10):
    n = int(input())
    if n%42 not in numbers:
        numbers.append(n % 42)
print(len(numbers))

# 10811 바구니 뒤집기
N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for i in range(N):
    print(basket[i], end = ' ')

# 1546 평균
n = int(input())
score = list(map(int, input().split()))
M = max(score)

for i in range(n):
    score[i] = score[i]/M*100

print(sum(score)/n)