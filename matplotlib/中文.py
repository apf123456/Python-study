import matplotlib.pyplot as plt
import numpy as np
import matplotlib

zhfont1=matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

x=np.arange(1,11)
y=2*x+5
plt.title("菜鸟教程",FontProperties=zhfont1)
plt.xlabel("x坐标",FontProperties=zhfont1)
plt.ylabel("y坐标",FontProperties=zhfont1)
plt.plot(x,y)
plt.show()
