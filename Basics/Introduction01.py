from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,20,0.01)
y = 1 + np.sin(2 * np.pi * x)

plt.plot(x,y,color='red')
plt.xlabel('time')
plt.ylabel('voltage')
plt.title('Sample Graph')

plt.show()