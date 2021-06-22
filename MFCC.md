<font size=20 color=CadetBlue face="微软雅黑"><center>MFCC</center></font>

# 梅尔倒谱系数（Mel-scaleFrequency Cepstral Coefficients）

根据人耳听觉机理的研究发现，人耳对不同频率的声波有不同的听觉敏感度。从200Hz到5000Hz的语音信号对语音的清晰度影响对大。两个响度不等的声音作用于人耳时，则响度较高的频率成分的存在会影响到对响度较低的频率成分的感受，使其变得不易察觉，这种现象称为 🌈 **<font color=Darkorange>掩蔽效应</font>**。

由于频率较低的声音在内耳蜗基底膜上行波传递的距离（速度）大于频率较高的声音，故一般来说，低音容易掩蔽高音，而高音掩蔽低音较困难。 在低频处的声音掩蔽的临界带宽较高频要小。所以，**<font color=Darkorange>人们从低频到高频这一段频带内按临界带宽的大小由密到疏安排一组带通滤波器，对输入信号进行滤波</font>**。

## 梅尔标度频率

```py
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(8001)
y = 2595 * np.log10(1+x/700)

plt.plot(x, y, color='blue', linewidth=3)

plt.xlabel("f", fontsize=17)
plt.ylabel("Mel(f)", fontsize=17)
plt.xlim(0,x[-1])
plt.ylim(0,y[-1])

plt.savefig('mel_f.png', dpi=500)
```
