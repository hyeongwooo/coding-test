# 2444 별찍기-7
n = int(input())
for i in range(1,n):
    print(' '*(n-i)+'*'*(2*i-1))
for j in range(n, 0, -1):
    print(' '*(n-j)+'*'*(2*j-1))

# 10988 팰린드룸
word = list(input())
if word[0:] != word[::-1]:   # if list(reversed(word)) --> reversed 함수를 쓰면 더 쉽게 해결가능!
    print("0")
else:
    print("1")

# 1157 단어 공부
word = input().upper()
my_word = list(set(word))        

num_list = []
for i in my_word:
    num = word.count(i)
    num_list.append(num)

if num_list.count(max(num_list)) > 1:
    print('?')
else:
    max_index = num_list.index(max(num_list))
    print(my_word[max_index])

# 2941 크로아티아 알파벳
word = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in alpha:
    word = word.replace(i, '*')     # alpah의 문자들을 *로 치환한다. --> 그렇게 하게 되면 쉽게 c= 이런 문자들을 하나로 치환하기 때문에 문자열이 몇개인지 쉽게 구할 수 있다!
print(len(word))

# 1316 그룹 단어 체커
n = int(input())
cnt = n
for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)

# 25206 너의 평점은
rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total = 0
result = 0 
for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        total += b 
        result += b * grade[rating.index(c)]
print('%6f' % (result/total))