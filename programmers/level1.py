# 카드 뭉치 

cards1 = ['i','drink','water']
cards2 = ['want','to']
goal = ['i','want','to','drink','water']

def solution(cards1, cards2, goal):
    answer = []
    n = len(cards1)
    m = len(cards2)

    i = j = 0

    for word in goal:
        if i < n and word == cards1[i]:
            answer.append(cards1[i])
            i += 1
        if j < m and word == cards2[j]:
            answer.append(cards2[j])
            j += 1
    if answer == goal:
        return 'Yes'
    else:
        return 'No'
    return answer       

result = solution(cards1, cards2, goal)
print(result)

# 크기가 작은 부분 문자열
t = '3141592'
p = '271'

def solution(t, p):
    answer = 0
    t_len = len(t)
    p_len = len(p)

    p = int(p)

    for i in range(0, t_len+1-p_len):
        if int(t[i:i+p_len]) <= p:
            answer += 1
    return answer

result = solution(t, p)
print(result)

# 추억 점수

name = ['may','kein','kain','radi']
yearning = [5,10,1,3]
photo = [['may'],['kein'],['deny'],['may'],['kon'],['coni']]

def solution(name, yearning, photo):
    answer = []
    for i in name:
        score = 0
        for n in i:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)
    return answer

result = solution(name, yearning, photo)
print(result)

# 접두사인지 확인하기

my_string = 'banana'
is_prefix = 'ban'

def solution(my_string, is_prefix):
    answer = 0
    tmp = [my_string[:i] for i in range(0, len(my_string))]
    for i in tmp:
        if is_prefix == i:
            answer = 1
        
    return answer

result = solution(my_string, is_prefix)
print(result)

# 명예의 전당

k = 3
score = [10,100,20,150,1,100,200]

def solution(k, score):
    answer = []
    a = []
    for i in score:
        if len(a) < k:
            a.append(i)
        else:
            if min(a) < i:
                a.remove(min(a))
                a.append(i)
        answer.append(min(a))

    return answer

result = solution(k, score)
print(result)

# 푸드 파이트 대회

food = [1,3,4,6]

def solution(food):
    answer = ''
    for i in range(0, len(food)):
        answer += str(i) * (food[i]//2)
    temp = ''.join(reversed(list(answer)))        
    return answer + '0' + temp

result = solution(food)
print(result)

# 과일 장수 

k = 3
m = 4
score = [1,2,3,1,2,3,1]

def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)    # 큰 값을 먼저 처리하기 위해 먼저 내림차순으로 정렬 --> sorted 함수와 reverse = True로 내림차순 정렬해줌
    for i in range(0, len(score), m):        # score 리스트를 m 개씩 묶어서 처리함.
        tmp = score[i:i+m]                   # score 리스트에서 m 개씩 묶인 부분 리스트가 저장됨.
        
        if len(tmp) == m:
            answer += min(tmp) * m
    return answer

result = solution(k, m, score)
print(result)