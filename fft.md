<font size=20 color=CadetBlue face="微软雅黑"><center>频谱分析</center></font>

-------------

# 1. Best Understanding

# 2. 傅里叶变换

<font size=10 color=Darkorange><center>
信号的绝对可积是傅里叶变换存在的充分条件
</center></font>

$$\large\int_{-\infty}^{\infty} |f(t)| dt < \infty$$
> 这边积分区间为 $-\infty$ 到 $\infty$ 与狄利克雷条件一致，因为信号默认非周期，看作周期 $T\rightarrow\infty$。
> 狄利克雷条件默认面向周期函数，故其积分区间为 $\frac{-T}{2}$ 至 $\frac{T}{2}$。

## 2.1. 狄利克雷条件

一个信号存在傅里叶变换的充分不必要条件（只要满足，一定存在；傅里叶变换存在不一定需要此条件，即此条件是严格条件）

- 在一个周期内，连续或者只有有限个第一类间断点（可去、跳跃间断点）；
- 在一个周期内，极大值和极小值的数目应是有限个；
- 在一个周期内，信号是绝对可积的；

## 2.2. 周期函数，傅里叶级数

频谱是离散的

$\omega_0$ 是周期函数的模拟频率，可以发现傅里叶级数将函数展开成基频率的n倍；

$$
\begin{aligned}
\Large F_n&=\frac{1}{T}\int_{\frac{-T}{2}}^{\frac{T}{2}}f(t)\cdot e^{-jn{\rm\omega_0} t} \\
\\
\normalsize f(t)&=\sum\limits_{n=-\infty}^{\infty}F_ne^{jn\omega_0 t}
\end{aligned}
$$

## 2.3. 非周期函数，傅里叶变换

频谱是连续的

对于非周期函数，可以看作 $T\rightarrow\infty,\quad \omega_0\rightarrow d\omega,\quad n\omega_0\rightarrow\omega$ 对 $F_n=\frac{1}{T}\int_{\frac{-T}{2}}^{\frac{T}{2}}f(t)\cdot e^{-jn\omega_0 t}$ 两边同乘以 $T$ 并取极限得  

$$
\begin{aligned}
\Large F(j\omega) &= \lim\limits_{T\rightarrow\infty}F_nT=\int_{-\infty}^\infty f(t)e^{-jwt}dt \\
\\
\normalsize f(t)&=\lim\limits_{T\rightarrow\infty}\sum\limits_{n=-\infty}^{\infty}F_ne^{jn\omega_0t}=\frac{1}{2\pi}\int_{-\infty}^\infty F(w)e^{j\omega t}d\omega
\end{aligned}
$$

## 2.4. 离散时间傅里叶变换

## 2.5. 离散傅里叶变换

$$
\begin{aligned}
\Large X(e^{j\omega})&=\frac{1}{N}\sum\limits_{n=0}^{N-1}x(n)W^{nk}_N,\quad W_N^{kn}=e^{-j\frac{2\pi}{N}} \\
\\
\normalsize x(n)&=\sum\limits_{k=0}^{N-1}X(e^{j\omega})W_N^{-kn}
\end{aligned}
$$

# 3. 拉普拉斯变换

:sunrise_over_mountains: CTFT 是将连续时间信号变换到频域，将频率的含义扩充以后，就得到拉普拉斯变换。

>很多教材对于频率的含义没有明确规定，由于CTFT和DTFT的形式分别为 $X(j\omega)$ 和 $X(e^{j\omega})$，因此很多人误将频率理解为 $j\omega$ 和 $e^{j\omega}$。但事实上我们在绘制频谱图的时候，取的自变量都是 $\omega$，这样才能画出函数图像。否则CTFT和DTFT都将变成复平面上变化的函数，无法画出函数图像了。而且我们日常用到频率这一概念时所说的 $f$，都是 $f=\frac{\omega}{2\pi}$。其对应的角频率恰恰是实数 $\omega$，而不是复数 $j\omega$ 或 $e^{\omega}$。
>
> **<font color=Darkorange>因此，我们所说的频率指的应当是 $\omega$ 而不是 $j\omega$ 或 $e^{j\omega}$</font>**。

## 3.1. 定义

CTFT 的定义公式为 $X(j\omega)=\int_{-\infty}^\infty x(t)e^{-j\omega t}dt$，这里的 $\omega$ 其实为实数。傅里叶变换要求时域信号绝对可积，即 $\int_{-\infty}^\infty |x(t)|dt < \infty$ 而功率信号不满足此条件，为了使这类不满足条件的信号也能求频谱，在 $e^{\sigma t}$ 的压迫下 $x(t)e^{\sigma t}$ 绝对可积。
$$
\begin{aligned}
X(s) &= \int_{-\infty}^\infty x(t)e^{-\sigma t}e^{-j\omega t}dt \\
&= \int_{-\infty}^\infty x(t)e^{-(\sigma + j\omega)t}dt \\
&=\int_{-\infty}^\infty x(t)e^{-st}dt \quad s=\sigma+j\omega
\end{aligned}
$$

