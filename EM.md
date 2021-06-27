<font size=20 color=CadetBlue face="微软雅黑"><center>EM 算法</center></font>

--------------------
[知乎](https://zhuanlan.zhihu.com/p/85236423)

# 1. 定义

EM算法（Expectation-maximization），又称最大期望算法，是一种迭代算法，用于含有隐变量的概率模型参数的极大似然估计（或极大后验概率估计）。

从定义可知，该算法是用来估计参数的，这里约定参数为 $\theta$。既然是迭代算法，那么肯定有一个初始值，记为 $\theta^{(0)}$，然后再通过算法计算 $\theta^{(1)},\theta^{(2)},\ldots,\theta^{(t)}$。

***<font color=Darkorange>
通常，当模型的变量都是观测变量时，可以直接通过极大似然估计法，或者贝叶斯估计法估计模型参数。但是当模型包含隐变量时，就不能简单的使用这些估计方法。</font>***

# 2. 执行步骤

假设在第 $i$ 次迭代后参数的估计值为 $\theta^{(i)}$，对于第 $i+1$ 次迭代，分为两步:
式中 $X$ 为观测序列，$Z$ 为隐藏变量数据。

:sunrise_over_mountains: 1. E步，求期望
$$
\begin{aligned}
\Large\color{Darkorange}{Q\left(\theta, \theta^{(i)}\right)=\sum\limits_Z P(Z \;|\; X, \theta^{(i)})\log P(X,Z \;|\; \theta) \\}
\end{aligned}
$$

:sunrise_over_mountains:2. M步，求最大化
$$
\Large\color{Darkorange}{\theta^{(i+1)}=\argmax\limits_\theta Q\left(\theta, \theta^{(i)}\right)}
$$

# 3. 推导

给定一组观测数据，记为 $X=\left(x_1,\ldots,x_n\right)$, 以及参数 $\theta$。 假设所有观测 $x_1, \ldots, x_n$ 是独立同分布， 有以下对数似然函数:

$$
\begin{aligned}
\Large \ell\left(\theta\;|\;X\right) &= \log P(X\;|\;\theta)
\end{aligned}
$$