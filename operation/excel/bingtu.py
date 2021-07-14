# -*-coding:utf-8 -*-
'''
@Time: 2021/7/14 18:10
@desc: 
'''



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,9))    #设置图形大小宽高
labels = '中专','大专','本科','硕士','其他'
fracs = [0.2515,0.3724,0.336,0.0368,0.0057]
explode = [0,0,0.1,0,0]   #凸出这一部分

plt.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）解决乱码问题
plt.axes(aspect = 1)    # set this , Figure is round, otherwise it is an ellipse
#autopct ，show percet
plt.pie(x=fracs,labels=labels,explode=explode,autopct='%3.1f %%',
        shadow=True,labeldistance=1.2,startangle=0,pctdistance=0.8)
plt.title("失信用户受教育水平分布：")
plt.show()

'''labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
shadow，饼是否有阴影
startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
pctdistance，百分比的text离圆心的距离
patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本'''
