
#%%

import matplotlib.pyplot as plt

population_ages = [4,8,25,111,54,36,76,123,119,108,98,68,29,19,16,115,129,147,85,37,49,29,95,103,33,77,92,47,69,83,88,123]

bins = [i for i in range(0,131,10)]

plt.hist(population_ages,bins,histtype='bar',color='c')
plt.xlabel('Population ages ')
plt.ylabel('bin count')
plt.title('Analysis of Population ages')

plt.show()