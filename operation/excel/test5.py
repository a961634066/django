# -*-coding:utf-8 -*-

import xlsxwriter


class Test5():

    def __init__(self):
        """
        支持的图表类型有
            area：创建区域（实线）样式图表。
            bar：创建条形（转置直方图）图表。
            column：创建列样式（直方图）图表。
            line：创建线型图表。
            pie：创建饼图样式图表。
            doughnut：创建甜甜圈样式图表。
            scatter：创建散点样式图表。
            stock：创建股票样式图表。
            radar：创建雷达样式图表。
        """
        self.char = {'type': 'pie'}

    def write(self):
        """
        :return:
        """
        """
        方式一
        chartsheet = workbook.add_chartsheet()
        # ...
        chartsheet.set_chart(chart)
        
        方式二
        workbook.add_worksheet(name="test5")
        chart = workbook.add_chart({'type': 'column'})
        worksheet.insert_chart('A7', chart)
        """
        workbook = xlsxwriter.Workbook("test5.xlsx")
        worksheet = workbook.add_worksheet(name="test5")
        chart = workbook.add_chart(self.char)
        worksheet.write_row('A1', [u"男生", u"女生", u"中性"])
        worksheet.write_row('A2', [8, 6, 2])
        """
        将数据系列添加到图表。
        chart.add_series({
        'categories': '=Sheet1!$A$1:$A$5',
        'values':     '=Sheet1!$B$1:$B$5',
        'line':       {'color': 'red'},
        })
        """
        # categories更改右侧的名字
        # data_labels饼图上显示东西，series_name是否显示外面的name，percentage是否显示百分比
        # name,系列的名称，非饼图/甜甜圈是显示的右侧名字
        chart.add_series(
            {'values': '=test5!$A$2:$C$2',
             'name': "two",
             'categories': '=test5!$A$1:$C$3',
             'data_labels': {'series_name': False, 'percentage': True}
             })
        """
        chart.set_x_axis()  # 设置图标x轴选项
        chart.set_y_axis()  # 设置图标y轴选项
        chart.set_title()   # 设置图标标题
        chart.set_style()   # 设置图标样式类型,set_style()方法用于将图表的样式设置为 Excel 中“设计”选项卡上可用的 48 种内置样式之一
        chart.set_hole_size()   # 设置圆环图孔大小
        chart.set_rotation()    # 设置饼图/甜甜圈图旋转  0 <= rotation <= 360
        """
        chart.set_title({"name": u"标题1"})
        chart.set_rotation(90)
        chart.set_style(10)
        worksheet.insert_chart('A7', chart)

        # 一个excel可以插入多个图，以下用与上面不一样的方式插入另外一个图
        chart2 = workbook.add_chart({'type': 'pie'})
        chart2.add_series(
            {'values': ["test5", 1, 0, 1, 2],
             'name': "two",
             'categories': ["test5", 0, 0, 0, 2],
             'data_labels': {'series_name': False, 'percentage': True},
             'points': [
                 {'fill': {'color': '#FF00FF'}},
                 {'fill': {'color': '#808080'}},
                 {'fill': {'color': '#FF6600'}}
             ],
             })
        chart2.set_style(38)
        worksheet.insert_chart('A23', chart2, {'x_offset': 25, 'y_offset': 10})

        workbook.close()


if __name__ == '__main__':
    t = Test5()
    t.write()
