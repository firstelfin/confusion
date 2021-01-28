<p>
    <center><h1>Confusion</h1></center>
	<br />
    <p align="center">
        <b>作者：</b><b><a href="https://github.com/firstelfin">elfin</a></b>&nbsp;&nbsp;
        <b>资料来源：<a href="https://packaging.python.org/guides/distributing-packages-using-setuptools/">setuptools</a></b>
	</p>
</p>
---

<p name="top" id="top">
    <b>目录</b>
</p>


---

## 1、项目简介

Confusion项目是一个绘制混淆矩阵的轻量级项目，支持用户自定义输入中英文注释，具体参考项目接口介绍。



## 2、draw ##

项目的主接口由draw函数给出，主要的参数有：

*   y_t：真实的标签列表；
*   y_p：预测的标签列表；
*   labels：数据集的所有标签，这里的元素要和y_t与y_p元素对应；
*   font：字体，可选择你环境下已有的字体；
*   c_map：颜色空间，默认为"YlGnBu"；
*   save：保存的路径，默认为空，不保存。



## 3、使用display ##

以下代码是测试案例。

```python
from confusion.display import draw

label = ["dog", "cat", "horse"]
y_true = [label[random.randint(0, 2)] for _ in range(10)]
y_pred = [label[random.randint(0, 2)] for _ in range(10)]

# 输出并保存混淆矩阵
font_dir = "C:/Windows/Fonts/simkai.ttf"
save_dir = "./save/"
draw(y_true, y_pred, label, font_dir, "YlGnBu", save_dir)
```

你也可以使用display进行默认测试：

```shell
python display.py
```

## 4、使用utils.Draw ##

utils包下面的Draw.py文件是项目逻辑实现的主要文件，其中类**ConfusionMatrixHeatMap**是绘制混淆矩阵热力图的主要实现。其初始化参数为：

*   **x：**混淆矩阵；
*   **labels：**标签列表，同3中所诉；
*   **line_widths：**默认为0.0，此参数设置绘制的热力图源元素离散后的间隔大小；
*   **chinese：**中文字体路径，默认为：""，即不支持中文设置标签等信息；
*   **color_map：**颜色空间，默认为：""，上一节中，默认为"YlGnBu"。



---

<p align="right">
    <b></b><a href="#top">Top</a></b>
	&nbsp;<b>---</b>&nbsp;
	<b></b><a href="#bottom">Bottom</a></b>
</p>
<p name="bottom" id="bottom" align="left">
    完！
</p>