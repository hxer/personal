#高级算法分析与设计考试内容

> 开卷, 内容：书上13-19章

---

* 1.在串的模式匹配中，检测一个文本串 X=x1x2x3...xn中是否包含有一个子串Y=y1y2y3...ym，（n>=m）
现在提供的算法：

    + 蛮力方法 
    + Monte Carlo算法 
    + Las Vegas算法

    判断可行性 

> 不可行，简单的说，首先，需要运行一定的比较多的次数；其次，即使通过测试，也不一定是正确的。不管是在时间和正确与否上都不能保证。好像是这样子的。

* 2.(16.8)说明如何有效地在一个给定的剩余图中找到一条增广路经。

* 3.(16.10)给出一个有效的算法，可以在一个给定的有向无回路图中，寻找最大瓶颈容量的路径。

* 4.(P296)设点集凸包上的顶点按照逆时针顺序依次是：P1,P2,P3,...,Pm,当沿着逆时针方向扫过该点集边界时，Pk是第一个离边PmP1最远的顶点，而Pl是第一个离边P1P2最远的顶点，则试证明：Pk与Pl中任意顶点(包括Pk和Pl)和P1形成一个跖对，且其余各顶点均不和P1形成跖对。

* 5.(19.15)设P是一个凸多边形，为简单起见，假设它的每个顶点只有一个最远邻点。对于P的任意顶点x，用f(x)记x的最远邻点。试证明：2个顶点x，y的 2条线段 xf(x),yf(y) 必定相交。
