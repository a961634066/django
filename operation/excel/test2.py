# -*-coding:utf-8 -*-
'''
@Time: 2021/6/24 14:31
@desc: 
'''
import os
import sys

import pandas as pd

file_name = 'test.xlsx'
in_excel_file_name = '../test/{}'.format(file_name)
out_excel_file_name = '{}.xlsx'.format(os.path.basename(file_name))

sheet_name = 'Sheet1'

df = pd.read_excel(in_excel_file_name)
# 将画图结果另存为一个文件
out_excel_file_path = os.path.join(sys.path[0], '输出')
if not os.path.exists(out_excel_file_path):
    os.makedirs(out_excel_file_path)
out_excel_file_name = os.path.join(out_excel_file_path, out_excel_file_name)

writer = pd.ExcelWriter(out_excel_file_name, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name, index=False)

workbook = writer.book
worksheet = writer.sheets[sheet_name]

# 设置颜色
points = []

points.append({'fill': {'color': '#eeb1aa'}})
points.append({'fill': {'color': '#01c4ea'}})

# 遍历行 type:doughnut为环形饼状图
for index, row in df.iterrows():
    chart = workbook.add_chart({'type': 'doughnut'})
    chart.set_title({'name': row['NAME']})  # 依据Excel文件中NAME列设置图表标题
    chart.add_series({
        'categories': '={}!$C$1:$D$1'.format(sheet_name),  # 根据C列~D列绘制
        'values': '={}!$C${}:$D${}'.format(sheet_name, index + 2, index + 2),  # C列~D列图表值
        'points': points
    })
    # 中心环形大小百分比
    chart.set_hole_size(50)

    # The default chart width x height is 480 x 288 pixels
    size1 = {'width': 185, 'height': 100}
    size2 = {'width': 185, 'height': 104}
    size3 = {'width': 185, 'height': 110}

    # 针对不同列属性绘制不同大小的图表
    if row['因素'] <= 6:
        chart.set_size(size1)
    elif 6 < row['因素'] <= 9:
        chart.set_size(size2)
    else:
        chart.set_size(size3)

    # anchored to cell 每行绘制5个，x_offset为图片偏移值
    # insert_chart('I{}'....)的参数 I为插入图片列
    x_offset = index % 5
    chart_pos_offset = int(index / 5)
    worksheet.insert_chart('I{}'.format(chart_pos_offset * 7 + 1), chart, {'x_offset': 200 * x_offset})

writer.save()
workbook.close()