<font color=Darkorange>拉普拉斯变换将频率从实数推广为复数，故傅里叶变换是拉普拉斯变换的一个特例，即当 $s$ 为纯虚数时，$x(t)$ 的拉普拉斯变换为其傅里叶变换</font>

# 4. Z变换

:sunrise_over_mountains: DTFT 是将离散时间信号变换到频域，将频域的含义扩充以后，就得到Z变换。 当 $|z|=1$ 时，$x[n]$ 的Z变换即为 $x[n]$ 的DTFT。

DTFT的公式是 $X(e^{j\omega})=\sum\limits_{n=-\infty}^\infty x[n]e^{-j\omega n}$，**<font color=Darkorange>这里的 $\omega$ 是连续变化的实数</font>**。同样的DTFT也需要满足绝对可和条件 $\sum\limits_{n=-\infty}^\infty |x[n]| < \infty$。为了让不满足绝对可和条件的函数 $X[n]$，也能变换到频率域，我们乘一个指数函数 $a^{-n}$， $a$ 为满足收敛域的任意实数。函数 $x[n]a^{-n}$ 的DTFT为：
$$
\large
\begin{aligned}
X(e^j\omega)&=\sum\limits_{n=-\infty}^\infty x[n]a^{-n}e^{-j\omega n}\\
&=\sum\limits_{n=-\infty}^\infty x[n](a\cdot e^{j\omega})^{-n} \\
&=\sum\limits_{n=-\infty}^\infty x[n]z^{-n} \quad z=a\cdot e^{-j\omega}
\end{aligned}
$$

>关于这里为什么对 $x[n]$ 乘以 $a^{-n}$ 而不是像拉氏变换中乘以 $e^{-\sigma n}$ ，主要是由离散序列的DTFT的周期性决定的。如果对离散序列进行拉氏变换，将 $\omega$ 映射到虚轴上，则得到的变换函数是在虚轴方向上周期变化的函数，这样就没有充分利用DTFT的周期性。而Z变换令 $z=a\cdot e^{j\omega}$ ，则当 $a=1$ ，即 $z=e^{j\omega}$ 时，随着 $\omega$ 从 $-\infty$ 向 $\infty$ 变化，z在复平面中的单位圆上以 $2\pi$ 为周期变化，如此恰能充分利用DTFT的周期性进一步简化我们的计算。

## 4.1. 定义

单位脉冲响应为 $h[n]$ 的离散时间线性时不变系统对复指数输入 $z^n$ 的响应 $y[n]$ 为
$$
\large y[n]=H(z)z^n
$$
式中 $H(z)$ 是一个复常数，为
$$
\large H(z)=\sum\limits_{n=-\infty}^{\infty}h[n]z^{-n}
$$

## 与拉普拉斯变换的关系

:sunrise_over_mountains:**Z变换本质上是拉普拉斯变换的离散形式。也称为Fisher-Z变换。对于连续信号进行抽样变换就得到了原函数的离散序列**：
$$
f_s(t) = f(t)\cdot \delta_T(t)=\sum\limits_{n=0}^{\infty}f(nT)\delta(t-nT)
$$
其中， $T$ 为采样周期， $\delta_T(t)$ 为冲激抽样。对上式进行单边拉普拉斯变换：
$$
\begin{aligned}
F_s(S)&=\int_0^\infty \sum\limits_{n=0}^{\infty}f(nT)\delta(t-nT)e^{-st}dt \\
&=\sum\limits_{n=0}^\infty f(nT)e^{-snT}\\
F(Z)&=\sum\limits_{n=0}^\infty f(nT)z^{-nT} \quad z=e^{sT}
\end{aligned}
$$

# 5. 滤波器差分方程

$$
\begin{aligned}
y(n) + b_1\cdot y(n-1) + \cdots + b_n\cdot y(0) &= a_0\cdot x(n) + a_1\cdot x(n-1) + \cdots \\
Y(z)(1+b_1z+b_2z^2+\cdots+b_nz^n)&=X(z)(a_0+a_1z+a_2z^2+\cdots+a_nz^n) \\
Y(z)&=\frac{X(z)(a_0+a_1z+a_2z^2+\cdots+a_nz^n)}{1+b_1z+b_2z^2+\cdots+b_nz^n}
\end{aligned}
$$
故令示波器的频率响应 $H(z)$ 为
$$
H(z)=\frac{\sum\limits_{i=0}^Na_iz^i}{1+\sum\limits_{i=1}^Nb_iz^i}
$$
式中 $N$ 为滤波器的阶数。

## 5.1. FIR滤波器

$b_i=0$ 即为FIR滤波器。
