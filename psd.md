<font size=15><center>PSD</center></font>

<font size=10 color=Darkorange><center>
PSD即功率谱，功率谱密度；
FFT对于确定信号=PSD对于随机信号；
</center></font>

> **所以求功率谱PSD就有了两种方法：**
>1. (傅立叶变换的平方)/(区间长度)； -- 确定信号
>2. 自相关函数的傅里叶变换。这两种方法分别叫做直接法和相关函数法； -- 随机信号

## 1. :fire:能量谱和功率谱之间的关系

功率谱是信号自相关函数的傅里叶变换，能量谱是信号本身傅立叶变换幅度的平方。
<font color=green>
 根据parseval定理，信号傅氏变换模平方被定义为能量谱，能量谱密度在时间上平均就得到了功率谱。即
 $$
 功率谱=\frac{能量谱}{时间（采样点数）}
 $$
 </font>

## 2. :fire:工程中

_在工程实际中，即便是功率信号，由于持续的时间有限，可以直接对信号进行傅里叶变换，然后对得到的幅度谱的模求平方，再除以持续时间来估计信号的功率谱。_

<font color=green>都是采用周期图法的改进，没有使用自相关函数取 fft 变换</font>

对确定性的信号，特别是非周期的确定性信号，常用能量谱来描述。而对于随机信号，由于持续期时间无限长，不满足绝对可积与能量可积的条件，因此不存在傅立叶变换，所以通常用功率谱来描述。

### 2.1. 周期图法

把 $N$ 点观测数据看做能量有限的信号，直接对其进行傅里叶变换，然后取其模值的平方，并除以 $N$，得到观测数据真实的功率谱的估计。
周期图法很简单，直接使用谱估计性能很差，因此在使用时一般使用改进的周期图法。

### 2.2. 平均周期图法

对一个随机变量观测时，得到 $M$ 组独立数据，每组数据长为 $L$。对每一组求PSD，之后将$M$个PSD加起来求平均。这样得到的均值不变，但是方差是原来的 $\frac{1}{M}$。

平均周期图法仍然是有偏估计，偏移和每组数据长度 $L$ 有关。由于每段fft的长度变为 $L$，频谱分辨率更低 $\Delta{fs}=\frac{fs}{L}$，因此，平均周期图法以分辨率的降低换取了估计方差的减少。  

### 2.3. 窗函数法

窗函数法是将长度为 $N$ 的观测数据乘以同一长度的数据窗 $\omega$，数据加窗后，谱估计值的数学期望等于真实谱值与窗谱函数的平方卷积，因而是有偏估计。

### 2.4. 修正的周期图平均法

又称 Bartlett 法，首先把长度为N的数据分成 $M$ 段，每段数据长为 $L$，则 $N=ML$。然后把窗函数 $\omega$ 加到每段数据上，求出每段的周期图，之后对每段周期图进行评价。

### 2.5. 加权交叠平均法

又称 Welch 法。对 Bartlett 法的改进。首先，分段时相邻两段可以重叠，其次，窗函数使用汉宁窗或汉明窗，通过改进，达到进一步减小方差的目的。

## 3. Matlab

```
Fs = 1000;
nfft = 1000;  %fft采样点数

%产生序列
n = 0:1/Fs:1;
xn = cos(2*pi*100*n) + 3*cos(2*pi*200*n)+(randn(size(n)));
subplot(5,1,1);plot(xn);title('加噪信号');xlim([0 1000]);grid on
%FFT
Y = fft(xn,nfft);
Y = abs(Y);
subplot(5,1,2);plot((10*log10(Y(1:nfft/2))));title('FFT');xlim([0 500]);grid on
%FFT直接平方
Y2 = Y.^2/(nfft);
subplot(5,1,3);plot(10*log10(Y2(1:nfft/2)));title('直接法');xlim([0 500]);grid on
%周期图法
window = boxcar(length(xn));  %矩形窗
[psd1,f] = periodogram(xn,window,nfft,Fs);
psd1 = psd1 / max(psd1);
subplot(5,1,4);plot(f,10*log10(psd1));title('周期图法');ylim([-60 10]);grid on
%自相关结果
cxn = xcorr(xn,'unbiased');  %计算自相关函数
%自相关法
CXk = fft(cxn,nfft);
psd2 = abs(CXk);
index = 0:round(nfft/2-1);
k = index*Fs/nfft;
psd2 = psd2/max(psd2);
psd2 = 10*log10(psd2(index+1));
subplot(5,1,5);plot(k,psd2);title('间接法');grid on
```