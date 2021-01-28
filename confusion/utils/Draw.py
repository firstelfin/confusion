#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: elfin-2020
# @Time: 2020/12/25 17:02
# project: confusion

import os
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.metrics import confusion_matrix


class ConfusionMatrixHeatMap(object):
    """
    The class is used to draw the confusion matrix of multi classification.
    Attribute:
        x: confusion matrix data;
        labels: Label in calculating confusion matrix;
        line_widths: The distance between the elements of HeatMap;
        chinese: Do you support Chinese, please set font_dir;
        color_map: Color space.
    """

    def __init__(self, x, labels=None, line_widths=0.0,
                 chinese="", color_map=""):
        self.x = x
        self.labels = labels
        self.line_widths = line_widths
        self.chinese = chinese
        if chinese and os.path.exists(chinese):
            self.font = FontProperties(fname=chinese, size=14)
        else:
            self.font = None
        self.color_map = color_map

    def show(self, save=""):
        # ---------------------set canvas--------------------- #
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twiny()
        x2tick_location = ax1.xaxis.get_ticklocs()
        ax2.set_xticks(x2tick_location)
        ax2.set_xticklabels(x2tick_location)
        ax1.set_xticks([])
        # -------------------set canvas end------------------- #

        x_matrix = pd.DataFrame(data=self.x,
                                index=self.labels,
                                columns=self.labels)
        sns.heatmap(x_matrix, annot=True,
                    fmt="d", linewidths=self.line_widths,
                    cmap=self.color_map)
        if not self.chinese:
            ax1.set_ylabel("Real")
            ax2.set_xlabel("Predict")
            plt.title("confusion Matrix", fontproperties=self.font)
        else:
            try:
                ax1.set_ylabel("真实", fontproperties=self.font)
                ax2.set_xlabel("预测", fontproperties=self.font)
                plt.title("混淆矩阵", fontproperties=self.font)
            except RuntimeWarning:
                raise RuntimeWarning(f"The {self.font} file isn't a Chinese font file.")
        # save the fig to the save_dir
        if save:
            if not os.path.exists(save):
                os.makedirs(save)
            plt.savefig(save + "/confusion_matrix.png", bbox_inches="tight")
        plt.rcParams["font.sans-serif"] = ["SimHei"]
        plt.show()
        plt.close()
        return


if __name__ == '__main__':
    label = ["dog", "cat"]
    y_true = [label[random.randint(0, 1)] for _ in range(10)]
    y_pred = [label[random.randint(0, 1)] for _ in range(10)]
    confusion_matrix1 = confusion_matrix(y_true=y_true,
                                         y_pred=y_pred,
                                         labels=label)
    # 输出y_true、y_pred、confusion_matrix
    print(f"y_true: {y_true}")
    print(f"y_pred: {y_pred}")
    print(confusion_matrix1)
    # 输出并保存混淆矩阵
    font_dir = "C:/Windows/Fonts/simkai.ttf"
    save_dir = "./save/"
    my_confusion_matrix = ConfusionMatrixHeatMap(confusion_matrix1, labels=label,
                                                 line_widths=0.7, chinese=font_dir,
                                                 color_map="YlGnBu")
    my_confusion_matrix.show(save=save_dir)
