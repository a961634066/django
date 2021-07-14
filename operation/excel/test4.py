# -*-coding:utf-8 -*-

import pandas as pd

# 默认是sheetname为0，返回多表使用sheetname=[0,1]，若sheetname=None是返回全表 。注意：int/string返回的是dataframe，而none和list返回的是dict of dataframe
# header ：指定作为列名的行，默认0，即取第一行，数据为列名行以下的数据；若数据不含列名，则设定 header = None；
# index_col=0会在获取时取消序号列，写入时就不会有，但是以下注释的行会报错
"""
数据如下
序号  名称  年龄
  2   5   8
  3   6   9
"""
df = pd.read_excel("456.xls", sheet_name=0, header=0)
height, width = df.shape
print(height, width, type(df))
print df
df[u"总数"] = df[u"序号"] + df[u"名称"]
# print df.head()
print df[u"序号"].max()
print df.keys()[0]
print df.keys()[1]
print df.keys()[2]

"""
取数据的几种方法
#第一种方法：ix
df.ix[i,j]		# 这里面的i,j为内置数字索引，行列均从0开始计数
df.ix[row,col]	# 这里面的row和col为表格行列索引，也就是表格中的行与列名称

#第二种方法：loc
df.loc[row,col]	# loc只支持使用表格行列索引，不能用内置数字索引

#第三种方法：iloc
df.iloc[i,j]	# iloc只支持使用内置数字索引，不能用表格行列索引

建议还是使用loc或者iloc而不是ix为好
"""

print df.loc[0, u"序号"]
print df.loc[0, u"名称"]
print df.iloc[1, 1]
print df.iloc[0, 0]

writer = pd.ExcelWriter("789.xls", engine='xlsxwriter')
df.to_excel(writer)

workbook = writer.book
worksheet = writer.sheets["Sheet1"]

writer.save()
