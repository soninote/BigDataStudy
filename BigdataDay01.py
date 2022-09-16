
# 데이터 입력 받기 - map 함수로 숫자 입력받기

'''
a = int(input("숫자 a를 입력하시오"))
b = int(input("숫자 b를 입력하시오"))

print(a+b)


'''

'''
# 문자형으로 입력받음

a = input("숫자 a를 입력하시오")
b = input("숫자 b를 입력하시오")

print(a+b)


'''

'''
# 오류  -  Type error
a, b, c = int(input("숫자 3개를 입력하시오").split(","))

print(a,b,c)
'''

# 해결  - map 함수 사용


a, b, c = map(int, input("숫자 3개를 입력하시오").split(","))

print(a+b+c)
