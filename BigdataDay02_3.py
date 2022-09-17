import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('sheet2.xlsx', engine='openpyxl')
pd.set_option('display.precision',1)
df.set_index('Unnamed: 0', inplace = True)
df.index = ['출생아수','조출생률','합계출산율','사망자수','조사망률','전체','남자','여자']
df.columns =[year for year in range(2012, 2022)]
x =df.columns
y1 = df.loc['출생아수'].values
y2 = df.loc['합계출산율'].values
fig, bAx = plt.subplots()
bAx.bar(x,y1,color = "pink")
bAx.set_xticks(x)
bAx.set_xlabel('Year')

sub = bAx.twinx()
sub.plot(x, y2, '-p', color = 'gold', linewidth = 2, markersize =10 )



plt.xticks(x)
plt.show()
