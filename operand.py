a, b = map(int, input().strip().split(' '))
def solution(a, b):
    test = a[0:]+b[0:]
    if test>2*a*b:
        return test
    else:
        return 2*a*b
    result = solution(a, b)
    print(result)
    answer = 0
    return answer