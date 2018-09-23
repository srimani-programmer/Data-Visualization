# scatter plots are used to relate two variables with in a distribution
#%%
import matplotlib.pyplot as plt

x = [i*i for i in range(50)]
y = [i*i*i for i in range(50)]

plt.scatter(x,y,marker='o',s=15)
plt.xlabel('squares')
plt.ylabel('cubes')
plt.title('Square V/S Cubes')

plt.show()