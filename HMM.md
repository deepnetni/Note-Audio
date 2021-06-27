<font size=20 color=CadetBlue face="微软雅黑"><center>HMM</center></font>

--------------------

# 1. 什么是 HMM

隐马尔可夫模型（Hidden Markov Model，HMM）是关于时许的概率模型，是一个生成模型，描述由一个隐藏的马尔科夫链随机生成不可观测的状态序列，每个状态生成一个观测，而由此产生一个观测序列。
[知乎](https://zhuanlan.zhihu.com/p/85454896)

## 1.1. HMM 的模型参数

模型参数包括 $M$ 观测变量的数量，$N$ 隐含状态的数量，$\lambda = (A, B, \pi)$ 其中
- 状态转移矩阵 $A$, $A=[a_{ij}]_{N \times N}$
- 观测概率矩阵 $B$，$B=[b_{ij}]_{N \times M}$；
- 初始概率分布 $\pi$，$\pi=[\pi_i]_N^T$；

## 1.2. HMM 三个基本问题

:mountain_biking_woman:1. 识别问题（概率计算算法），如何评估模型与观测序列之间的匹配程度。
>给定参数 $\lambda = (A, B, \pi)$ 和观测序列 $O = (o_1, o_2, \cdots, o_T)$，计算观测序列 $O$ 的条件概率 $P(O|\lambda)$；

:mountain_biking_woman:2. 学习问题（学习算法），如何训练模型使其能更好地描述观测数据。
>给定观测序列 $O$，反推参数 $A, B, \pi$；

:mountain_biking_man:3. 解码问题（预测算法），如何根据观测序列推断出隐藏地模型状态。
>给定参数 $\lambda$ 和观测序列 $O$ 求可能性最大的状态序列 $Z=(z_1, z_2, \cdots, z_T)$；

:beginner:***两个基础假设：***

> 1. 齐次马尔可夫假设：即任意时刻的状态只依赖于前一时刻的状态，与其他时刻的状态无关（当然，初始时刻的状态由参数 $\pi$ 决定）；
> $P(z_t | z_{t-1}, \cdots, z_1, o_t, \cdots, o_1) = P(z_t|z_{t-1}),\quad t=2,3,\cdots,T$
>  
> 2. 观测独立假设：即任意时刻的观测只依赖于该时刻的状态，与其他无关：
> $P(o_t | o_{t-1}, \cdots, o_1, z_t, \cdots, z_1) = P(o_t|z_t),\quad t=2,3,\cdots,T$

# 2. 识别问题-概率计算算法

关于概率的计算，由于存在隐变量，所以 $O$ 的边际概率需要将所有的联合概率 $P(O, Z)$ 加和得到
$$
\large
P(O|\lambda)=\sum\limits_Z P(O, Z|\lambda)
$$

## 2.1. 条件概率的分解

$$
\large
\left\{
\begin{aligned}
P(O, Y, Z) &= P(O, Y | Z)P(Z) = P(O|Y,Z)P(Y,Z) \\[2ex]
P(Y, Z)&=P(Y|Z)P(Z)
\end{aligned}
\right.
$$

$$
\rightarrow P(O,Y|Z)P(Z)=P(O|Y,Z)P(Y|Z)P(Z) \\[2ex]
{\Large\color{Darkorange}\rightarrow P(O,Y|Z)=P(O|Y,Z)P(Y|Z)}
$$

## 2.2. 前向概率

### 2.2.1. 定义

$$
\alpha_t(i)=P(o_1,\ldots,o_t, z_t=q_i|\lambda)
$$

$$
\begin{aligned}
\alpha_T(i)&=P(o_1,o_2,\ldots,o_T,z_T=q_i|\lambda) \\
&= P(O, z_T=q_i|\lambda)
\end{aligned}
$$

由上式可知，遍历求和 $z_T$ 可以得到 $O$ 的边缘概率，式中 $N$ 表示隐含状态的个数。

$$
\Large\color{Darkorange}{\sum\limits_i^N\alpha_T(i)=\sum\limits_i^NP(O,z_T=q_i|\lambda) = P(O|\lambda)}
$$

假设已知 $\alpha_t(q_1),\;\alpha_t(q_2),\ldots,\alpha_t(q_N)$，求 $\alpha_{t+1}(*)$

$$
\color{Darkorange}{
\begin{aligned}
\alpha_{t+1}(j) &= P(o_1,o_2,\ldots,o_{t+1},\;z_{t+1}=q_j|\lambda) \\
&=\left[\sum\limits_{i=1}^N \alpha_t(i)a_{ij}\right]b_j(o_{t+1})
\end{aligned}
}
$$

### 2.2.2. 初始值

$$
\begin{aligned}
\alpha_1(i)&=P(o_1,z_1=q_i \;|\; \lambda) \\
&=P(o_1|z_1=q_i,\;\lambda)P(z_1=q_i\;|\;\lambda) \\
&=b_i(o_1)\cdot \pi_i
\end{aligned}
$$

式中 $b_i(o)$ 表示由状态 $q_i$ 生成给定观测数据的概率，例如 $t$ 时刻观测数据 $o_t=o_j$，有
$$
b_i(o_t) = b_i(o_t=o_j)=P(o_t=o_j|z_t=q_i,\lambda)=b_{ij}
$$

## 2.3. 后向概率

### 2.3.1. 定义

$$
\begin{aligned}
&\beta_t(i) = P(o_T, o_{T-1}, \ldots, o_{t+1}|z_t=q_i,\lambda) \\[2ex]
&\Large\color{Darkorange}{\beta_t(i)=\sum\limits_{j=1}^N a_{ij}b_j(o_{t+1})\beta_{t+1}(j)}
\end{aligned}
$$

:sunny:通过后向概率计算 $P(O|\lambda)$

$$
\begin{aligned}
P(O|\lambda) &= P(o_1, o_2,\ldots,o_T|\lambda) \\
&=\sum\limits_{i=1}^N P(o_1,o_2,\ldots,o_T, z_1=q_i|\lambda) \\
&=\sum\limits_{i=1}^N P(o_1|o_2,\ldots,o_T,z_1=q_i,\lambda) P(o_2,o_3,\ldots,o_T, z_1=q_i|\lambda) \\
&=\sum\limits_{i=1}^N P(o_1|z_1=q_i)P(z_1=q_i|\lambda)P(o_T,o_{T-1},\ldots,o_2|z_1=q_i,\lambda) \\
&=\sum\limits_{i=1}^N b_i(o_1)\pi_i\beta_1(i) \\
\end{aligned}
$$

对于任意时刻 $t$，存在以下等式

$$
\Large\color{Darkorange}{P(O|\lambda)=\sum\limits_{i=1}^N \alpha_t(i)\beta_t(i)}
$$

:sunny:$\beta_t$ 与 $\beta_{t+1}$ 之间地推导:

$$
\begin{aligned}
\beta_t &= P(o_{t+1},\ldots,o_T \;|\; z_t=q_i,\lambda) \\
&=\sum\limits_{j=1}^N P(o_{t+1},\ldots,o_T, z_{t+1}=q_j \;|\; z_t=q_i, \lambda) \\
&=\sum\limits_{j=1}^N \color{red}{P(o_{t+1}, \ldots, o_T \;|\; z_{t+1}=q_j, z_t=q_i, \lambda)}
\color{green}{P\left(o_{t+1} \;|\; z_t,\lambda \right)}
\end{aligned}
$$

上式 $\color{green}{P\left(z_{t+1} \;|\; z_t,\lambda \right)}$ 就是 $a_{ij}$ 状态转移矩阵
由于 $\color{red}{P(o_{t+1}, \ldots, o_T \;|\; z_{t+1}=q_j, z_t=q_i, \lambda)}$ 其中 $z_t$ 与 $o_{t+1},\ldots, X_T$ 无关，故可以省略化简为：

$$
\begin{aligned}
&\color{red}{P(o_{t+1}, \ldots, o_T \;|\; z_{t+1}=q_j, {\color{grey}{z_t=q_i}},\;\lambda)} \\
=&P(o_{t+1}, \ldots, o_T \;|\; z_{t+1}=q_j, \lambda) \\
=&P(o_{t+1} \;|\; o_{t+2}, \ldots, o_T, z_{t+1}=q_j)P(o_{t+2},\ldots,o_T \;|\; z_{t+1}=q_j) \\
=&P(o_{t+1}\;|\;z_{t+1}=q_j)\beta_{t+1}(j) \\
=&\color{yellow}{b_j(o_{t+1})\beta_{t+1}(j)}
\end{aligned}
$$

故
$$
\color{Darkorange}{\beta_t(i)=\sum\limits_{j=1}^N {\color{green}{a_{ij}}}{\color{yellow}{b_j(o_{t+1})\beta_{t+1}(j)}}}
$$

### 2.3.2. 初始值

$\beta_T(1)=\beta_T(2)=\cdots=\beta_T(N)=1$

# 3. 学习问题-学习算法

# 4. 解码问题-预测算法

# 5. HMM局限性

HMM不适用于：
1. 状态值存在长距离地依赖；
2. 观测值有非独立地交叉特征；
