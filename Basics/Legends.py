import matplotlib.pyplot as plt

x1 = [i for i in range(10000)]
y1 = [i for i in range(1000,11000)]

x2 = [i*i for i in range(50,100)]
y2 = [i*i*i for i in range(50)]

plt.plot(x1,y1,label = 'linear')
plt.plot(x2,y2,label='non-linear')
plt.xlabel('x-axis')
plt.ylabel('Y-axis')
plt.title('Graph Between linear and Non-linear')
plt.legend()

plt.show()