# It is mainly used to give relation between the group of activities
#%%
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

sleeping = [6,5,7,6,8,7,9]
playing  = [2,2,2,2,3,3,3]
eating   = [2,2,2,2,2,2,2]
studying = [11,13,12,11,12,9,11]

#plt.plot([ ],[ ] ,label='sleeping',linewidth = 5)
#plt.plot([ ],[ ] ,label='playing',linewidth = 5)
#plt.plot([ ],[ ] ,label='eating',linewidth=5)
#plt.plot([ ],[ ] ,label='studying',linewidth=5)

plt.stackplot(days,sleeping,playing,eating,studying)
plt.title('My Schedule')
plt.xlabel('Week Days')
plt.ylabel('No of Hours')
plt.legend()
plt.show()