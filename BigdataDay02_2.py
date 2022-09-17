import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.font_manager as fonm
'''
# 설치된 폰트 확인 코드
fontl = [font.name for font in fonm.fontManager.ttflist]
for f in fontl:
    print(f"{f}.ttf")
    '''
'''
#꺾은선 그래프
x = np.linspace(0, 2*math.pi,30)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(6,5)) #인쇄시 그래프 크기, inch단위
plt.title('1.py')


plt.rcParams['font.size']= 10
plt.plot(x,y1, 'g--*', label = "hi")
plt.plot(x,y2, 'y:p', label = "hello")

plt.legend()
plt.show()

'''
'''

name = ['Kim', 'Lee','Park', 'Jeong','Choi','Ha','Yoon']
x= np.arange(7) # x는 0에서 7까지의 정수로 구성된 배열
np.random.seed(1)
score = np.random.randint(50, 101, 7)
score2 = np.random.randint(50, 101, 7)
plt.bar(x-0.2, score, color='lightblue', width = 0.4) #막대그래프
plt.bar(x+0.2, score2, color='pink', width = 0.4) #막대그래프
plt.xticks(x,name)

font = {
        'family': 'sans-serif',
        'color' : 'darkgrey',
        'weight': 'normal',
        'size': 9,
        'ha': 'center'
    }
font2 = {
        'family': 'sans-serif',
        'color' : 'grey',
        'weight': 'normal',
        'size': 9,
        'ha': 'center'
    }

for i in x : # 가로위치, 세로위치, 배열인덱스 , 글자색, 
    plt.text(i-0.2, score[i]-7, score[i],  fontdict = font)
    plt.text(i+0.2, score2[i]-7, score2[i],  fontdict = font2)

plt.show()

print ('설정파일 위치: ', mpl.matplotlib_fname())



'''


#원형그래프
plt.rcParams['font.family']='NanumBarunGothic'
지출항목 = ['가','나','다','라','마']
지출금액 = [3,4,5,6,7]
plt.pie(지출금액, labels = 지출항목)
plt.show()
