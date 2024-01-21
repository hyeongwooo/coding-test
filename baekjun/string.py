# 백준 11654 아스키 코드
n = input()
print(ord(n)) # ord(): 문자의 아스키 코드값을 리턴하는 함수이다. 
#               chr(): 아스키 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수

# 백준 2743 단어 길이 재기
n = input()
print(len(n))

# 백준 2744 대소문자 바꾸기
string = input()
print(string.swapcase())

# 백준 2754 학점계산
dic = {'A+': '4.3', 'A0': '4.0', 'A-': '3.7', 'B+': '3.3', 'B0': '3.0', 'B-': '2.7', 'C+': '2.3', 'C0': '2.0', 'C-': '1.7', 'D+': '1.3', 'D0': '1.0', 'D-': '0.7', 'F': '0.0'}
grade = input()
print(dic[grade])

# 백준 27866 문자와 문자열
string = input()
n = int(input())
print(string[n-1])

# 백준 11718 문자열 그대로 출력하기
import sys          # 이 문제에서는 입력을 얼마나 하는지 주어지지 않았기 때문에 try & except문을 통해 EOF 에러 발생시 break
while True:
    try:
        print(input())
    except EOFError:
        break

# 백준 9086 문자열
n = int(input())
for i in range(n):
    string = str(input())
    print(string[0]+string[-1])
