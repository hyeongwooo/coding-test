start, end_num  = map(int, input().strip().split(' '))
def solution(start, end_num):
    answer = []
    while start >= end_num: # start가 end_num 보다 크거나 같을 때까지 반복문 실행
        answer.append(start) # 현재의 start값을 answer list 에 추가 
        start -= 1
    return answer
result = solution(start, end_num)
print(result)

