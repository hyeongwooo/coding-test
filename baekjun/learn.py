# 1977 완전제곱수
a = int(input())
b = int(input())
sum = 0
min = 0

for i in range(1, 101):
    if a<= i*i and b>= i*i:
        if sum == 0:
            min = i*i
        sum += i*i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)

# 5635 생일
list = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    d, m, y = map(int, (d, m, y))
    list.append((y, m, d, n))
list.sort()
print(list[-1][3])
print(list[0][3])



