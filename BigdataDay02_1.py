
# numpy 

import numpy as np
'''
emp = np.zeros((2,3,4))

print(emp)

a1 = np.zeros((2,3)) + 5 # . 있음
print (a1)

a2 = np.full((2,3), 5) # . 없음
print(a2)
'''
'''
# f-string 사용

year = 2016
print(f'arr[1][3]={year}')
'''
'''
#numpy 덧셈 a 
a = np.array([[1,3,5],[2,4,6]])
#b = np.array([1,2,1])
b = 3
print(np.add(a,b)) # or + 도 사용가능

result :

[[4 6 8]
 [5 7 9]]
'''

#난수발생 (최소, 최대,(행, 열)) - randint 사용
np.random.seed(0) # 랜덤값이 고정됨 (고정된 랜덤값 0, 1, 2....)
score = np.random.randint(60, 101, (5,3)) # 그냥 rand 는 실수형
print(score)

totalSum = np.sum(score)
totalAvg = np.mean(score)
# f-String 과 자릿수 제한 사용
print(f'전체합계{totalSum}, 전체평균 = {totalAvg:.1f}')

















