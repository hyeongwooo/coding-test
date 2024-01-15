a, b = map(int, input().strip().split(' '))  # strip() --> 문자열 양 끝의 공백을 제거  // split() --> 문자열을 공백을 기준으로 나눠 리스트로 만든다.  // map(int, ...) --> 나뉜 각 요소를 정수로 변환
if a>=1 and b<=100:
    c = a + b
    print(f"{a} + {b} = {c}")

# a, b = input() --> 두 개의 값이 있는 것처럼 보일 수 있지만 실제로는 입력한 문제열 전체가 하나의 값으로 간주된다. 
# if a>=1 and b<=100:
#     c = a + b
#     print(f"{a} + {b} = {c}")

