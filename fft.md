# <center>傅里叶变换</center>

<font size=10 color=Darkorange><center>
信号的绝对可积是傅里叶变换存在的充分条件
</center></font>

$$\int_{-\infty}^{\infty} |f(t)| dt < \infty$$

## 一、狄利克雷条件

一个信号存在傅里叶变换的充分不必要条件（只要满足，一定存在；傅里叶变换存在不一定需要此条件，即此条件是严格条件）

- 在一个周期内，连续或者只有有限个第一类间断点（可去、跳跃间断点）；
- 在一个周期内，极大值和极小值的数目应是有限个；
- 在一个周期内，信号是绝对可积的；

## 二、周期函数，傅里叶级数

频谱是离散的

$\omega_0$ 是周期函数的模拟频率，可以发现傅里叶级数将函数展开成基频率的n倍；

$$
\begin{aligned}
\Large F_n&=\frac{1}{T}\int_{\frac{-T}{2}}^{\frac{T}{2}}f(t)\cdot e^{-jn{\rm\omega_0} t} \\
\\
\normalsize f(t)&=\sum\limits_{n=-\infty}^{\infty}F_ne^{jn\omega_0 t}
\end{aligned}
$$

## 三、非周期函数，傅里叶变换

频谱是连续的

对于非周期函数，可以看作 $T\rightarrow\infty,\quad \omega_0\rightarrow d\omega,\quad n\omega_0\rightarrow\omega$ 对 $F_n=\frac{1}{T}\int_{\frac{-T}{2}}^{\frac{T}{2}}f(t)\cdot e^{-jn\omega_0 t}$ 两边同乘以 $T$ 并取极限得  

$$
\begin{aligned}
\Large F(w) &= \lim\limits_{T\rightarrow\infty}F_nT=\int_{-\infty}^\infty f(t)e^{-jwt}dt \\
\\
\normalsize f(t)&=\lim\limits_{T\rightarrow\infty}\sum\limits_{n=-\infty}^{\infty}F_ne^{jn\omega_0t}=\frac{1}{2\pi}\int_{-\infty}^\infty F(w)e^{j\omega t}d\omega
\end{aligned}
$$

## 四、离散时间傅里叶变换

## 五、离散傅里叶变换

$$
\begin{aligned}
\Large X(e^{j\omega})&=\frac{1}{N}\sum\limits_{n=0}^{N-1}x(n)W^{nk}_N,\quad W_N^{kn}=e^{-j\frac{2\pi}{N}} \\
\\
\normalsize x(n)&=\sum\limits_{k=0}^{N-1}X(e^{j\omega})W_N^{-kn}
\end{aligned}
$$
