#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: elfin-2020
# @Time: 2020/12/25 17:03
# project: confusion
import os
import sys
import time
import random
from sklearn.metrics import confusion_matrix

sys.path.append(os.getcwd())
from confusion.utils.Draw import ConfusionMatrixHeatMap as CH


def draw(y_t, y_p, labels, font, c_map="YlGnBu", save=""):
    confusion_matrix1 = confusion_matrix(y_true=y_t,
                                         y_pred=y_p,
                                         labels=labels)
    my_confusion_matrix = CH(confusion_matrix1, labels=labels,
                             line_widths=0.7, chinese=font,
                             color_map=c_map)
    my_confusion_matrix.show(save=save)


def main():
    label = ["dog", "cat", "horse"]
    y_true = [label[random.randint(0, 2)] for _ in range(10)]
    y_pred = [label[random.randint(0, 2)] for _ in range(10)]

    # 输出y_true、y_pred、confusion_matrix
    # print(f"y_true: {y_true}")
    # print(f"y_pred: {y_pred}")
    # print(confusion_matrix1)
    # 输出并保存混淆矩阵
    font_dir = "C:/Windows/Fonts/simkai.ttf"
    save_dir = "./save/"
    print("模型测试……")
    time.sleep(3)
    draw(y_true, y_pred, label, font_dir, "YlGnBu", save_dir)


if __name__ == '__main__':
    main()
