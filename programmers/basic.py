# 이어 붙인 수
num_list = [3, 4, 5, 2, 1]

def solution(num_list):
    
    answer_1 = ''
    answer_2 = ''
    for i in range (len(num_list)):
        if num_list[i] % 2 == 0:
            answer_1 += str(num_list[i])
        else:
            answer_2 += str(num_list[i])
    answer = int(answer_1) + int(answer_2)
    return answer

result = solution(num_list)
print(result)

# 조건에 맞게 수열 변환하기 3

arr = [1, 2, 3, 100, 99, 98]
k = 3

def solution(arr, k):
    answer = []
    if k % 2 == 0:
        answer = [num + k for num in arr]
    else:
        answer = [num * k for num in arr]

    return answer


result = solution(arr, k)
print(result)

# 뒤에서 5등까지

num_list = [12, 4, 15, 46, 38, 1, 14]

def solution(num_list):
    answer = []
    num_list.sort()
    return num_list[0:5]

result = solution(num_list)
print(result)

# 마지막 두 원소

num_list = [2, 1, 6]

def solution(num_list):
    answer = num_list
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)
    return answer
        

result = solution(num_list)
print(result)

# n보다 커질 때까지 더하기

numbers = [34, 5, 71, 29, 100, 34]
n = 123

def solution(numbers, n):
    answer = 0
    for i in range(0, len(numbers)):
        answer += numbers[i]
        if answer > n:
            return answer

result = solution(numbers, n)
print(result)

# 홀짝에 따라 다른 값 반환하기

n = 7

def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                answer += int(i*i)
                
    else:
        for i in range(1, n+1):
            if i % 2 == 1:
                answer += i
               
    return answer

result = solution(n)
print(result)

# 카운트 업

start_num = 3
end_num = 10

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer += [i]
        
    return answer

result = solution(start_num, end_num)
print(result)

# 원소들의 곱과 합

num_list = [3,4,5,2,1]

def solution(num_list):
    answer = 0
    multiple = 1
    add = 0

    for i in num_list:
        multiple *= i
        add += i
        
        if multiple < add*add:
            answer = 1
        else:
            answer = 0
    return answer

result = solution(num_list)
print(result)

# 수 조작하기 1

control = 'wsdawsdassw'
n = 0

def solution(n, control):
    answer = 0
    for i in control:
        if i == 'w':
            answer += 1
        elif i == 's':
            answer -= 1
        elif i == 'd':
            answer += 10
        elif i == 'a':
            answer -= 10
    return answer

result = solution(n, control)
print(result)

# 길이에 따른 연산

num_list = [2,3,4,5]

def solution(num_list):
    answer = 0 

    if len(num_list) >= 11:
        for i in num_list:
            answer += i
            
    else:
        answer = 1        # 곱셈 연산을 하기 위해 1로 초기화 시켜준 것이다. 
        for i in num_list:
            answer *= i
    return answer
result = solution(num_list)
print(result)