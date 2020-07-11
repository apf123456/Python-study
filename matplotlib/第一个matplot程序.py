import numpy as np
from matplotlib import pyplot as plt  

x=np.arange(1,11)
y=x*2+5
plt.title("Matplotlib Demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()