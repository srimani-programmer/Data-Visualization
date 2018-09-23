import matplotlib.pyplot as plt
import numpy as np
#%%

sleeping = [6,5,7,6,8,7,9]
playing  = [2,2,2,2,3,3,3]
eating   = [2,2,2,2,2,2,2]
studying = [11,13,12,11,12,9,11]

my_activities = ['sleeping','playing','eating','studying']
slides = [sum(sleeping),sum(playing),sum(eating),sum(studying)]
plt.pie(slides,labels=my_activities)
plt.axis('equal')
plt.title('Total Week Analysis...!')

plt.show()