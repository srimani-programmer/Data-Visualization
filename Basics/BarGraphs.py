
#%%
import matplotlib.pyplot as plt

x1 = [1,3,5,7,9,11]
y1 = [2,4,6,8,10,12]

x2 = [i*i for i in range(6)]
y2 = [i*i*i for i in range(6)]

plt.bar(x1,y1,label='bar1',color='cyan')
plt.bar(x2,y2,color='green',label='bar2')
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.title('Bar-Graph')
plt.legend()
plt.show()
