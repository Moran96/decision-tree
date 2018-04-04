通过计算信息增益,可以选择出最好的数据划分方式.
度量集合内信息的无序程度的两种方式:
* 香农熵(Shannon entropy)
* 基尼不纯度(Gini impurity)
---
## 信息的定义
如果待分类的**样本**可能划分在多个分类中,
则符号\(x_i\)的信息定义为
$$l(x)=-log_2 p(x_i)$$其中\(p(x_i)\)是选择该分类的概率.
计算所有类别所有可能的信息期望值:
$$H=\sum_{i=1}^n l(x_i)p(x_i)=-\sum_{i=1}^n p(x_i) log_2 p(x_i)$$

## 香农熵的特性
香农熵越大,集合内信息的label种类越多,集合体现无序.
```python
>>> importlib.reload(trees)
<module 'trees' from '/Users/a/Desktop/WorkSpace/Decision-Tree/trees.py'>
>>> data
[[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
>>> trees.calculate_shannon_entropy(data)
0.9709505944546686
>>> data[0][-1] = 'maybe'
>>> data
[[1, 1, 'maybe'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
>>> trees.calculate_shannon_entropy(data)
1.3709505944546687
```
## Question
* 香农熵在决策树里有何作用?
香农熵作为划分数据集过程中的一个重要参数,可依据熵的值判断数据集划分是否恰当.

## Notice
* 数学公式与程序代码的纽带是算法.但是从数学移植到代码的过程是需要针对具体问题的.
* 本文的公式仅是体现在数学层面,其具体含义和实现过程需要参考函数代码:
[trees.py: calculate_shannon_entropy()](www.cctv.com)
* 由以上两公式移植出的calculate_shannon_entropy()函数是具有使用范围的.首先,只要使用了分类概率 \(p(x_i)\),就已经默认了每一个样本的ground-truth为已知.即函数的传入参数只能为训练样本集或其子集.
